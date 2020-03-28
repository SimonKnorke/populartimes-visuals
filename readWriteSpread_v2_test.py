"""Test script for spreadsheet read-write for api response
Created: 2020-03-28
Author: Simon
"""

import pandas as pd
import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
from api_helpers import create_popular_dataframe

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

GOOGLE_API_KEY = 'AIzaSyB01iwAcDWzDrs_Ltf0ZvHgX02vCjX1dpY'  # EDIT please!!
CRED_FILE = 'populartimes-visuals-c883285882c7.json'  # EDIT please!!
creds = ServiceAccountCredentials.from_json_keyfile_name(CRED_FILE, scope)
client = gspread.authorize(creds)

# load spreadsheet, read as dataframe
sh = client.open('TestData')
sh_places = sh.worksheet("places")
sh_data = sh.worksheet("data")
df_places = pd.DataFrame(sh_places.get_all_records()) # OR gd.get_as_dataframe(sh_places)
df_data = pd.DataFrame(sh_data.get_all_records())
print('-->connected to spreadsheet')

if __name__ == "__main__":
	test_id_list = ['ChIJWVbXxhhPqEcR3OZE5GXI9I4']
	df_response, response_list = create_popular_dataframe(GOOGLE_API_KEY, test_id_list, print_mode=True)
	updated = df_data.append(df_response)
	gd.set_with_dataframe(sh_data, updated)
	print('-->wrote response to spreadsheet')
