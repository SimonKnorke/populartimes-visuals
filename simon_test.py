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
response = populartimes.get_id(GOOGLE_API_KEY, "ChIJSYuuSx9awokRyrrOFTGg0GY")
print(response)

#germany rectangular 54.418930,6.041843 47.597696,15.092453
# Test call for populartimes.get !!!
#response = populartimes.get(GOOGLE_API_KEY, ["zoo"],  (49.313618, 10.854743), (49.541317, 11.277381))
#print(response)
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# Do a simple nearby search where we specify the location
# in lat/lon format, along with a radius measured in meters
parks = gmaps.places_nearby(location='50.8271434,10.181946', radius=3000, open_now=False, type='park')
#pprint.pprint(parks['results'])
print(len(parks['results']))
for park in parks['results']:
	print(park['name'])