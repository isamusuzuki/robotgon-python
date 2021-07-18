import math
import os
from logging import Logger
from typing import List

from apps.util.result import Result

from twilio.rest import Client


class TwilioHandler():
    """
    twilioを使ってSMSを一斉送信する
    """

    def __init__(self) -> None:
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self.client = Client(account_sid, auth_token)
        self.from_number = '+12067371120'
        self.unit_length = 67
        self.unit_price_dollar = 0.08
        self.dollar_yen_rate = 110.0

    def calc_price(self, length: str) -> str:
        """
        文字数から1通あたりの送信料金を計算する
        """
        unit_count = math.ceil(length / self.unit_length)
        price_yen = math.ceil(
            unit_count * self.unit_price_dollar * self.dollar_yen_rate
        )
        return price_yen

    def format_e164(self, phone: str) -> str:
        """
        電話番号をE164形式に整える
        """
        p = phone.replace('-', '')
        return f'+81{p[1:]}'

    def send_sms(
            self, body: str,
            phone_list: List[str], logger: Logger) -> Result:
        """
        SMSを一斉送信する
        """
        logger.debug('start send_sms')
        result = Result(__name__)
        length = len(body)
        unit_price = self.calc_price(length)
        send_count = len(phone_list)
        result.data = {
            'body': body,
            'length': length,
            'unit_price': unit_price,
            'send_count': send_count,
            'total_price': send_count * unit_price,
            'responses': []
        }
        logger.debug('start loop')
        try:
            for phone in phone_list:
                response = self.client.messages.create(
                    body=body,
                    from_=self.from_number,
                    to=self.format_e164(phone)
                )
                result.data['responses'].append({
                    'date_sent': response.date_sent,
                    'sid': response.sid,
                    'status': response.status,
                    'to': response.to,
                })
            logger.debug('end loop')
            result.success = True
        except Exception as err:
            result.message = f'error => {err}'
        finally:
            logger.debug('end send_sms')
            return result
