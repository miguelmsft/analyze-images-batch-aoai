import base64  
import os  
import json  
from dotenv import load_dotenv  
from mimetypes import guess_type  
from openai import AzureOpenAI  
from pydantic import BaseModel  
from pathlib import Path  
  
# Load environment variables  
load_dotenv()  
  
# Azure OpenAI environment variables  
aoai_endpoint = os.getenv("AOAI_ENDPOINT")  
aoai_api_key = os.getenv("AOAI_API_KEY")  
aoai_deployment_name = os.getenv("AOAI_DEPLOYMENT")  
  
# Initialize the Azure OpenAI client  
client = AzureOpenAI(  
    azure_endpoint=aoai_endpoint,  
    api_key=aoai_api_key,  
    api_version="2024-08-01-preview"  
)  
  
def image_to_data_url(image_path):  
    """  
    Convert a local image file to a data URL.  
  
    Parameters:  
    -----------  
    image_path : str  
        The path to the local image file to be converted.  
  
    Returns:  
    --------  
    str  
        A data URL representing the image, suitable for embedding in HTML or other web contexts.  
    """  
    # Get mime type  
    mime_type, _ = guess_type(image_path)  
  
    if mime_type is None:  
        mime_type = 'application/octet-stream'  
  
    with open(image_path, "rb") as image_file:  
        base64_encoded_data = base64.b64encode(  
            image_file.read()).decode('utf-8')  
  
    return f"data:{mime_type};base64,{base64_encoded_data}"  
  
def call_azure_openai(prompt, image_data_url, response_format, client=client, aoai_deployment_name=aoai_deployment_name):  
    """  
    Call the Azure OpenAI service to analyze an image.  
  
    Parameters:  
    -----------  
    prompt : str  
        The prompt to send to the model.  
    image_data_url : str  
        The data URL of the image.  
    response_format : BaseModel
        The pydantic BaseModel defining the expected structured output. If None, a regular completion call is made.  
    client : AzureOpenAI  
        The Azure OpenAI client instance.  
    aoai_deployment_name : str  
        The deployment name of the Azure OpenAI model.  

    Returns:  
    --------  
    str or dict  
        The response from the Azure OpenAI model. If structured output is requested, a dictionary is returned.  
    """  

    completion = client.beta.chat.completions.parse(  
        model=aoai_deployment_name,  
        messages=[{  
            "role": "system",  
            "content": "You are an AI helpful assistant that extracts information from documents."  
        }, {  
            "role": "user",  
            "content": [{  
                "type": "text",  
                "text": prompt  
            }, {  
                "type": "image_url",  
                "image_url": {  
                    "url": image_data_url  
                }  
            }]  
        }],  
        max_tokens=2000,  
        temperature=0.7,  
        response_format=response_format  
    )  

    response = json.loads(completion.model_dump_json(indent=2))

    extracted_information = response['choices'][0]['message']['parsed']  

    return extracted_information  
  
def main():  
    # Define input and output directories  
    input_dir = Path('input_documents')  
    output_dir = Path('output_results')  
    output_dir.mkdir(exist_ok=True)  
  
    # Prompt to extract specific information  
    prompt = """Based on this image, answer the questions:   
                1) What is the name of the business?   
                2) What is the address of the business?
                3) What is the date of the transaction?  
                4) What is the total charge in the receipt? Include currency  
    """  
  
    # Define the structured output format using pydantic  
    class ExtractedAnswers(BaseModel):  
        businessName: str  
        businessAddress: str
        transactionDate: str  
        totalCharge: str  
  
    # Iterate over each image in the input directory  
    for image_file in input_dir.iterdir():  
        if image_file.is_file() and image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.gif', '.tiff']:  
            print(f"Processing {image_file.name}...")  
  
            # Convert image to data URL  
            image_data_url = image_to_data_url(image_file)  
  
            try:  
                # Call Azure OpenAI to extract structured information  
                extracted_info = call_azure_openai(prompt, image_data_url, response_format=ExtractedAnswers)  
  
                # Define output file path  
                output_file = output_dir / f"{image_file.stem}.json"  
  
                # Save the result as a JSON file  
                with open(output_file, 'w', encoding='utf-8') as json_file:  
                    json.dump(extracted_info, json_file, ensure_ascii=False, indent=2)  
  
                print(f"Saved extracted information to {output_file.name}")  
  
            except Exception as e:  
                print(f"Error processing {image_file.name}: {e}")  
  
if __name__ == "__main__":  
    main()  