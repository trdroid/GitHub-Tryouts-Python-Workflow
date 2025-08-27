import json
import requests
import argparse
import rich_argparse

user_data = {
    "id": 1234,
    "name": "James Gosling",
    "email": "james_gosling@oracle.com",    
}

user_data["requests"] = f"{requests}"
user_data["rich_argparse"] = f"{rich_argparse}"

argument_parser = argparse.ArgumentParser()

argument_parser.add_argument("--client-id", help="The ClientID", required=True)
argument_parser.add_argument("--client-secret", help="The Client Secret", required=True)

args = argument_parser.parse_args()

user_data["client_id"] = args.client_id
user_data["client_secret"] = args.client_secret

json_output = json.dumps(user_data, indent=4)

print(json_output)