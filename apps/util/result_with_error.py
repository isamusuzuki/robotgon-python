from typing import Any


class ResultWithError():
    """
    スクリプトの戻り値を共通化する
    """

    def __init__(self, name: str) -> None:
        """
        ResultWithErrorクラスをインスタンス化する

        Parameters
        ----------
        name: str
            名前
        """
        self.name: str = name
        self.success: bool = False
        self.has_error: bool = True
        self.message: str = ''
        self.data: Any = None

    def print(self) -> str:
        """
        結果を出力する

        Returns
        -------
        result: str
        """
        if self.success:
            if len(self.message) > 0:
                return f'{self.name} => SUCCESS: {self.message}'
            else:
                return f'{self.name} => SUCCESS'
        else:
            if self.has_error:
                return f'{self.name} => FAIL: {self.message}'
            else:
                return f'{self.name} => NO_ERROR: {self.message}'
