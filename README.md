# AWS Bedrock Pet Store AI Solutions 🐶🐱

This project contains AI-powered applications developed for the **AnyCompany Pets Store** scenario to enhance customer experience and improve pet adoption rates.

Built using **Amazon Bedrock**, the **Amazon Nova Lite** model, and the **AWS SDK for Python (Boto3)**.

## Applications

### 1. Smart Recipe Generator (`src/recipe_maker.py`)
Helps pet owners create safe and healthy treats using available ingredients.
- **Features:** Validates pet type, accepts ingredient lists, and filters out known allergens.
- **Tech:** Context-aware prompting with safety guardrails.

### 2. Adoption Profile Enhancer (`src/pet_profiles.py`)
Generates engaging and personality-rich descriptions for shelter animals to attract potential adopters.
- **Features:** Batch processing of pet data.
- **Dynamic Logic:** Adjusts "temperature" (creativity) based on pet type (e.g., higher creativity for cats, lower for dogs).

### 3. Creative Writing (`src/poem_generator.py`)
A foundational module demonstrating basic text generation capabilities with Amazon Nova Lite.

## Technology Stack
- **Cloud Service:** AWS Bedrock
- **Model:** Amazon Nova Lite (`amazon.nova-lite-v1:0`)
- **Language:** Python 3
- **SDK:** Boto3

## Project Structure
```text
aws-bedrock-pet-store-ai/
├── .gitignore             # Security configuration
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── src/                   # Application source code
    ├── recipe_maker.py
    ├── pet_profiles.py
    └── poem_generator.py