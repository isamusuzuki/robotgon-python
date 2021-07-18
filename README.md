# robotgon-python

ロボットゴン Python

作成日 2021/07/18

## 01. ファイル・フォルダ構成

```text
--robotgon-python/
    |--apps/    ... 自作モジュールの置き場
    |--data/    ... データファイルの置き場
    |--logs/    ... ログファイルの置き場
    |--temp/    ... 一時ファイルの置き場
    |--tests/   ... テストスクリプトの置き場
    |--.env     ... 環境変数に組み込むキーバリュー
    `--main.py  ... 実行スクリプト
```

## 02. Python 環境の構築

```bash
cd ~/robotgon
python3 -m venv venv
source venv/bin/activate
pip install wheel
pip install -r requirements.txt -c constraints.txt
```

### .vscode/settings.json 設定例

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Path": "venv/bin/flake8",
  "python.linting.lintOnSave": true,
  "python.formatting.provider": "autopep8",
  "python.formatting.autopep8Path": "venv/bin/autopep8",
  "editor.formatOnSave": true,
  "terminal.integrated.env.linux": {
    "PYTHONPATH": "/home/{{YOURNAME}}/robotgon-python"
  }
}
```

## 03. 実行スクリプトの使い方

```bash
cd ~/robotgon-python
source venv/bin/activate

# 連絡網に一斉送信する
python main.py renrakumo --genko=210718 --meibo=test
```
