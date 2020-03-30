"""Automated script to update data every hour
Created: 2020-03-28
Author: Simon
"""

import json
import pandas as pd
#import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
from api_helpers import create_popular_dataframe, dump_response_list, connect_to_spreadsheet
import time
import datetime

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

DUMP_FOLDER = './collected_data/'
with open('api_creds.json', 'r') as fp:
    api_creds = json.load(fp)
    GOOGLE_API_KEY = api_creds.get('GOOGLE_API_KEY', 'None')
print('GOOGLE_API_KEY: {}'.format(GOOGLE_API_KEY))

SERVICE_CREDS = 'service_creds.json'  # EDIT please!!
SPREADSHEET = 'TestData'
SHEET_PLACES = 'places'
SHEET_DATA = 'data'

creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_CREDS, scope)


def main():
    print('Start Places script - {}'.format(str(datetime.datetime.now())))
    sh = connect_to_spreadsheet(SPREADSHEET, creds, print_mode=True)
    sh_places = sh.worksheet(SHEET_PLACES)
    sh_data = sh.worksheet(SHEET_DATA)
    df_places = pd.DataFrame(sh_places.get_all_records())
    df_data = pd.DataFrame(sh_data.get_all_records())
    places_id_list = df_places.loc[df_places['deactivated'] == '', 'PlacesID'].to_list()

    print('--> create pop dataframe for {} places'.format(len(places_id_list)))
    df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, places_id_list, print_mode=False)
    dump_response_list(response_list, DUMP_FOLDER)
    print('saved responses in {}'.format(DUMP_FOLDER))

    updated = df_data.append(df_response)
    gd.set_with_dataframe(sh_data, updated)
    print('-->wrote response to spreadsheet')


def get_seconds_till_next_hour():
    now = datetime.datetime.now()
    return 3600 - (now.minute * 60 + now.second)


if __name__ == "__main__":
    START_NOW = False
    HOUR_START = 9
    HOUR_END = 21
    now = datetime.datetime.now()
    while (now.hour >= HOUR_START - 1) and (now.hour < HOUR_END):
        sleep_sec = get_seconds_till_next_hour()
        print('--> Seconds till next run: {} secs'.format(sleep_sec))
        time.sleep(sleep_sec)
        main()


