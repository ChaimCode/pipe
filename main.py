from asynmsg.msgengine import MessageEngine
from bean import ObjectBean
from callback import TradeOrderHandlerForCreateOrder
from constants import TRADE_ORDER_HANDLER_FOR_CREATE_ORDER

if __name__ == '__main__':
    object_bean = ObjectBean()
    MessageEngine.instance().register(TRADE_ORDER_HANDLER_FOR_CREATE_ORDER, TradeOrderHandlerForCreateOrder())
    MessageEngine.instance().send(TRADE_ORDER_HANDLER_FOR_CREATE_ORDER, delay=0, amount=101)
    if object_bean.trade_order_bean:
        MessageEngine.instance().shutdown()
