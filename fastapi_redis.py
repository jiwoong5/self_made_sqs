# web_server.py
import uuid
import redis
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
r = redis.Redis(host="localhost", port=6379, db=0)

class TaskRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(request: TaskRequest):
    task_id = str(uuid.uuid4())
    task_data = {
        "task_id": task_id,
        "prompt": request.prompt
    }

    # 작업 큐에 등록
    r.lpush("task_queue", str(task_data))

    # 응답용 placeholder 설정 (선택사항)
    r.set(f"result:{task_id}", "PENDING", ex=300)

    # 비동기 응답
    return {"task_id": task_id, "status": "submitted"}
