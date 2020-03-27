"""
This file should test the functionality of the polulartimes package
Created: 2020-03-25
Author: Simon
"""

import populartimes
import os
import googlemaps
import pprint


GOOGLE_API_KEY = 'AIzaSyB96Sd3bMylEC7M0Snydz8QblpmXhW0QqQ' #('GOOGLE_API_KEY')
if GOOGLE_API_KEY is None:
	print('INFO: Please set env variable "GOOGLE_API_KEY" via "export GOOGLE_API_KEY=<YOUR_KEY>"')
else:
	print('your key is {}'.format(GOOGLE_API_KEY))

# Test call for populartimes.get_id
response = populartimes.get_id(GOOGLE_API_KEY, "ChIJnc3vbEgJvUcRxGJfy-eGHW8")
print(response)
