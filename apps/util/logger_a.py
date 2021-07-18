import os
from datetime import datetime
from logging import \
    FileHandler, Formatter, Logger, StreamHandler, getLogger

import pytz


def getLoggerA(
        name: str, level: int,
        type: str = 'console', prefix: str = 'main',
        cycle: str = 'monthly') -> Logger:
    """
    logging.getLogger()を拡張する
    """
    logger = getLogger(name)
    logger.setLevel(level)
    if not logger.hasHandlers():
        # Formatterは共通
        fmt = Formatter(
            '%(asctime)0.19s - %(module)s [%(levelname)s] %(message)s'
        )
        # FileHandlerを準備して組み込む
        if type == 'both' or type == 'file':
            now = datetime.now(pytz.timezone('Asia/Tokyo'))
            day_str = now.strftime('%Y%m%d')
            month_str = now.strftime('%Y%m')
            month_folder = f'logs/{month_str}'
            if not os.path.exists(month_folder):
                os.mkdir(month_folder)
            if cycle == 'daily':
                log_file = f'{month_folder}/{prefix}_{day_str}.log'
            else:
                log_file = f'{month_folder}/{prefix}_{month_str}.log'
            fh = FileHandler(log_file)
            fh.setLevel(level)
            fh.setFormatter(fmt)
            logger.addHandler(fh)

        # StreamHandlerの準備して組み込む
        if type == 'both' or type == 'console':
            sh = StreamHandler()
            sh.setFormatter(fmt)
            logger.addHandler(sh)
    return logger
