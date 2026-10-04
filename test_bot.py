import requests

url = 'http://127.0.0.1:5000/ask'
payload = {
    "answer": "In C++, an array is a collection of items stored at contiguous memory locations."
}

print("🎙️ Sending answer to PrepPilot AI...\n")
try:
    response = requests.post(url, json=payload)
    data = response.json()
    print("🤖 AI Interviewer Response:")
    print(data)
except Exception as e:
    print("Error:", e)