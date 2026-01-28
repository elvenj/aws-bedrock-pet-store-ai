import boto3
import json

def generate_pet_descriptions():
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

    pets = [
        {"name": "Buddy", "type": "dog", "age": 3, "description": ""},
        {"name": "Mittens", "type": "cat", "age": 5, "description": ""},
        {"name": "Lucky", "type": "dog", "age": 6, "description": ""},
    ]

    print("Generating profiles...")

    for pet in pets:
        # Dynamic Logic: Cats get higher temperature (creativity)
        temperature = 0.9 if pet["type"] == "cat" else 0.3
        
        prompt = f"Write a fun, engaging description for a {pet['age']}-year-old {pet['type']} named {pet['name']}."

        request_payload = {
            "messages": [{"role": "user", "content": [{"text": prompt}]}],
            "inferenceConfig": {"maxTokens": 512, "temperature": temperature},
        }

        try:
            response = bedrock.invoke_model(
                modelId="amazon.nova-lite-v1:0", 
                body=json.dumps(request_payload)
            )
            response_body = json.loads(response["body"].read())
            pet["description"] = response_body["output"]["message"]["content"][0]["text"]
            
            print(f"\n{pet['name']} ({pet['type']}, {pet['age']}y): {pet['description']}")
            print("-" * 50)

        except Exception as e:
            print(f"Failed to generate for {pet['name']}: {e}")

if __name__ == "__main__":
    generate_pet_descriptions()