import json
import shutil
from logging import INFO
from os import mkdir, path
from time import sleep

from apps.browser_auto.bacon import bacon
from apps.browser_auto.cacao import cacao
from apps.util.logger_a import getLoggerA

from dotenv import load_dotenv

from fire import Fire


class ItemImages():
    def job1(self, suffix: str) -> None:
        """
        楽天市場の商品ページから商品画像のURLを取得する

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

    def job2(self, suffix: str) -> None:
        """
        Yahoo!ショッピングの商品ページからiFrame内のHTMLを抜き出す
        """
        # ターゲットフォルダを空にする
        target_folder = f'temp/html{suffix}'
        if path.exists(target_folder):
            shutil.rmtree(target_folder)
        mkdir(target_folder)

        json_file = f'temp/itemcodes{suffix}.json'
        with open(json_file, mode='r', encoding='utf-8') as f:
            item_code_list = json.loads(f.read())
        for item_code in item_code_list:
            cacao(
                item_code=item_code,
                target_folder=target_folder, logger=self.logger)
            # しばし待つ
            sleep(2)


if __name__ == '__main__':
    load_dotenv()
    Fire(ItemImages)
