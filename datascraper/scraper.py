"""
API DOCUMENTATION
max = number of results. Guests are only allowed 100_000
type = type of trade. C for commodity
freq = A for annual
px = Classification code. We use Harmonized System so it's HS
ps = Duration. Right now, we are using past five years.
r = Reporter ID. For US it's 842. See the accompanying reporter and partner file
p = Partner ID. ALL signifies all partners.
rg = Import or Export (We want Imports i.e. 1)
CC = classification. 27 for petroleums
fmt = Format. We are using csv right now.
"""
import requests
import json
import time
import os
from tqdm import tqdm

countries = json.load(open("country_codes.json", "r"))      # list of countries and their codes used by COMTRADE
HS_CODE = 27        # For petroleum
years = '%2C'.join(['2021', '2020', '2019', '2018', '2017'])
years2 = '%2C'.join(['2016', '2015', '2014', '2013', '2012'])

api = "/api/get?max=100000&type=C&freq=A&px=HS&ps={years}&r={reporter_id}&p=all&rg=1&cc={HS_CODE}&fmt=csv"
api = 'https://comtrade.un.org' + api
folder = "data/"
if not os.path.exists(folder):
    os.mkdir(folder)

def get_csv(years, country):
    api_country = api.format(years=years, reporter_id=countries[country], HS_CODE=HS_CODE)
    r = requests.get(api_country)
    # try and see if the api succeeded.
    assert r.status_code == 200
    csv = r.text.replace('\r\n', '\n')
    assert "Classification,Year" in csv  # assert that we collected good data
    return csv

for country in tqdm(countries):
    # check if data already exists. If so, ignore
    filename = folder+country+".csv"
    if os.path.exists(filename):
        print (f"File for {country} already exists. The filesize is {os.path.getsize(filename)}")
        continue
    try:
        # All years from 2017-2021
        csv = get_csv(years, country)
        # time.sleep(40)
        # All years from 2012-2016
        csv2 = get_csv(years2, country)
        csv_all = csv + csv2.partition('\n')[2]     #discard the header of second and merge
        open(filename, "w").write(csv_all)
        # time.sleep(40)
    except AssertionError:
        print(f"{country}'s data couldn't be downloaded.")
        exit()
