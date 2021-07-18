# apps/renrakumo 概要

連絡網アプリ

作成日 2021/07/18

## 01. ファイル・フォルダ構成

```text
--apps/renrakumo/
    |--__init__.py        ... 連絡網アプリ本体
    `--twilio_handler.py  ... twilioを使ってSMSを一斉送信する
```

## 02. 単体テスト

```bash
cd ~/robotgon-python
source venv/bin/activate

python tests/test_twilio_handler.py
```
