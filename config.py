import os
from dotenv import load_dotenv

load_dotenv()

FINANCIAL_DATA_API_KEY = os.getenv("FINANCIAL_DATA_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_TA_PARAMETERS = {
    "rsi_period": 14,
    "macd_fast": 12,
    "macd_slow": 26,
    "macd_signal": 9,
    "bollinger_window": 20,
    "bollinger_std_dev": 2
}
