import requests

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyCPOZkakp1a8jcE8NTGTeopuHnP2emno4o"

headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [{"text": "hi"}]
        }
    ]
}

response = requests.post(url, json=data, headers=headers)

print(response.json())
