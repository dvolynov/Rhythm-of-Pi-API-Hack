import os, dotenv, configparser

from database import Database, error_handler


dotenv.load_dotenv()
config = configparser.ConfigParser()
config.read('config.ini')


SUNO_TOKEN     = os.getenv("SUNO_API_TOKEN")
DOMAIN         = os.getenv("DOMAIN")

SAVE_DIRECTORY = config['GENERAL']['SAVE_DIRECTORY']
CUSTOM_MODE    = config['SUNO']['CUSTOM_MODE']
INSTRUMENTAL   = config['SUNO']['INSTRUMENTAL']
MODEL          = config['SUNO']['MODEL']

print(f"{DOMAIN+SAVE_DIRECTORY=}")
print(f"{CUSTOM_MODE=}")
print(f"{INSTRUMENTAL=}")
print(f"{MODEL=}")

db = Database()