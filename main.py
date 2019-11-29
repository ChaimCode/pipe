from asynmsg.msgengine import MessageEngine
from callback import PipeCallback
from constants import TRADE_ORDER_HANDLER_FOR_CREATE_ORDER
from handler import TradeOrderHandlerForCreateOrder
from pipeline import Pipe

if __name__ == '__main__':
    pipe_callback = PipeCallback()
    MessageEngine.instance().register(TRADE_ORDER_HANDLER_FOR_CREATE_ORDER, TradeOrderHandlerForCreateOrder(pipe_callback))
    MessageEngine.instance().send(TRADE_ORDER_HANDLER_FOR_CREATE_ORDER, amount=101)
    result = pipe_callback.get_result(10)
    print(result)
    # # 串行执行
    # # 1. 创建订单
    # # 2. 预支付
    pipe = Pipe()
    pipe.add_jobs([
        ''
    ])