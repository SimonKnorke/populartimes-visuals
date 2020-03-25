"""
This file should test the functionality of the polulartimes package
Created: 2020-03-25
Author: Simon
"""

import populartimes
import os

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
if GOOGLE_API_KEY is None:
	print('INFO: Please set env variable "GOOGLE_API_KEY" via "export GOOGLE_API_KEY=<YOUR_KEY>"')
else:
	print('your key is {}'.format(GOOGLE_API_KEY))

# Test call for populartimes.get_id
response = populartimes.get_id(GOOGLE_API_KEY, "ChIJSYuuSx9awokRyrrOFTGg0GY")
print(response)


# Test call for populartimes.get !!! 
#response = populartimes.get(GOOGLE_API_KEY, ["bar"], (48.132986, 11.566126), (48.142199, 11.580047))
#print(response)