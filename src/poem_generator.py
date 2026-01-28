import boto3
import json


def generate_poem(
    prompt_text="Write a short poem about a curious cat", temperature=0.5
):
    """Generates a text response using Amazon Nova Lite."""
    bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

    request_payload = {
        "messages": [{"role": "user", "content": [{"text": prompt_text}]}],
        "inferenceConfig": {"temperature": temperature},
    }

    try:
        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0", body=json.dumps(request_payload)
        )
        response_body = json.loads(response["body"].read())
        return response_body["output"]["message"]["content"][0]["text"]
    except Exception as e:
        return f"Error generating poem: {str(e)}"


if __name__ == "__main__":
    print(generate_poem())
