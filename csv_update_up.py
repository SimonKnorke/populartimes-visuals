from datetime import date
import datetime
import pickle
import pandas as pd
import populartimes
import os
import googlemaps
import pprint


key = 'Your API Key' 
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

df1 = pd.read_csv("ptt.csv", encoding="latin-1")

ans = []

for i in df1.iterrows():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")

    data = populartimes.get_id(key, i[1][3])
    print(data["name"])
    if "current_popularity" in data:
        pickle.dump([i[1][0], i[1][1], i[1][2], i[1][3], data], open(f"C:\\dumps\\{i[1][0]}_{i[1][1]}_{i[1][2]}_{dt_string}.p", "wb"))

    else:
        print("No Popularity-Data for " + f"{i[1][0]}_{i[1][1]}_{i[1][2]}")





cities = []
types = []
places = []
timestamp = []
current_popularity = []
years = []
months = []
days = []
hours = []
mean_popularity = []
place_id = []
place_coord_lat = []
place_coord_lon = []
popularity_mo_0 = []
popularity_mo_1 = []
popularity_mo_2 = [] 
popularity_mo_3 = []
popularity_mo_4 = []
popularity_mo_5 = []
popularity_mo_6 = []
popularity_mo_7 = []
popularity_mo_8 = []
popularity_mo_9 = []
popularity_mo_10 = []
popularity_mo_11 = []
popularity_mo_12 = []
popularity_mo_13 = []
popularity_mo_14 = []
popularity_mo_15 = []
popularity_mo_16 = []
popularity_mo_17 = []
popularity_mo_18 = []
popularity_mo_19 = []
popularity_mo_20 = []
popularity_mo_21 = []
popularity_mo_22 = []
popularity_mo_23 = []
popularity_tu_0 = []
popularity_tu_1 = []
popularity_tu_2 = [] 
popularity_tu_3 = []
popularity_tu_4 = []
popularity_tu_5 = []
popularity_tu_6 = []
popularity_tu_7 = []
popularity_tu_8 = []
popularity_tu_9 = []
popularity_tu_10 = []
popularity_tu_11 = []
popularity_tu_12 = []
popularity_tu_13 = []
popularity_tu_14 = []
popularity_tu_15 = []
popularity_tu_16 = []
popularity_tu_17 = []
popularity_tu_18 = []
popularity_tu_19 = []
popularity_tu_20 = []
popularity_tu_21 = []
popularity_tu_22 = []
popularity_tu_23 = []
popularity_wed_0 = []
popularity_wed_1 = []
popularity_wed_2 = [] 
popularity_wed_3 = []
popularity_wed_4 = []
popularity_wed_5 = []
popularity_wed_6 = []
popularity_wed_7 = []
popularity_wed_8 = []
popularity_wed_9 = []
popularity_wed_10 = []
popularity_wed_11 = []
popularity_wed_12 = []
popularity_wed_13 = []
popularity_wed_14 = []
popularity_wed_15 = []
popularity_wed_16 = []
popularity_wed_17 = []
popularity_wed_18 = []
popularity_wed_19 = []
popularity_wed_20 = []
popularity_wed_21 = []
popularity_wed_22 = []
popularity_wed_23 = []
popularity_th_0 = []
popularity_th_1 = []
popularity_th_2 = [] 
popularity_th_3 = []
popularity_th_4 = []
popularity_th_5 = []
popularity_th_6 = []
popularity_th_7 = []
popularity_th_8 = []
popularity_th_9 = []
popularity_th_10 = []
popularity_th_11 = []
popularity_th_12 = []
popularity_th_13 = []
popularity_th_14 = []
popularity_th_15 = []
popularity_th_16 = []
popularity_th_17 = []
popularity_th_18 = []
popularity_th_19 = []
popularity_th_20 = []
popularity_th_21 = []
popularity_th_22 = []
popularity_th_23 = []
popularity_fr_0 = []
popularity_fr_1 = []
popularity_fr_2 = [] 
popularity_fr_3 = []
popularity_fr_4 = []
popularity_fr_5 = []
popularity_fr_6 = []
popularity_fr_7 = []
popularity_fr_8 = []
popularity_fr_9 = []
popularity_fr_10 = []
popularity_fr_11 = []
popularity_fr_12 = []
popularity_fr_13 = []
popularity_fr_14 = []
popularity_fr_15 = []
popularity_fr_16 = []
popularity_fr_17 = []
popularity_fr_18 = []
popularity_fr_19 = []
popularity_fr_20 = []
popularity_fr_21 = []
popularity_fr_22 = []
popularity_fr_23 = []
popularity_sat_0 = []
popularity_sat_1 = []
popularity_sat_2 = [] 
popularity_sat_3 = []
popularity_sat_4 = []
popularity_sat_5 = []
popularity_sat_6 = []
popularity_sat_7 = []
popularity_sat_8 = []
popularity_sat_9 = []
popularity_sat_10 = []
popularity_sat_11 = []
popularity_sat_12 = []
popularity_sat_13 = []
popularity_sat_14 = []
popularity_sat_15 = []
popularity_sat_16 = []
popularity_sat_17 = []
popularity_sat_18 = []
popularity_sat_19 = []
popularity_sat_20 = []
popularity_sat_21 = []
popularity_sat_22 = []
popularity_sat_23 = []
popularity_su_0 = []
popularity_su_1 = []
popularity_su_2 = [] 
popularity_su_3 = []
popularity_su_4 = []
popularity_su_5 = []
popularity_su_6 = []
popularity_su_7 = []
popularity_su_8 = []
popularity_su_9 = []
popularity_su_10 = []
popularity_su_11 = []
popularity_su_12 = []
popularity_su_13 = []
popularity_su_14 = []
popularity_su_15 = []
popularity_su_16 = []
popularity_su_17 = []
popularity_su_18 = []
popularity_su_19 = []
popularity_su_20 = []
popularity_su_21 = []
popularity_su_22 = []
popularity_su_23 = []
time_spent_lo = []
time_spent_hi = []
tstamps = []
timestamp_2 = []

adr = r"C:\Your\Working\Path"
entries = os.listdir(adr)
wd = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
for item in entries:


    f = pickle.load(open(f"{adr}//{item}", "rb"))
    [city, typ, name, tstamp] = item.split("_")
    [tstamp, _] = tstamp.split(".")
    [day, month, year, hour, _, _] = tstamp.split("-")

    wksday = date(int(year), int(month), int(day))
    
    time = datetime.datetime(int(year), int(month), int(day), int(hour), 0, 0)


    nameOfDay = wksday.weekday()


    cities.append(city)
    types.append(typ)
    places.append(name)
    timestamp.append(tstamp)
    timestamp_2.append(time)
    years.append(year)
    months.append(month)
    days.append(day)
    hours.append(hour)
    tstamps.append(f"{month}-{day}-{hour}")
    current_popularity.append(f[4]["current_popularity"])
    place_id.append(f[4]['id'])
    place_coord_lat.append(f[4]['coordinates']['lat'])
    place_coord_lon.append(f[4]['coordinates']['lng'])

    popularity_mo_0.append(f[4]["populartimes"][0]["data"][0])
    popularity_mo_1.append(f[4]["populartimes"][0]["data"][1])
    popularity_mo_2.append(f[4]["populartimes"][0]["data"][2])
    popularity_mo_3.append(f[4]["populartimes"][0]["data"][3])
    popularity_mo_4.append(f[4]["populartimes"][0]["data"][4])
    popularity_mo_5.append(f[4]["populartimes"][0]["data"][5])
    popularity_mo_6.append(f[4]["populartimes"][0]["data"][6])
    popularity_mo_7.append(f[4]["populartimes"][0]["data"][7])
    popularity_mo_8.append(f[4]["populartimes"][0]["data"][8])
    popularity_mo_9.append(f[4]["populartimes"][0]["data"][9])
    popularity_mo_10.append(f[4]["populartimes"][0]["data"][10])
    popularity_mo_11.append(f[4]["populartimes"][0]["data"][11])
    popularity_mo_12.append(f[4]["populartimes"][0]["data"][12])
    popularity_mo_13.append(f[4]["populartimes"][0]["data"][13])
    popularity_mo_14.append(f[4]["populartimes"][0]["data"][14])
    popularity_mo_15.append(f[4]["populartimes"][0]["data"][15])
    popularity_mo_16.append(f[4]["populartimes"][0]["data"][16])
    popularity_mo_17.append(f[4]["populartimes"][0]["data"][17])
    popularity_mo_18.append(f[4]["populartimes"][0]["data"][18])
    popularity_mo_19.append(f[4]["populartimes"][0]["data"][19])
    popularity_mo_20.append(f[4]["populartimes"][0]["data"][20])
    popularity_mo_21.append(f[4]["populartimes"][0]["data"][21])
    popularity_mo_22.append(f[4]["populartimes"][0]["data"][22])
    popularity_mo_23.append(f[4]["populartimes"][0]["data"][23])
    popularity_tu_0.append(f[4]["populartimes"][1]["data"][0])
    popularity_tu_1.append(f[4]["populartimes"][1]["data"][1])
    popularity_tu_2.append(f[4]["populartimes"][1]["data"][2])
    popularity_tu_3.append(f[4]["populartimes"][1]["data"][3])
    popularity_tu_4.append(f[4]["populartimes"][1]["data"][4])
    popularity_tu_5.append(f[4]["populartimes"][1]["data"][5])
    popularity_tu_6.append(f[4]["populartimes"][1]["data"][6])
    popularity_tu_7.append(f[4]["populartimes"][1]["data"][7])
    popularity_tu_8.append(f[4]["populartimes"][1]["data"][8])
    popularity_tu_9.append(f[4]["populartimes"][1]["data"][9])
    popularity_tu_10.append(f[4]["populartimes"][1]["data"][10])
    popularity_tu_11.append(f[4]["populartimes"][1]["data"][11])
    popularity_tu_12.append(f[4]["populartimes"][1]["data"][12])
    popularity_tu_13.append(f[4]["populartimes"][1]["data"][13])
    popularity_tu_14.append(f[4]["populartimes"][1]["data"][14])
    popularity_tu_15.append(f[4]["populartimes"][1]["data"][15])
    popularity_tu_16.append(f[4]["populartimes"][1]["data"][16])
    popularity_tu_17.append(f[4]["populartimes"][1]["data"][17])
    popularity_tu_18.append(f[4]["populartimes"][1]["data"][18])
    popularity_tu_19.append(f[4]["populartimes"][1]["data"][19])
    popularity_tu_20.append(f[4]["populartimes"][1]["data"][20])
    popularity_tu_21.append(f[4]["populartimes"][1]["data"][21])
    popularity_tu_22.append(f[4]["populartimes"][1]["data"][22])
    popularity_tu_23.append(f[4]["populartimes"][1]["data"][23])
    popularity_wed_0.append(f[4]["populartimes"][2]["data"][0])
    popularity_wed_1.append(f[4]["populartimes"][2]["data"][1])
    popularity_wed_2.append(f[4]["populartimes"][2]["data"][2])
    popularity_wed_3.append(f[4]["populartimes"][2]["data"][3])
    popularity_wed_4.append(f[4]["populartimes"][2]["data"][4])
    popularity_wed_5.append(f[4]["populartimes"][2]["data"][5])
    popularity_wed_6.append(f[4]["populartimes"][2]["data"][6])
    popularity_wed_7.append(f[4]["populartimes"][2]["data"][7])
    popularity_wed_8.append(f[4]["populartimes"][2]["data"][8])
    popularity_wed_9.append(f[4]["populartimes"][2]["data"][9])
    popularity_wed_10.append(f[4]["populartimes"][2]["data"][10])
    popularity_wed_11.append(f[4]["populartimes"][2]["data"][11])
    popularity_wed_12.append(f[4]["populartimes"][2]["data"][12])
    popularity_wed_13.append(f[4]["populartimes"][2]["data"][13])
    popularity_wed_14.append(f[4]["populartimes"][2]["data"][14])
    popularity_wed_15.append(f[4]["populartimes"][2]["data"][15])
    popularity_wed_16.append(f[4]["populartimes"][2]["data"][16])
    popularity_wed_17.append(f[4]["populartimes"][2]["data"][17])
    popularity_wed_18.append(f[4]["populartimes"][2]["data"][18])
    popularity_wed_19.append(f[4]["populartimes"][2]["data"][19])
    popularity_wed_20.append(f[4]["populartimes"][2]["data"][20])
    popularity_wed_21.append(f[4]["populartimes"][2]["data"][21])
    popularity_wed_22.append(f[4]["populartimes"][2]["data"][22])
    popularity_wed_23.append(f[4]["populartimes"][2]["data"][23])
    popularity_th_0.append(f[4]["populartimes"][3]["data"][0])
    popularity_th_1.append(f[4]["populartimes"][3]["data"][1])
    popularity_th_2.append(f[4]["populartimes"][3]["data"][2])
    popularity_th_3.append(f[4]["populartimes"][3]["data"][3])
    popularity_th_4.append(f[4]["populartimes"][3]["data"][4])
    popularity_th_5.append(f[4]["populartimes"][3]["data"][5])
    popularity_th_6.append(f[4]["populartimes"][3]["data"][6])
    popularity_th_7.append(f[4]["populartimes"][3]["data"][7])
    popularity_th_8.append(f[4]["populartimes"][3]["data"][8])
    popularity_th_9.append(f[4]["populartimes"][3]["data"][9])
    popularity_th_10.append(f[4]["populartimes"][3]["data"][10])
    popularity_th_11.append(f[4]["populartimes"][3]["data"][11])
    popularity_th_12.append(f[4]["populartimes"][3]["data"][12])
    popularity_th_13.append(f[4]["populartimes"][3]["data"][13])
    popularity_th_14.append(f[4]["populartimes"][3]["data"][14])
    popularity_th_15.append(f[4]["populartimes"][3]["data"][15])
    popularity_th_16.append(f[4]["populartimes"][3]["data"][16])
    popularity_th_17.append(f[4]["populartimes"][3]["data"][17])
    popularity_th_18.append(f[4]["populartimes"][3]["data"][18])
    popularity_th_19.append(f[4]["populartimes"][3]["data"][19])
    popularity_th_20.append(f[4]["populartimes"][3]["data"][20])
    popularity_th_21.append(f[4]["populartimes"][3]["data"][21])
    popularity_th_22.append(f[4]["populartimes"][3]["data"][22])
    popularity_th_23.append(f[4]["populartimes"][3]["data"][23])
    popularity_fr_0.append(f[4]["populartimes"][4]["data"][0])
    popularity_fr_1.append(f[4]["populartimes"][4]["data"][1])
    popularity_fr_2.append(f[4]["populartimes"][4]["data"][2])
    popularity_fr_3.append(f[4]["populartimes"][4]["data"][3])
    popularity_fr_4.append(f[4]["populartimes"][4]["data"][4])
    popularity_fr_5.append(f[4]["populartimes"][4]["data"][5])
    popularity_fr_6.append(f[4]["populartimes"][4]["data"][6])
    popularity_fr_7.append(f[4]["populartimes"][4]["data"][7])
    popularity_fr_8.append(f[4]["populartimes"][4]["data"][8])
    popularity_fr_9.append(f[4]["populartimes"][4]["data"][9])
    popularity_fr_10.append(f[4]["populartimes"][4]["data"][10])
    popularity_fr_11.append(f[4]["populartimes"][4]["data"][11])
    popularity_fr_12.append(f[4]["populartimes"][4]["data"][12])
    popularity_fr_13.append(f[4]["populartimes"][4]["data"][13])
    popularity_fr_14.append(f[4]["populartimes"][4]["data"][14])
    popularity_fr_15.append(f[4]["populartimes"][4]["data"][15])
    popularity_fr_16.append(f[4]["populartimes"][4]["data"][16])
    popularity_fr_17.append(f[4]["populartimes"][4]["data"][17])
    popularity_fr_18.append(f[4]["populartimes"][4]["data"][18])
    popularity_fr_19.append(f[4]["populartimes"][4]["data"][19])
    popularity_fr_20.append(f[4]["populartimes"][4]["data"][20])
    popularity_fr_21.append(f[4]["populartimes"][4]["data"][21])
    popularity_fr_22.append(f[4]["populartimes"][4]["data"][22])
    popularity_fr_23.append(f[4]["populartimes"][4]["data"][23])
    popularity_sat_0.append(f[4]["populartimes"][5]["data"][0])
    popularity_sat_1.append(f[4]["populartimes"][5]["data"][1])
    popularity_sat_2.append(f[4]["populartimes"][5]["data"][2])
    popularity_sat_3.append(f[4]["populartimes"][5]["data"][3])
    popularity_sat_4.append(f[4]["populartimes"][5]["data"][4])
    popularity_sat_5.append(f[4]["populartimes"][5]["data"][5])
    popularity_sat_6.append(f[4]["populartimes"][5]["data"][6])
    popularity_sat_7.append(f[4]["populartimes"][5]["data"][7])
    popularity_sat_8.append(f[4]["populartimes"][5]["data"][8])
    popularity_sat_9.append(f[4]["populartimes"][5]["data"][9])
    popularity_sat_10.append(f[4]["populartimes"][5]["data"][10])
    popularity_sat_11.append(f[4]["populartimes"][5]["data"][11])
    popularity_sat_12.append(f[4]["populartimes"][5]["data"][12])
    popularity_sat_13.append(f[4]["populartimes"][5]["data"][13])
    popularity_sat_14.append(f[4]["populartimes"][5]["data"][14])
    popularity_sat_15.append(f[4]["populartimes"][5]["data"][15])
    popularity_sat_16.append(f[4]["populartimes"][5]["data"][16])
    popularity_sat_17.append(f[4]["populartimes"][5]["data"][17])
    popularity_sat_18.append(f[4]["populartimes"][5]["data"][18])
    popularity_sat_19.append(f[4]["populartimes"][5]["data"][19])
    popularity_sat_20.append(f[4]["populartimes"][5]["data"][20])
    popularity_sat_21.append(f[4]["populartimes"][5]["data"][21])
    popularity_sat_22.append(f[4]["populartimes"][5]["data"][22])
    popularity_sat_23.append(f[4]["populartimes"][5]["data"][23])
    popularity_su_0.append(f[4]["populartimes"][6]["data"][0])
    popularity_su_1.append(f[4]["populartimes"][6]["data"][1])
    popularity_su_2.append(f[4]["populartimes"][6]["data"][2])
    popularity_su_3.append(f[4]["populartimes"][6]["data"][3])
    popularity_su_4.append(f[4]["populartimes"][6]["data"][4])
    popularity_su_5.append(f[4]["populartimes"][6]["data"][5])
    popularity_su_6.append(f[4]["populartimes"][6]["data"][6])
    popularity_su_7.append(f[4]["populartimes"][6]["data"][7])
    popularity_su_8.append(f[4]["populartimes"][6]["data"][8])
    popularity_su_9.append(f[4]["populartimes"][6]["data"][9])
    popularity_su_10.append(f[4]["populartimes"][6]["data"][10])
    popularity_su_11.append(f[4]["populartimes"][6]["data"][11])
    popularity_su_12.append(f[4]["populartimes"][6]["data"][12])
    popularity_su_13.append(f[4]["populartimes"][6]["data"][13])
    popularity_su_14.append(f[4]["populartimes"][6]["data"][14])
    popularity_su_15.append(f[4]["populartimes"][6]["data"][15])
    popularity_su_16.append(f[4]["populartimes"][6]["data"][16])
    popularity_su_17.append(f[4]["populartimes"][6]["data"][17])
    popularity_su_18.append(f[4]["populartimes"][6]["data"][18])
    popularity_su_19.append(f[4]["populartimes"][6]["data"][19])
    popularity_su_20.append(f[4]["populartimes"][6]["data"][20])
    popularity_su_21.append(f[4]["populartimes"][6]["data"][21])
    popularity_su_22.append(f[4]["populartimes"][6]["data"][22])
    popularity_su_23.append(f[4]["populartimes"][6]["data"][23])
    if "time_spent" in f[4]:
        time_spent_lo.append(f[4]["time_spent"][0])
        time_spent_hi.append(f[4]["time_spent"][1])
    else:
        time_spent_lo.append("-")
        time_spent_hi.append("-")




df_dict_1 = {"City": cities, 
		"Type": types, 
		"Place": places, 
		"Timestamp": timestamp, 
		"Timestamp2": timestamp_2,
		"Year": years, 
		"Month": months, 
		"Day": days, 
		"Hour": hours,
		"tstamps": tstamps,
        "current_popularity": current_popularity,
        "place_id": place_id, 
        "place_coord_lat": place_coord_lat, 
        "place_coord_lon": place_coord_lon,
        "popularity_mo_0": popularity_mo_0,
        "popularity_mo_1": popularity_mo_1,
        "popularity_mo_2": popularity_mo_2,
        "popularity_mo_3": popularity_mo_3,
        "popularity_mo_4": popularity_mo_4,
        "popularity_mo_5": popularity_mo_5,
        "popularity_mo_6": popularity_mo_6,
        "popularity_mo_7": popularity_mo_7,
        "popularity_mo_8": popularity_mo_8,
        "popularity_mo_9": popularity_mo_9,
        "popularity_mo_10": popularity_mo_10,
        "popularity_mo_11": popularity_mo_11,
        "popularity_mo_12": popularity_mo_12,
        "popularity_mo_13": popularity_mo_13,
        "popularity_mo_14": popularity_mo_14,
        "popularity_mo_15": popularity_mo_15,
        "popularity_mo_16": popularity_mo_16,
        "popularity_mo_17": popularity_mo_17,
        "popularity_mo_18": popularity_mo_18,
        "popularity_mo_19": popularity_mo_19,
        "popularity_mo_20": popularity_mo_20,
        "popularity_mo_21": popularity_mo_21,
        "popularity_mo_22": popularity_mo_22,
        "popularity_mo_23": popularity_mo_23,
        "popularity_tu_0": popularity_tu_0,
        "popularity_tu_1": popularity_tu_1,
        "popularity_tu_2": popularity_tu_2,
        "popularity_tu_3": popularity_tu_3,
        "popularity_tu_4": popularity_tu_4,
        "popularity_tu_5": popularity_tu_5,
        "popularity_tu_6": popularity_tu_6,
        "popularity_tu_7": popularity_tu_7,
        "popularity_tu_8": popularity_tu_8,
        "popularity_tu_9": popularity_tu_9,
        "popularity_tu_10": popularity_tu_10,
        "popularity_tu_11": popularity_tu_11,
        "popularity_tu_12": popularity_tu_12,
        "popularity_tu_13": popularity_tu_13,
        "popularity_tu_14": popularity_tu_14,
        "popularity_tu_15": popularity_tu_15,
        "popularity_tu_16": popularity_tu_16,
        "popularity_tu_17": popularity_tu_17,
        "popularity_tu_18": popularity_tu_18,
        "popularity_tu_19": popularity_tu_19,
        "popularity_tu_20": popularity_tu_20,
        "popularity_tu_21": popularity_tu_21,
        "popularity_tu_22": popularity_tu_22,
        "popularity_tu_23": popularity_tu_23,
        "popularity_wed_0": popularity_wed_0,
        "popularity_wed_1": popularity_wed_1,
        "popularity_wed_2": popularity_wed_2,
        "popularity_wed_3": popularity_wed_3,
        "popularity_wed_4": popularity_wed_4,
        "popularity_wed_5": popularity_wed_5,
        "popularity_wed_6": popularity_wed_6,
        "popularity_wed_7": popularity_wed_7,
        "popularity_wed_8": popularity_wed_8,
        "popularity_wed_9": popularity_wed_9,
        "popularity_wed_10": popularity_wed_10,
        "popularity_wed_11": popularity_wed_11,
        "popularity_wed_12": popularity_wed_12,
        "popularity_wed_13": popularity_wed_13,
        "popularity_wed_14": popularity_wed_14,
        "popularity_wed_15": popularity_wed_15,
        "popularity_wed_16": popularity_wed_16,
        "popularity_wed_17": popularity_wed_17,
        "popularity_wed_18": popularity_wed_18,
        "popularity_wed_19": popularity_wed_19,
        "popularity_wed_20": popularity_wed_20,
        "popularity_wed_21": popularity_wed_21,
        "popularity_wed_22": popularity_wed_22,
        "popularity_wed_23": popularity_wed_23,
        "popularity_th_0": popularity_th_0,
        "popularity_th_1": popularity_th_1,
        "popularity_th_2": popularity_th_2,
        "popularity_th_3": popularity_th_3,
        "popularity_th_4": popularity_th_4,
        "popularity_th_5": popularity_th_5,
        "popularity_th_6": popularity_th_6,
        "popularity_th_7": popularity_th_7,
        "popularity_th_8": popularity_th_8,
        "popularity_th_9": popularity_th_9,
        "popularity_th_10": popularity_th_10,
        "popularity_th_11": popularity_th_11,
        "popularity_th_12": popularity_th_12,
        "popularity_th_13": popularity_th_13,
        "popularity_th_14": popularity_th_14,
        "popularity_th_15": popularity_th_15,
        "popularity_th_16": popularity_th_16,
        "popularity_th_17": popularity_th_17,
        "popularity_th_18": popularity_th_18,
        "popularity_th_19": popularity_th_19,
        "popularity_th_20": popularity_th_20,
        "popularity_th_21": popularity_th_21,
        "popularity_th_22": popularity_th_22,
        "popularity_th_23": popularity_th_23,
        "popularity_fr_0": popularity_fr_0,
        "popularity_fr_1": popularity_fr_1,
        "popularity_fr_2": popularity_fr_2,
        "popularity_fr_3": popularity_fr_3,
        "popularity_fr_4": popularity_fr_4,
        "popularity_fr_5": popularity_fr_5,
        "popularity_fr_6": popularity_fr_6,
        "popularity_fr_7": popularity_fr_7,
        "popularity_fr_8": popularity_fr_8,
        "popularity_fr_9": popularity_fr_9,
        "popularity_fr_10": popularity_sat_10,
        "popularity_fr_11": popularity_sat_11,
        "popularity_fr_12": popularity_sat_12,
        "popularity_fr_13": popularity_sat_13,
        "popularity_fr_14": popularity_sat_14,
        "popularity_fr_15": popularity_sat_15,
        "popularity_fr_16": popularity_sat_16,
        "popularity_fr_17": popularity_sat_17,
        "popularity_fr_18": popularity_sat_18,
        "popularity_fr_19": popularity_sat_19,
        "popularity_fr_20": popularity_sat_20,
        "popularity_fr_21": popularity_sat_21,
        "popularity_fr_22": popularity_sat_22,
        "popularity_fr_23": popularity_sat_23,
        "popularity_sat_0": popularity_sat_0,
        "popularity_sat_1": popularity_sat_1,
        "popularity_sat_2": popularity_sat_2,
        "popularity_sat_3": popularity_sat_3,
        "popularity_sat_4": popularity_sat_4,
        "popularity_sat_5": popularity_sat_5,
        "popularity_sat_6": popularity_sat_6,
        "popularity_sat_7": popularity_sat_7,
        "popularity_sat_8": popularity_sat_8,
        "popularity_sat_9": popularity_sat_9,
        "popularity_sat_10": popularity_sat_10,
        "popularity_sat_11": popularity_sat_11,
        "popularity_sat_12": popularity_sat_12,
        "popularity_sat_13": popularity_sat_13,
        "popularity_sat_14": popularity_sat_14,
        "popularity_sat_15": popularity_sat_15,
        "popularity_sat_16": popularity_sat_16,
        "popularity_sat_17": popularity_sat_17,
        "popularity_sat_18": popularity_sat_18,
        "popularity_sat_19": popularity_sat_19,
        "popularity_sat_20": popularity_sat_20,
        "popularity_sat_21": popularity_sat_21,
        "popularity_sat_22": popularity_sat_22,
        "popularity_sat_23": popularity_sat_23,
        "popularity_su_0": popularity_su_0,
        "popularity_su_1": popularity_su_1,
        "popularity_su_2": popularity_su_2,
        "popularity_su_3": popularity_su_3,
        "popularity_su_4": popularity_su_4,
        "popularity_su_5": popularity_su_5,
        "popularity_su_6": popularity_su_6,
        "popularity_su_7": popularity_su_7,
        "popularity_su_8": popularity_su_8,
        "popularity_su_9": popularity_su_9,
        "popularity_su_10": popularity_su_10,
        "popularity_su_11": popularity_su_11,
        "popularity_su_12": popularity_su_12,
        "popularity_su_13": popularity_su_13,
        "popularity_su_14": popularity_su_14,
        "popularity_su_15": popularity_su_15,
        "popularity_su_16": popularity_su_16,
        "popularity_su_17": popularity_su_17,
        "popularity_su_18": popularity_su_18,
        "popularity_su_19": popularity_su_19,
        "popularity_su_20": popularity_su_20,
        "popularity_su_21": popularity_su_21,
        "popularity_su_22": popularity_su_22,
        "popularity_su_23": popularity_su_23,
        "time_spent_lo": time_spent_lo,
        "time_spent_hi": time_spent_hi}


df = pd.DataFrame(df_dict_1)
wd = ["mo","tu","wed","th","fr","sat","su"]
for item in entries:


    f = pickle.load(open(f"{adr}//{item}", "rb"))
    [city, typ, name, tstamp] = item.split("_")
    [tstamp, _] = tstamp.split(".")
    [day, month, year, hour, _, _] = tstamp.split("-")

    
    

momentan_popularity = []
for [index, entry] in df.iterrows():
	ts = entry["Timestamp"]
	[day, month, year, hour, _, _] = ts.split("-")
	weekday = wd[date(int(year), int(month), int(day)).weekday()]
	call = f"popularity_{weekday}_{int(hour)}"
	momentan_popularity.append(entry[call])



df.insert(9, "Average popularity", momentan_popularity)

df.to_csv("data.csv", encoding="latin-1")