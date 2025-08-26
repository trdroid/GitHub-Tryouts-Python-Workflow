import json
import requests
import rich_argparse

user_data = {
    "id": 1234,
    "name": "James Gosling",
    "email": "james_gosling@oracle.com",    
}

user_data["requests"] = f"{requests}"
user_data["rich_argparse"] = f"{rich_argparse}"

json_output = json.dumps(user_data, indent=4)

print(json_output)