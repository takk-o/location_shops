from os import environ
from pathlib import Path
from dotenv import load_dotenv

# .envファイル読み込み
dotenv_path = Path.cwd().joinpath('.env')
load_dotenv(dotenv_path)
# API_KEY取得
key = environ.get('API_KEY')
