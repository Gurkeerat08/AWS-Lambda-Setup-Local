import boto3

try: 
    # Set up your AWS credentials
    session = boto3.Session(
        aws_access_key_id='YOUR_KEY',
        aws_secret_access_key='YOUR_KEY',
        aws_session_token='YOUR_KEY'
    )

    # Create a Lambda client
    lambda_client = session.client('lambda',region_name='us-east-2')

    # Specify the Lambda Name
    # For example , FunctionName='aads-marketplace-get-data-request-history-dev'
    response = lambda_client.get_function_configuration(FunctionName='aads-marketplace-get-data-request-history-dev')

    # Extract environment variables
    env_variables = response['Environment']['Variables']
    print(env_variables)
except Exception as e:
    # Code that runs if an exception occurs
    print(f"An error occurred: {e}")