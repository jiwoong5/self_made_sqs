from queue import Queue
from typing import Optional

class SimpleSQS:
    def __init__(self):
        self.queue = Queue()

    def send_message(self, message: dict):
        self.queue.put(message)

    def receive_message(self) -> Optional[dict]:
        if not self.queue.empty():
            return self.queue.get()
        return None

    def delete_message(self, message: dict):
        # 실제 SQS는 ReceiptHandle로 삭제하지만 여기선 생략
        pass
