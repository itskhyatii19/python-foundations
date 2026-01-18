import requests

res = requests.post(
    "http://127.0.0.1:5000/login",
    json={"username": "khyati", "password": "1234"}
)

print(res.json())
