"""Helper module to transform/handle the api response for populartimes
Created: 2020-03-28
Author: Simon
"""

import datetime
import populartimes
import pandas as pd
from collections import OrderedDict
import joblib
import gspread


def create_popular_dataframe(GOOGLE_API_KEY, places_id_list, print_mode=False):
    """Dataframe for cleaned API rensponse (simpler dict) + timestamps."""
    response_list = []  # original responses as list, could be saved as pickle file if wanted
    reponse_dict_list = []
    for idx, place_id in enumerate(places_id_list):
        #time.sleep(10)
        dt_now = datetime.datetime.now()
        str_now = dt_now.strftime('%Y-%m-%d_%H%M%S')
        try:
            response = populartimes.get_id(GOOGLE_API_KEY, place_id)
            print('get place {}: {}'.format(idx, response.get('name', 'None')))
            response_list.append(response)
            clean_response = get_clean_response(response)
            clean_response['timestamp'] = dt_now#str_now  # Put datetime in response dict
            clean_response = OrderedDict(clean_response)  # to set timestamp to beginning
            clean_response.move_to_end('timestamp', last=False)
            reponse_dict_list.append(clean_response)
            if print_mode:
                print('Response for Time {}:'.format(str_now))
                for (key, val) in clean_response.items():
                    print('{}: {}'.format(key, val))
                print(clean_response)
        except:
            print('not worked for this one')
    df_response = pd.DataFrame(reponse_dict_list)
    return df_response, response_list


def get_clean_response(response):
    """Transform the response dict to a more simple dict with simple values str or int.
    Current state: Without coordinates"""
    new_dict = dict()
    easy_keys = ['id', 'name', 'address', 'rating', 'rating_n', 'current_popularity']
    for key in easy_keys:
        new_dict[key] = response.get(key, 'None')
    new_dict['types'] = '-'.join(response.get('types', ['None']))  # concatenate types with '-' or 'None' if no types
    #new_dict['lat'] = response.get('coordinates', {'lat': 51})['lat']  # ignore coordinates for dataframe
    #new_dict['lng'] = response.get('coordinates', {'lng': 10})['lng']
    time_spent = response.get('time_spent', ['None']) # e.g. time_spent: [60,60], 
    new_dict['time_spent'] = '-'.join([str(i) for i in time_spent]) # have to convert to string for join
    populartimes_list = response.get('populartimes', []) # look for populartimes or return empty list
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day_idx, day in enumerate(weekdays):
        key = 'populartimes_{}'.format(day)
        if len(populartimes_list) == 7:  # only write when we got all weekdays (can be discussed!)
            pop_data = populartimes_list[day_idx].get('data', ['None'])   # 'data': [1,0,0,0,0,0,0,0,0,0,20,25,29,32,33,31,28,23,18,13,9,5,2,0]
            new_dict[key] = '-'.join([str(i) for i in pop_data]) # 1-0-0-0-...
        else: 
            new_dict[key] = 'None'  
    return new_dict


def dump_response_list(response_list, folder_path):
    """store response_list locally"""
    dt_now = datetime.datetime.now()
    str_now = dt_now.strftime('%Y-%m-%d_%H%M%S')
    filename = '{}_response_list.pkl'.format(str_now)
    joblib.dump(response_list, folder_path + filename)


def connect_to_spreadsheet(spreadsheet, creds, print_mode=False):
    client = gspread.authorize(creds)
    sh = client.open(spreadsheet)
    if print_mode:
        print('-->connected to spreadsheet')
    return sh


