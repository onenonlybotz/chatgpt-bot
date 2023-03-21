from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "16051908"))
API_HASH = getenv("API_HASH", "abf9b83f9ca40cf9f5ba9bf6e6afaa8b")
BOT_TOKEN = getenv("BOT_TOKEN", "5956160709:AAHPTf3PfjgSrJ8FDlpm_qkp7jhHg927y7A")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
