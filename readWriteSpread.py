import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import populartimes
import os
import googlemaps
import pprint

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

GOOGLE_API_KEY = 'AIzaSyB96Sd3bMylEC7M0Snydz8QblpmXhW0QqQ' #('GOOGLE_API_KEY')
if GOOGLE_API_KEY is None:
	print('INFO: Please set env variable "GOOGLE_API_KEY" via "export GOOGLE_API_KEY=<YOUR_KEY>"')
else:
	pass
# Test call for populartimes.get_id




#places = client.open("TestData").sheet1  # Open the spreadhseet
sh = client.open('TestData')
places = sh.worksheet("places")
data = sh.worksheet("data")
placesWeTrack = places.get_all_values()
columnNames = ['id', 'name', 'address', 'types', 'coordinates', 'rating',
               'international_phone_number', 'current_popularity','populartimes', 'time_spent']
rowNumber = 2
for i, place in enumerate(placesWeTrack):
    if i > 1 and place[0] != '' and i < 3:
        response = populartimes.get_id(GOOGLE_API_KEY, place[3])
        newRow = []
        columnNumber = 0
        for name in columnNames:
            for key in response.keys():
                if name == key:
                    columnNumber += 1
                    print(response[key])
                    newRow.append(key)
        data.update('B{}'.format(rowNumber), [newRow])
        rowNumber += 1
#data = sheet.get_all_records()  # Get a list of all records
#print(data)
#sheet = client.open("TestData").sheet1  # Open the spreadhseet
'''
row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1, 2).value  # Get the value of a specific cell

insertRow = ["hello", "red", "blue"]
sheet.add_rows(insertRow, 3)  # Insert the list as a row at index 4

sheet.update_cell(2, 2, "CHANGED")  # Update one cell

numRows = sheet.row_count  # Get the number of rows in the sheet'''