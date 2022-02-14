from logging import INFO

from apps.pdftool import PdfTool
from apps.pdftool.read_json import read_json
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

    def pdftool(self) -> None:
        """
        PdfToolアプリを実行する

        ※ 細かい指示は、pdftool.jsonファイルに書く
        """
        logger = getLoggerA(__name__, INFO, 'console')
        result = read_json()
        if not result.success:
            logger.critical(result.print())
        else:
            logger.info(result.print())

            # PdfToolをインスタンス化する
            pdftool = PdfTool(logger=logger)

            if result.data['command'] == 'merge':
                pdftool.merge(
                    input_files=result.data['input_files'],
                    output_file=result.data['output_file']
                )
            elif result.data['command'] == 'split':
                pdftool.split(
                    input_file=result.data['input_file'],
                    output_folder=result.data['output_folder']
                )
            elif result.data['command'] == 'rotate':
                pdftool.rotate(
                    input_file=result.data['input_file'],
                    output_file=result.data['output_file'],
                    pages=result.data['pages'],
                    clockwise=result.data['clockwise']
                )


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
