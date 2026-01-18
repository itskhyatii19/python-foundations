import requests

token = "PASTE_ACCESS_TOKEN"

res = requests.post(
    "http://127.0.0.1:5000/logout",
    headers={
        "Authorization": f"Bearer {token}"
    }
)

print("Status:", res.status_code)
print("Response:", res.text)
