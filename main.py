from logging import INFO

from apps.renrakumo import Renrakumo
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class Main():
    def renrakumo(self, genko: str, meibo: str) -> None:
        """
        連絡網アプリを実行する

        Parameters
        ----------
        genko: str
            原稿txtのファイル名
        meibo: str
            名簿csvのファイル名
        """
        logger = getLoggerA(
            __name__, INFO, 'both', 'renrakumo', 'monthly')
        r = Renrakumo(logger=logger)
        try:
            result = r.send(genko=genko, meibo=meibo)
            logger.info(result.print())
        except Exception as err:
            logger.exception(err)


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
