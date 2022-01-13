from logging import Logger
from typing import List

from playwright.sync_api import sync_playwright


def bacon(item_code: str, logger: Logger) -> List[str]:
    """
    楽天市場の商品ページから商品画像のURLを取得する

    Parameter
    ---------
    item_code: str
        商品コード
    logger: Logger
        ロガー

    Returns
    -------
    item_images: List[str]
        商品画像のURL群
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        url = f'https://item.rakuten.co.jp/backyard/{item_code}/'
        page.goto(url, wait_until='domcontentloaded')
        images = page.query_selector_all(
            'xpath=//div[@class="shohin-detail"]/img')
        logger.info(f'{item_code} count => {len(images)}')
        item_images = []
        if len(images) > 0:
            for image in images:
                src = page.evaluate('(x) => x.getAttribute("src")', image)
                logger.info(f'{item_code} src => {src}')
                item_images.append(src)
        browser.close()
        return item_images
