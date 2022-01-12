from logging import Logger

from playwright.sync_api import sync_playwright


def apple(logger: Logger) -> None:
    """
    Playwrightでブラウザを動かす

    Parameter
    ---------
    logger: Logger
        ロガー
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto('http://whatsmyuseragent.org/')
        png_file = 'temp/whatsmyuseragent.png'
        page.screenshot(path=png_file)
        logger.info(f'done => {png_file}')
        browser.close()
