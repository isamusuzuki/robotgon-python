import json
from logging import INFO
from os import path

from apps.pdftool import PdfTool
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
        json_file = 'temp/pdftool.json'
        if not path.exists(json_file):
            logger.critical(f'{json_file}がありません')
        else:
            # order.json を読む
            with open(json_file, mode='r', encoding='utf-8') as f:
                order_dict = json.loads(f.read())
            if 'command' not in order_dict:
                logger.critical(f'{json_file}にcommandキーがありません')
            else:
                command = order_dict['command']
                # PdfToolをインスタンス化する
                pdftool = PdfTool(logger=logger)
                if command == 'merge':
                    if 'input_files' not in order_dict:
                        logger.critical(f'{json_file}にinput_filesキーがありません')
                    elif 'output_file' not in order_dict:
                        logger.critical(f'{json_file}にoutput_fileキーがありません')
                    else:
                        pdftool.merge(
                            input_files=order_dict['input_files'],
                            output_file=order_dict['output_file']
                        )
                elif command == 'split':
                    if 'input_file' not in order_dict:
                        logger.critical(f'{json_file}にinput_fileキーがありません')
                    elif 'output_folder' not in order_dict:
                        logger.critical(f'{json_file}にoutput_folderキーがありません')
                    else:
                        pdftool.split(
                            input_file=order_dict['input_file'],
                            output_folder=order_dict['output_folder']
                        )
                else:
                    logger.critical(f'{command}は想定外のコマンドです')


if __name__ == '__main__':
    load_dotenv()
    Fire(Main)
