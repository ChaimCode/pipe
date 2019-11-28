import requests

from asynmsg.handlers import AsynNotifyHandler
from checkargs.checkcmds import CheckNoNullCmd, CheckNumberCmd


class TradeOrderHandlerForCreateOrder(AsynNotifyHandler):

    def _execute(self, amount):
        params = dict(version="1.0",
                      user_code="1",
                      team="weike",
                      order_type=313,
                      order_amount=amount,
                      discount_amount=0,
                      pay_amount=amount,
                      offset_amount=0,
                      fee_amount=0,
                      trade_ip="127.0.0.1",
                      server="business_pay")
        url = 'http://127.0.0.1:8001/order/create_order'
        result = requests.get(url, params).json()
        return result

    def _init_check_item(self, **kwargs):
        self.add_check_item('amount', CheckNoNullCmd(), CheckNumberCmd())
