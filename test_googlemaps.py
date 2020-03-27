"""
This file should test the functionality of the googlemaps package
Created: 2020-03-26
"""

import googlemaps
import os


# set env variable "GOOGLE_API_KEY" via export/setx GOOGLE_API_KEY=<YOUR_KEY>, depending on console
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY', None) # or assign to your key in code
if GOOGLE_API_KEY is None:
	print('GOOGLE_API_KEY is not set!')
print('your key is {}'.format(GOOGLE_API_KEY))

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

city = 'Berlin'
park = gmaps.places(query='parks', location=city, radius=500, type='park', region='country:DE')
print(park)
