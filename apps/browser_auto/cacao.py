from logging import Logger

from playwright.sync_api import sync_playwright


def cacao(item_code: str, target_folder: str, logger: Logger) -> None:
    """
    Yahoo!ショッピングの商品ページからiFrame内のHTMLを抜き出す

    Parameter
    ---------
    item_code: str
        商品コード
    target_folder: str
        HTMLファイルを保存する先
    logger: Logger
        ロガー
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = (
            'https://paypaymall.yahoo.co.jp/'
            f'store/backyard/item/{item_code}/'
        )
        page.goto(url, wait_until='domcontentloaded')
        logger.info(f'{item_code}: frame count => {len(page.frames)}')
        i = 1
        for frm in page.frames:
            if i < 5:
                html_file = f'{target_folder}/{item_code}_{i:02}.html'
                with open(html_file, mode='w', encoding='utf-8') as f:
                    f.write(frm.content())
                logger.info(f'done => {html_file}')
            else:
                logger.info(f'skip => {i}')
            i += 1
        browser.close()
