"""Test script for spreadsheet read-write for api response
Created: 2020-03-28
Author: Simon
"""

import json
import pandas as pd
import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
from api_helpers import create_popular_dataframe
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

#GOOGLE_API_KEY = 'AIzaSyBE29HdBocD2F5TKfq1IaePz-x_cAxB8p8'#'AIzaSyB01iwAcDWzDrs_Ltf0ZvHgX02vCjX1dpY'  # EDIT please!!
#GOOGLE_API_KEY = 'None'
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
sh_data = sh.worksheet("test") # test sheet on google sheets
df_places = pd.DataFrame(sh_places.get_all_records())  # OR gd.get_as_dataframe(sh_places)
df_data = pd.DataFrame(sh_data.get_all_records())
print('-->connected to spreadsheet')


def main():
    global df_data
    print('Start test - {}'.format(str(datetime.datetime.now())))
    test_id_list = ['ChIJWVbXxhhPqEcR3OZE5GXI9I4']
    df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, test_id_list, print_mode=False)
    updated = df_data.append(df_response)
    gd.set_with_dataframe(sh_data, updated)
    df_data = updated
    print('-->wrote response to spreadsheet')


if __name__ == "__main__":
    main()
    #print('Set schedule for Interval: {} Hours'.format(HOURS_INTERVAL))
    #scheduler = BlockingScheduler()
    #scheduler.add_job(main, 'interval', minutes=1)  # hours, minutes, seconds=5
    #scheduler.start()
