import json
import requests
import rich_argparse

user_data = {
    "id": 1234,
    "name": "James Gosling",
    "email": "james_gosling@oracle.com",    
}

json_output = json.dumps(user_data, indent=4)

print(f"requests: {requests}")
print(f"rich_argparse: {rich_argparse}")

print(json_output)