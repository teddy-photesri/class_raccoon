'''
Lab 21: Rain Data
Version 1

The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland,
and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Download one of these files and write a function to load the file.
The two columns that are most important are the date and the daily total.
The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries,
or a list of instances of a custom class.

To parse the dates, use datetime.strptime.
This allows for easy access to the year, month, and day as ints.
Below I've shown how to parse an example string, resulting in a datetime object.
We can then access the year, month, and day on that datetime as ints. Later,
if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
'''

import requests
import re
import datetime

def get_file():
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
    page_source = response.text
    rain_file = re.findall(r'(\d{2}-\w+-\d{4})\s+(\d+)', page_source)
    return rain_file

def parse_data(str):
    date_data = datetime.datetime.strptime(str, '%d-%b-%Y')
    return date_data

rain_file = get_file() # list of tuples
rain_tuple = []

print(get_file())
print('*'*40)
print(parse_data('25-MAR-2016'))
print()

for i in range(len(rain_file)):
    date = parse_data(rain_file[i][0])
    daily_total = int(rain_file[i][1])
    rain_tuple = [(date, daily_total)]
    print(rain_tuple)




# print(parse_date())

# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
