import requests
from datetime import datetime
import uuid

# 파이프라인 실행 단위 UUID 생성 (예시)
pipeline_id = str(uuid.uuid4())

# 현재 시간 ISO8601 포맷 (UTC)
timestamp = datetime.utcnow().isoformat() + "Z"

payload = {
    "pipeline_id": pipeline_id,
    "step_name": "ocr result",
    "payload": {
        "task": "generate_image",
        "user_id": "abc123",
        "prompt": "a cat flying in space"
    },
    "timestamp": timestamp
}

response = requests.post('http://localhost:5000/enqueue', json=payload)
print("Client Response:", response.json())
