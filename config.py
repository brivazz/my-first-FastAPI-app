import os
from dotenv import load_dotenv


load_dotenv()

ENV_SECRET = os.getenv('ENV_SECRET')
DO_API_ACCESS_TOKEN = os.getenv('DO_API_ACCESS_TOKEN')
