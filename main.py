import os

import openai
from dotenv import load_dotenv

# .envから環境変数を読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[],
)
print(response.choices[0]["message"]["content"].strip())