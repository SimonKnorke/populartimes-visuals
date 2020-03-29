"""Automated script to update data every hour
Created: 2020-03-28
Author: Simon
"""

import json
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

HOURS_INTERVAL = 1
DUMP_FOLDER = './collected_data/'
with open('api_creds.json', 'r') as fp:
    api_creds = json.load(fp)
    GOOGLE_API_KEY = api_creds.get('GOOGLE_API_KEY', 'None')
print('GOOGLE_API_KEY: {}'.format(GOOGLE_API_KEY))
SERVICE_CREDS = 'service_creds.json'  # EDIT please!!
creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_CREDS, scope)
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
    global df_data
    #places_id_list = df_places['PlacesID'].to_list()
    places_id_list = df_places.loc[df_places['deactivated'] == '', 'PlacesID'].to_list()
    print('--> create pop dataframe for {} places'.format(len(places_id_list)))
    df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, places_id_list, print_mode=False)
    dump_response_list(response_list, DUMP_FOLDER)
    updated = df_data.append(df_response)
    gd.set_with_dataframe(sh_data, updated)
    df_data = updated
    print('-->wrote response to spreadsheet')


if __name__ == "__main__":
    #print('Set schedule for Interval: {} Hours'.format(HOURS_INTERVAL))
    #scheduler = BlockingScheduler()
    #scheduler.add_job(main, 'interval', minutes=HOURS_INTERVAL)  # hours, minutes, seconds=5
    #scheduler.start()
    main()

