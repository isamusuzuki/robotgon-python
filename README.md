# robotgon-python 概要

ロボットゴン Python スクリプト集

作成日 2021/07/18、更新日 2022/02/14

## 01. ファイル・フォルダ構成

```text
--robotgon-python/
  |--apps/          ... 自作モジュールの置き場
  |--jupyter-dojo/  ... Jupyter 道場
  |--logs/          ... ログファイルの置き場（※1）
  |--private-data/  ... 個人情報の置き場（※1）
  |--temp/          ... 一時ファイルの置き場（※1）
  |--tests/         ... テストスクリプトの置き場
  |--.env           ... 環境変数に組み込むキーバリュー（※1）
  `--main.py        ... 実行スクリプト

※1 ... リポジトリから除外
```

## 02. Python 環境の構築

- OS は WSL2 上の Ubuntu を想定
- エディタは Visual Studio Code を想定

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
python main.py renrakumo --genko=220311h --meibo=hancho
python main.py renrakumo --genko=220311n --meibo=newbie
python main.py renrakumo --genko=220311y --meibo=yakuin

# PDFファイルを加工する
# ※ 細かい指示は、temp/pdftool.jsonファイルに書く
python main.py pdftool
```

## 04. temp/pdftool.json ファイルの書き方

PDF を結合する

```json
{
  "command": "merge",
  "input_files": ["temp/pdf/01.pdf", "temp/pdf/02.pdf"],
  "output_file": "temp/merged.pdf"
}
```

PDF を分割する

```json
{
  "command": "split",
  "input_file": "temp/pdf/original.pdf"
}
```

PDF のページを回転させる

```json
{
  "command": "rotate",
  "input_file": "temp/pdf/original.pdf",
  "output_file": "temp/rotated.pdf",
  "pages": [4, 5],
  "clockwise": false
}
```
