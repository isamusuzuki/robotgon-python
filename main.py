from logging import DEBUG

from apps.browser_auto.firstscript import firstscript
from apps.renrakumo import Renrakumo
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class Main():
    def browserauto(self) -> None:
        """
        ブラウザを自動実行する
        """
        logger = getLoggerA(
            __name__, DEBUG, 'both', 'browserauto', 'daily')
        firstscript(logger=logger)

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
            __name__, DEBUG, 'both', 'renrakumo', 'monthly')
        r = Renrakumo(logger=logger)
        try:
            result = r.send(genko=genko, meibo=meibo)
            logger.info(result.print())
        except Exception as err:
            logger.exception(err)


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
