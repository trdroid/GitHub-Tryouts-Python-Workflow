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
argument_parser.add_argument("--env-one", help="Environment value one", required=True)
argument_parser.add_argument("--env-two", help="Environment value two", required=True)
args = argument_parser.parse_args()

client_id = args.client_id
client_secret = args.client_secret

user_data["client_id"] = client_id
user_data["client_secret"] = client_secret

user_data["env_one"] = args.env_one
user_data["env_two"] = args.env_two

json_output = json.dumps(user_data, indent=4)

print(json_output)

print(f"client_id: {client_id}")
print(f"client_secret: {client_secret}")

print(f"client_id == 'client_id_value' is {client_id == 'client_id_value'}")
print(f"client_secret == 'client_secret_value' is {client_secret == 'client_secret_value'}")

print(f"client_id == 'non_prod_client_id_value' is {client_id == 'non_prod_client_id_value'}")
print(f"client_secret == 'non_prod_client_secret_value' is {client_secret == 'non_prod_client_secret_value'}")