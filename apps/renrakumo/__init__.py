import json
import os
from logging import DEBUG, Logger

from apps.renrakumo.twilio_handler import TwilioHandler
from apps.util.logger_a import getLoggerA
from apps.util.result import Result

import pandas as pd


class Renrakumo():
    """
    連絡網アプリ
    """

    def __init__(self, logger: Logger = None) -> None:
        """
        連絡網アプリをインスタンス化する

        Parameters
        ----------
        logger: Logger
            ロガー
        """

        if logger:
            self.logger = logger
        else:
            self.logger = getLoggerA(
                name=__name__,
                level=DEBUG,
                type='file',
                prefix='renrakumo',
                cycle='monthly'
            )

    def send(self, genko: str, meibo: str) -> Result:
        """
        連絡網に一斉送信する

        Parameters
        ----------
        genko: str
            原稿txtのファイル名
        meibo: str
            名簿csvのファイル名

        Returns
        -------
        Result.data: None
        """
        self.logger.debug('start')
        result = Result(__name__)

        # 1. 原稿を読む
        text_file = f'private-data/genko/{genko}.txt'
        if not os.path.exists(text_file):
            error_message = f'{text_file}が見つかりません'
            self.logger.critical(error_message)
            result.message = error_message
            return result
        else:
            with open(text_file, mode='r', encoding='utf-8') as f:
                body = f.read().replace('\n', ' ')
            self.logger.debug(f'read <= {text_file}')

            # 2. 名簿を読む
            csv_file = f'private-data/meibo/{meibo}.csv'
            if not os.path.exists(csv_file):
                error_message = f'{csv_file}が見つかりません'
                self.logger.critical(error_message)
                result.message = error_message
                return result
            else:
                df1 = pd.read_csv(
                    csv_file, encoding='utf-8', dtype=object).fillna('')
                phone_list = df1['phone'].values.tolist()
                self.logger.debug(f'read <= {csv_file}')

                # 3. SMSを送信する
                handler = TwilioHandler()
                result1 = handler.send_sms(
                    body=body,
                    phone_list=phone_list,
                    logger=self.logger
                )
                self.logger.debug(result1.print())

                if not result1.success:
                    result.message = result1.message
                else:
                    json_data = json.dumps(
                        result1.data, ensure_ascii=False, indent=2)
                    self.logger.debug(f'result1.data => \n{json_data}')
                    result.success = True
                return result
