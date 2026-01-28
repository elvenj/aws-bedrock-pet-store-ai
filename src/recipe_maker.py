import boto3
import json

def get_valid_pet_type():
    while True:
        pet_type = input("Enter your pet type (dog/cat): ").strip().lower()
        if pet_type in ["dog", "cat"]:
            return pet_type
        print("Invalid input. Please enter 'dog' or 'cat'.")

def generate_recipe():
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    
    # Input Collection
    pet_type = get_valid_pet_type()
    ingredients = input("Enter ingredients (comma-separated): ")
    allergies = input("Enter allergies (comma-separated, press Enter if none): ")

    prompt = f"Create a healthy recipe for a {pet_type} using: {ingredients}. Strictly avoid: {allergies}."
    
    request_payload = {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {
            "max_new_tokens": 512,
            "temperature": 0.7,
            "topP": 0.9,
        },
    }

    try:
        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0", 
            body=json.dumps(request_payload)
        )
        response_body = json.loads(response["body"].read())
        output_text = response_body["output"]["message"]["content"][0]["text"]

        if "blocked" in output_text.lower():
            print("Content blocked for safety. Please consult a veterinarian.")
        else:
            print(f"\n--- Generated Recipe for {pet_type.capitalize()} ---\n{output_text}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    generate_recipe()