# AWS Bedrock Generative AI Suite

A collection of Python scripts utilizing the **Amazon Nova Lite** model via AWS Bedrock to demonstrate text generation capabilities.

## Modules
1. **Poem Generator**: Basic text generation with adjustable temperature.
2. **Pet Recipe Maker**: Context-aware generation with safety filters and input validation.
3. **Pet Profile Generator**: Batch processing with dynamic inference parameters based on metadata.

## Setup
1. Ensure AWS credentials are configured (or run within an IAM-authorized environment).
2. Install dependencies: `pip install -r requirements.txt`
3. Run modules from src: `python src/recipe_maker.py`