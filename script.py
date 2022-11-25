import requests
import os
from os.path import dirname, join
from dotenv import load_dotenv
import schedule
import time


##### .env adjustments
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HEROKU_TOKEN = os.environ.get("HEROKU_TOKEN")
APP_NAME = os.environ.get("APP_NAME")

def restart_all_dynos():
	URL = f"https://api.heroku.com/apps/{APP_NAME}/dynos"
	HEADERS = {
		"Accept": "application/vnd.heroku+json; version=3",
		"Authorization": f"Bearer {HEROKU_TOKEN}"
	}
	r = requests.delete(url = URL, headers=HEADERS)
	print(r.status_code)
	return r.status_code

schedule.every(20).minutes.do(restart_all_dynos)
print("SCRIPT STARTED SUCCESSFULY")
while True:
    schedule.run_pending()
    time.sleep(1)
