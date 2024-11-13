# Metadata Manager Lambda Local Setup

This guide provides steps to run AWS Lambda functions locally for the Metadata Manager project.

## Prerequisites

1. **AWS CLI Setup**
   - Follow the steps documented in the Confluence link: [AWS CLI Setup - Enterprise Data - Enterprise Confluence](https://lilly-confluence.atlassian.net/wiki/spaces/EDB/pages/904006250/AWS+CLI+Setup)
   - Create your local AWS CLI profile and generate your keys.

2. **Fetch Env variables using this script**
   - Replace the placeholder keys with actual keys in [the provided Python script](https://github.com/Gurkeerat08/AWS-Lambda-Setup-Local/blob/main/environment_variables.py).
   - Add the Lambda name and execute the script to obtain the environment variables for your Lambda.

3. **Setup `python-lambda-local`**
   - Do a `pip install python-lambda-local` to 
   - Create an `event.json` file to mock API calls inside the lambda folder inside functions.

## Steps

1. **Create `event.json` File**
   - Create an `event.json` file with the required payload.

2. **Replace Environment Variables**
   - Replace all environment variables in your lambda with the values obtained from [the provided Python script](https://github.com/Gurkeerat08/AWS-Lambda-Setup-Local/blob/main/environment_variables.py).
   - Before pushing the code, make sure to revert back to the `os.environment` approach.

3. **Run Lambda Locally**
   - cd inside your Lambda folder
   - Use the following command to trigger your Lambda:
     ```bash
     python-lambda-local -f lambda_handler aads_marketplace_get_ddw_data_request_history.py event.json
     ```

By using this command, you can run the Lambda directly on your local machine and test it with various scenarios by manipulating the `event.json` file.

## Notes

### Possible Error Scenarios

- **Password Input for AWS CLI Configuration**
  - Always use a right-click to paste the password.

- **Region Specification for Boto Resources**
  - For resources like S3, specify the region manually:
    ```python
    s3_client = boto3.client("s3", region_name='us-east-2')
    ```
  - Resolve `NoRegionError` by providing the region name.

### Example `event.json`

```json
{
  "requestContext": {
    "authorizer": {
      "uid": "example-user-id"
    }
  },
  "headers": {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
  },
  "queryStringParameters": {
    "ID": "ac4b07aca865f1db6b867dd1ce6a35"
  },
  "body": "{\"key1\":\"value1\",\"key2\":\"value2\"}"
}
```

### Troubleshooting

- **Invalid Security Token Error**
  - Check if your AWS CLI login session has expired:

    Assuming metadata-local-dev is the name of your local AWS CLI Profile : 

    ```bash
    aws sts get-caller-identity --profile metadata-local-dev
    ```
  - If expired, log in again:
    ```bash
    lilly-aws-auth login metadata-local-dev
    ```

- **Default AWS Session Issue**
  - Set your profile as the default:
    ```bash
    setx AWS_PROFILE "your_profile_name"
    ```
  - If this doesn't work, copy your keys from your actual profile to the default profile in `C/users/user-id/.aws/credentials`.
  - The session is created for an hour hence the keys are only valid for 1 hour