import requests

payload = {
    'task': 'generate_image',
    'user_id': 'abc123',
    'prompt': 'a cat flying in space'
}

response = requests.post('http://localhost:5000/enqueue', json=payload)
print("Client Response:", response.json())
