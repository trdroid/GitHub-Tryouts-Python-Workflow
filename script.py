import json

user_data = {
    "id": 1234,
    "name": "James Gosling",
    "email": "james_gosling@oracle.com",    
}

json_output = json.dumps(user_data, indent=4)

print(json_output)