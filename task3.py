# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
# Certifique-se de que a região está correta para o seu lab (usualmente us-east-1)
bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# --- COLETA DE DADOS (Limpa e Validada) ---

# Validate pet type.
while True:
    pet_type = input("Enter your pet type (dog/cat): ").strip().lower()
    if pet_type in ["dog", "cat"]:
        break
    print("Invalid pet type. Please enter either 'dog' or 'cat'.")

# Collect other inputs.
ingredients = input("Enter your ingredients separated by commas: ")
allergies = input("Enter any allergies separated by commas (press Enter if none): ")

# --- CORREÇÃO PRINCIPAL: DEFINIÇÃO DO PROMPT ---
# Criamos a variável 'prompt' usando os dados coletados acima
prompt = f"Create a healthy recipe for a {pet_type} using the following ingredients: {ingredients}. strictly avoid these allergens: {allergies}."

# Set up request parameters.
max_tokens = 512
temperature = 0.7

# Task 3.3: Generate and display the recipe

# Create request with the Amazon Nova Lite model
request = {
    "messages": [
        {"role": "user", "content": [{"text": prompt}]}
    ],  # Agora 'prompt' existe
    "inferenceConfig": {
        # CORREÇÃO DO TODO: Adicionado o max_new_tokens
        "max_new_tokens": max_tokens,
        "temperature": temperature,
        "topP": 0.9,
    },
}

# Send the request to Bedrock and generate the recipe.
try:
    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
    )

    # Process and display the recipe.
    response_body = json.loads(response["body"].read())

    print(
        f"\nRecipe generated with {max_tokens} max tokens and a temperature of {temperature}.\n"
    )

    # Extrai o texto da resposta (estrutura específica do Nova)
    output_text = response_body["output"]["message"]["content"][0]["text"]

    if output_text.startswith(" - The generated text has been blocked"):
        print(
            "I apologize, but I cannot provide specific pet food recipes. For your pet's safety, please consult with a veterinarian."
        )
    else:
        print(output_text)

except Exception as e:
    print(f"An error occurred: {e}")
