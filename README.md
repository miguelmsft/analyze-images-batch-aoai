# Extracting Structured Information from Images using Azure OpenAI GPT-4o  
   
This repository contains a script that processes images, extracts specific information using Azure OpenAI GPT-4o, and saves the results in a structured JSON format. In includes Contoso examples to illustrate the AI functionality.  
   
## Table of Contents  
   
- [Overview](#overview)  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Setup](#setup)  
- [Usage](#usage)  
- [Directory Structure](#directory-structure)  
- [Script Explanation](#script-explanation)  
- [Example Output](#example-output)  
- [License](#license)  
   
## Overview  
   
The `analyze_images.py` script automates the process of extracting specific details from images (such as receipts) using the Azure OpenAI GPT-4o model. It reads each image in the `input_documents` folder, sends a request to the Azure OpenAI service to extract predefined pieces of information, and saves the extracted data as a JSON file in the `output_results` folder.  
   
## Features  
   
- **Automated Image Processing**: Processes multiple images in a batch from a specified input directory.  
- **Structured Data Extraction**: Extracts specific information and saves it in a structured JSON format.  
- **Customizable Prompt and Output**: Easily modify the prompt and the expected output fields.  
- **Azure OpenAI Integration**: Leverages the powerful GPT-4o model hosted on Azure for advanced image understanding.  
   
## Prerequisites  
   
- **Python 3.7 or higher**  
- Azure OpenAI Service access with the GPT-4o model deployed  
- Required Python packages:  
  - `openai`  
  - `pydantic`  
  - `python-dotenv`  
- An Azure account with proper permissions to use the OpenAI service  
- **Environment Variables**: Azure OpenAI credentials set in a `.env` file  
   
## Setup  
   
### 1. Clone the Repository  
   
```bash  
git clone https://github.com/yourusername/your-repo-name.git  
cd your-repo-name  
```  
   
### 2. Install Dependencies  
   

   
```bash  
pip install openai pydantic python-dotenv  
```  
   
### 3. Configure Environment Variables  
   
Create a `.env` file in the root directory and add your Azure OpenAI credentials:  
   
```env  
AOAI_ENDPOINT=your_azure_openai_endpoint  
AOAI_API_KEY=your_azure_openai_api_key  
AOAI_DEPLOYMENT=your_azure_openai_deployment_name  
```  
   
Replace the placeholders with your actual Azure OpenAI endpoint, API key, and deployment name.  
   
### 4. Prepare Input Images  
   
Place the images you want to process in the `input_documents` folder. Supported image formats include `.png`, `.jpg`, `.jpeg`, `.gif`, and `.tiff`.  
   
## Usage  
   
Run the script using the following command:  
   
```bash  
python analyze_images.py  
```  
   
The script will process each image in the `input_documents` folder, extract the specified information, and save the results as JSON files in the `output_results` folder.  
   
### Customizing the Script  
   
- **Modify the Prompt**: You can change the `prompt` variable in the script to extract different information from the images.  
- **Adjust the Output Format**: Update the `ExtractedAnswers` class to match the information you're extracting.  
   
## Directory Structure  
   
```  
├── LICENSE  
├── README.md  
├── analyze_images.py  
├── input_documents  
│   ├── sample1.png  
│   ├── sample2.jpg  
│   ├── sample3.png  
│   ├── sample4.png  
│   ├── sample5.png  
│   └── sample6.jpg  
├── output_results  
│   ├── sample1.json  
│   ├── sample2.json  
│   ├── sample3.json  
│   ├── sample4.json  
│   ├── sample5.json  
│   └── sample6.json  
```  
   
- **`analyze_images.py`**: The main script that processes images and extracts information.  
- **`input_documents/`**: Directory containing input image files.  
- **`output_results/`**: Directory where output JSON files are saved.  
- **`LICENSE`**: License file for the project.  
- **`README.md`**: This README file.  
   

## Example Output  
   
When you run the script, it will process each image and display output similar to:  
   
```bash  
Processing sample1.png...  
Saved extracted information to sample1.json  
Processing sample2.jpg...  
Saved extracted information to sample2.json  
Processing sample3.png...  
Saved extracted information to sample3.json  
Processing sample4.png...  
Saved extracted information to sample4.json  
Processing sample5.png...  
Saved extracted information to sample5.json  
Processing sample6.jpg...  
Saved extracted information to sample6.json  
```  
   
Each JSON file in the `output_results` directory will contain the extracted information in the following format:  
   
```json  
{  
  "businessName": "Example Store",  
  "businessAddress": "123 Main Street, City, Country",  
  "transactionDate": "2023-10-15",  
  "totalCharge": "$45.67"  
}  
```  
   
## License  
   
This project is licensed under the [MIT License](LICENSE).  
   