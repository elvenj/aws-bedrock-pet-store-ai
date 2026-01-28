# Import the required libraries for AWS service interaction and JSON processing.
import boto3
import json

# Connect to the Amazon Bedrock client.
bedrock = boto3.client(service_name="bedrock-runtime")


# Set up the prompt and temperature.
prompt = "Write a short poem about a curious cat"  # Use this example, or create one of your own!
temperature = 0.5  # TODO: when you run the code, try adjusting the temperature value between 0.0 and 1.0 to experiment with randomness.

# Structure a request dictionary for Amazon Bedrock Amazon Nova Lite model that includes inputText and temperature parameters
# Create the request dictionary for the Amazon Nova Lite model that includes text and temperature parameters.
request = {
    "messages": [{"role": "user", "content": [{"text": prompt}]}],
    "inferenceConfig": {"temperature": temperature},
}

# Make the API call to the Amazon Bedrock Amazon Nova Lite Model
# Use the Amazon Bedrock client to invoke the Amazon Nova Lite model and save the resulting output to a variable named response .
# Use the Amazon Bedrock client to invoke the Amazon Nova Lite model.
response = bedrock.invoke_model(
    modelId="amazon.nova-lite-v1:0", body=json.dumps(request)
)

# Get and print the response
# Get and print the response
response_body = json.loads(response["body"].read())
generated_text = response_body["output"]["message"]["content"][0]["text"]
print(f"\nText generated with the following prompt and temperature.")
print(f"Prompt: {prompt}")
print(f"Temperature: {temperature}:\n")
print(generated_text)
