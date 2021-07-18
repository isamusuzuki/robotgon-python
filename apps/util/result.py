from typing import Any


class Result():
    """
    スクリプトの戻り値を共通化する
    """

    def __init__(
            self, name: str,
            success: bool = False,
            message: str = '',
            data: Any = None) -> None:
        self.name = name
        self.success = success
        self.message = message
        self.data = data

    def print(self):
        if self.success:
            if len(self.message) > 0:
                return f'[{self.name}] SUCCESS: {self.message}'
            else:
                return f'[{self.name}] SUCCESS'
        else:
            return f'[{self.name}] FAIL: {self.message}'
