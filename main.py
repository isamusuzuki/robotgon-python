import json
from logging import DEBUG, INFO

from apps.browser_auto.apple import apple
from apps.browser_auto.bacon import bacon
from apps.renrakumo import Renrakumo
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class Main():
    def browserauto(self) -> None:
        """
        ブラウザを自動実行する
        """
        logger = getLoggerA(__name__, INFO, 'console')
        apple(logger=logger)


    def itemimages(self, suffix: str) -> None:
        """
        商品画像のURLをまとめて取得する

        あらかじめ temp/itemcodes{suffix}.jsonを用意しておくこと
        ["ahc3601", "oajon3"]

        Parameters
        ----------
        suffix: str
            ファイル名に使っている接尾辞
        """
        logger = getLoggerA(__name__, INFO, 'console')
        json_file = f'temp/itemcodes{suffix}.json'
        with open(json_file, mode='r', encoding='utf-8') as f:
            itemcodes = json.loads(f.read())
        result_dict = {}
        for item_code in itemcodes:
            logger.info(f'item_code = {item_code} ')
            result_dict[item_code] = bacon(item_code=item_code, logger=logger)
        json_file = f'temp/itemimages{suffix}.json'
        with open(json_file, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(result_dict, ensure_ascii=False, indent=2))
        logger.info(f'done => {json_file}')

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
