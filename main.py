from logging import DEBUG

from apps.renrakumo import Renrakumo
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class Main():
    def renrakumo(self, genko: str, meibo: str) -> None:
        """
        連絡網アプリを実行する

        arameters
        ----------
        genko: str
            原稿txtのファイル名
        meibo: str
            名簿csvのファイル名
        """
        logger = getLoggerA(
            __name__, DEBUG, 'both', 'renrakumo', 'monthly')
        r = Renrakumo(logger=logger)
        result = r.send(genko=genko, meibo=meibo)
        logger.info(result.print())


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
