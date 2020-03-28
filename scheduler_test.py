"""Automated script to update data every hour
Created: 2020-03-28
Author: Simon
"""

import pandas as pd
import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
from api_helpers import create_popular_dataframe, dump_response_list
from apscheduler.schedulers.blocking import BlockingScheduler

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

DUMP_FOLDER = './collected_data/'
GOOGLE_API_KEY = 'AIzaSyB01iwAcDWzDrs_Ltf0ZvHgX02vCjX1dpY'  # EDIT please!!
CRED_FILE = 'creds.json'  # EDIT please!!
HOURS_INTERVAL = 1
creds = ServiceAccountCredentials.from_json_keyfile_name(CRED_FILE, scope)
client = gspread.authorize(creds)

# load spreadsheet, read as dataframe
sh = client.open('TestData')
sh_places = sh.worksheet("places")
sh_data = sh.worksheet("data")
# sh_test = sh.worksheet("data")
df_places = pd.DataFrame(sh_places.get_all_records())  # OR gd.get_as_dataframe(sh_places)
df_data = pd.DataFrame(sh_data.get_all_records())
print('-->connected to spreadsheet')


def main():
    places_id_list = df_places['PlacesID'].to_list()
    df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, places_id_list, print_mode=False)
    dump_response_list(response_list, DUMP_FOLDER)
    updated = df_data.append(df_response)
    gd.set_with_dataframe(sh_data, updated)
    print('-->wrote response to spreadsheet')


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(main, 'interval', hours=HOURS_INTERVAL)  # hours, seconds=5
    print('Set schedule for Interval: {} Hours'.format(HOURS_INTERVAL))
    scheduler.start()
