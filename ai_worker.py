# ai_worker.py
import ast
import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

def process(prompt):
    # 예시 AI 처리 (실제로는 Stable Diffusion 등 연결)
    time.sleep(3)
    return f"Generated result for: {prompt}"

print("Worker started...")

while True:
    task = r.brpop("task_queue", timeout=5)  # block until task or timeout

    if task:
        _, task_str = task
        task_data = ast.literal_eval(task_str.decode())
        task_id = task_data["task_id"]
        prompt = task_data["prompt"]

        print(f"Processing task {task_id}...")

        result = process(prompt)

        # 결과 저장
        r.set(f"result:{task_id}", result, ex=600)
