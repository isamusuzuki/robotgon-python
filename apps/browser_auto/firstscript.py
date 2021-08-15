from logging import Logger

from playwright.sync_api import sync_playwright


def firstscript(logger: Logger) -> None:
    """
    Playwrightというブラウザを自動化するライブラリの最初のスクリプト

    Parameter
    ---------
    logger: Logger
        ロガー
    """

    logger.debug('start firstscript()')
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(
            # headless=False, # => ブラウザを表示する
            # slow_mo=50      # => ブラウザをゆっくり動かす
        )
        page.goto('http://whatsmyuseragent.org/')
        img_file = 'temp/firstscript.png'
        page.screenshot(path=img_file)
        logger.debug(f'done => {img_file}')
        browser.close()
