import time
from threading import RLock

from asynmsg.handlers import AsynMsgCallBack
from asynmsg.msgengine import MessageEngine


class PipeCallback(AsynMsgCallBack):
    def __init__(self):
        self.lock = RLock()
        self.finish_sum = 0
        self.result = None

    def _execute(self, exec_result=None, **kwargs):
        with self.lock:
            print(self.finish_sum)
            self.finish_sum += 1
            self.result = exec_result
        return exec_result

    def get_result(self, timeout=60):
        start_time = time.time()
        while True:
            current_time = time.time()

            if current_time - start_time > timeout:
                return self.result

            if self.finish_sum > 0:
                MessageEngine.instance().shutdown()
                return self.result
