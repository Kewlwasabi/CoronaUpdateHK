import requests
import json
import numpy as np
import matplotlib.pyplot as plt
import mymail
from datetime import datetime

def main():
    district_api = "https://api.data.gov.hk/v2/filter?q=%7B%22resource%22%3A%22http%3A%2F%2Fwww.chp.gov.hk%2Ffiles%2Fmisc%2Fbuilding_list_eng.csv%22%2C%22section%22%3A1%2C%22format%22%3A%22json%22%7D"
    response = requests.get(district_api)
    json_obj = response.json()
    data = np.array(json_obj)
    mymail.smtp_gmail("Corona Update: " + str(datetime.date(datetime.now())), get_Eastern_updates(data))

def get_districts_list(data):
    temp = []
    for obj in data:
        temp.append(obj['District'])
    
    return temp


def get_districts_dict(data):
    freq = dict.fromkeys(get_districts_list(data), 0)

    for obj in data:
        freq[obj['District']] = freq[obj['District']] + 1

    return freq

def dict_to_freq(dict):
    temp = []

    for key in dict:
        temp.append(dict[key])
    
    return temp

def get_Eastern_updates(data):
    temp = 'Please stay away from the following locations: \n'
    for obj in data:
        if obj['District'] == 'Eastern':
            building = obj['Building name']
            if "Taikoo Shing" in building or "Sai Wan Ho" in building or "North Point" in building:
                temp = temp + building + '\n'
    return temp

main()
