from common.base import DictBean


class ObjectBean(DictBean):
    def __init__(self):
        super().__init__()
        self.trade_order_bean = None
