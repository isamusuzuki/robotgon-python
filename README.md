# robotgon-python

ロボットゴン Python スクリプト集

作成日 2021/07/18、更新日 2022/01/12

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

- OS は Ubuntu を想定
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

### Playwright 用ブラウザのインストール

```bash
cd ~/robotgon-python
source venv/bin/activate

pip install playwright

playwright --version
# => Version 1.17.1

# Chromiumをインストールする
playwright install chromium
# => Playwright build of chromium v939194 downloaded to /home/i_suzuki/.cache/ms-playwright/chromium-939194
```

インストールされたブラウザのありか

```text
~/.cache/
  `--ms-playwright/
      `--chromium-939194/
          `--chrome-linux/
              `--chrome
```

## 03. 実行スクリプトの使い方

```bash
cd ~/robotgon-python
source venv/bin/activate

# 連絡網に一斉送信する
python main.py renrakumo --genko=210807 --meibo=yakuin
python main.py renrakumo --genko=210807 --meibo=hancho

# ブラウザ自動化スクリプト
python main.py browserauto
```
