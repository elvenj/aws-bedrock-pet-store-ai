# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to Amazon Bedrock.
bedrock = boto3.client("bedrock-runtime")

# Define a list of pet dictionaries.
pets = [
    {"name": "Buddy", "type": "dog", "age": 3, "description": ""},
    {"name": "Mittens", "type": "cat", "age": 5, "description": ""},
    {"name": "Lucky", "type": "dog", "age": 6, "description": ""},
]

# Task 4: Create a pet description generator
# Loop through each pet dictionary and update its description.
for pet in pets:
    # Adjust the temperature dynamically based on the pet's type
    if pet["type"] == "cat":
        temperature = 0.9
    else:
        temperature = 0.3

    max_tokens = (
        512  # Consider adjusting this value to control the length of the response.
    )

    # Define the prompt for generating the description.
    prompt = f"Write a fun and engaging description for a {pet['age']}-year-old {pet['type']} named {pet['name']}."

# Loop through each pet dictionary and update its description.
for pet in pets:
    # Adjust the temperature dynamically based on the pet's type
    if pet["type"] == "cat":
        temperature = 0.9
    else:
        temperature = 0.3

    max_tokens = (
        512  # Consider adjusting this value to control the length of the response.
    )

    # Define the prompt for generating the description.
    prompt = f"Write a fun and engaging description for a {pet['age']}-year-old {pet['type']} named {pet['name']}."

    # Create the request payload.
    request = {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"maxTokens": max_tokens, "temperature": temperature},
    }

    # Send the request to the Amazon Bedrock model.
    response = bedrock.invoke_model(
        modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
    )

    # Parse the response and update the pet's description.
    response_body = json.loads(response["body"].read())
    pet["description"] = response_body["output"]["message"]["content"][0]["text"]


# Print the updated list of pets with descriptions.
for pet in pets:
    print(f"{pet['name']} ({pet['type']}, {pet['age']} years): {pet['description']}\n")
    print("-" * 50)  # Separator line between pets
