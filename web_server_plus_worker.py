from flask import Flask, request, jsonify
from threading import Thread
import time
from queue import Queue

app = Flask(__name__)
queue = Queue()

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.json
    queue.put(data)
    return jsonify({'status': 'queued'}), 200

def worker_loop():
    print("[Worker] Started")
    while True:
        if not queue.empty():
            msg = queue.get()
            print(f"[Worker] Processing task: {msg}", flush=True)
            time.sleep(2)
            print(f"[Worker] Done processing: {msg}", flush=True)
        else:
            time.sleep(1)

if __name__ == '__main__':
    # 워커 스레드 실행
    t = Thread(target=worker_loop, daemon=True)
    t.start()

    # 플라스크 웹서버 실행
    app.run(debug=True)
