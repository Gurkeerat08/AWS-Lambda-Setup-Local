import boto3
import json

try: 
    # Set up your AWS credentials
    session = boto3.Session(
        aws_access_key_id = "actual-value-here",
        aws_secret_access_key = "actual-value-here",
        aws_session_token = "actual-value-here"
    )

    # Create a Lambda client
    lambda_client = session.client('lambda',region_name='us-east-2')
    lambda_name = 'lambda-name-here'
    # Get the function configuration
    response = lambda_client.get_function_configuration(FunctionName=lambda_name)

    # Extract environment variables
    env_variables = response['Environment']['Variables']
    # Convert the dictionary to a JSON string
    json_data = json.dumps(env_variables, indent=4)

    # Write the JSON string to a file
    with open(lambda_name+'env_variables.json', 'w') as json_file:
        json_file.write(json_data)

    print("JSON file created successfully for the lambda : "+lambda_name)
except Exception as e:
    # Code that runs if an exception occurs
    print(f"An error occurred: {e}")
