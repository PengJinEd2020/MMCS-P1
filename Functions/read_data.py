import pandas as pd
import numpy as np

def read_file(file):
    data = pd.read_csv(file)
    return data

data = read_file('bikedata.csv')
data_in_array = data.values
data_in_array.shape

def howmanydays(data):
    date = data[['started_at', 'ended_at']].values
    daylist = []
    day = 0
    for i in range(date.shape[0]):
        daylist.append(date[i, 0][0:10])

    days = list(set(daylist))
    return len(days)

num_of_days = howmanydays(data)

def howmanystations(data):
    stations = data[['start_station_name', 'end_station_name']].values
    stationlist = []
    station = 0
    for i in range(stations.shape[0]):
        stationlist.append(stations[i, 0])

    station = list(set(stationlist))
    return len(station)

num_of_stations = howmanystations(data)

def  sortingdata(data):
    for i in
        data.loc[data.a>=2,'started_at'] = 'new_data'

def  get_daily_endpoint(data_in_array, which_day):
    # which_day type: '2019-10-01'
    data_thatday = data_in_array[]
    print(data_thatday.info())


get_daily_endpoint(data, '2019-10-01')



data
