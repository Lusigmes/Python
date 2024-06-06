import datetime
import pytz
# https://pynative.com/list-all-timezones-in-python/
dataCC = datetime.datetime.now(
    pytz.timezone(zone="America/Chicago"))
dataSP = datetime.datetime.now(
    pytz.timezone(zone="America/Sao_Paulo"))
print("Chicago:", dataCC)     
print("São Paulo:", dataSP)     

#python -m venv .venv
#.venv\Scrips\activate .venv\bin\activate