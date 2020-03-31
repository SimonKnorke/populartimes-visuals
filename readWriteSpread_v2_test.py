"""Test script for spreadsheet read-write for api response
Created: 2020-03-28
Author: Simon
"""

import json
import pandas as pd

import gspread_dataframe as gd
from api_helpers import create_popular_dataframe, connect_to_spreadsheet
from apscheduler.schedulers.blocking import BlockingScheduler
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import time

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

#GOOGLE_API_KEY = ''
with open('api_creds.json', 'r') as fp:
    api_creds = json.load(fp)
    GOOGLE_API_KEY = api_creds.get('GOOGLE_API_KEY', 'None')
print('GOOGLE_API_KEY: {}'.format(GOOGLE_API_KEY))

SERVICE_CREDS = 'service_creds.json'  # EDIT please!!
SPREADSHEET = 'TestData'
SHEET_PLACES = 'places'
SHEET_DATA = 'test'


def main():
    print('Start test - {}'.format(str(datetime.datetime.now())))
    creds = ServiceAccountCredentials.from_json_keyfile_name(SERVICE_CREDS, scope)
    sh = connect_to_spreadsheet(SPREADSHEET, creds, print_mode=True)
    sh_places = sh.worksheet(SHEET_PLACES)
    sh_data = sh.worksheet(SHEET_DATA)
    df_places = pd.DataFrame(sh_places.get_all_records())
    df_data = pd.DataFrame(sh_data.get_all_records())
    places_id_list = ['ChIJWVbXxhhPqEcR3OZE5GXI9I4']
    df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, places_id_list, print_mode=False)
    print('--> got response from places API')
    updated = df_data.append(df_response)
    gd.set_with_dataframe(sh_data, updated)
    print('-->wrote response to spreadsheet')


if __name__ == "__main__":
    main()
