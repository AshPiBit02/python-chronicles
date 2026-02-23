# The "datetime" module is a built-in python module for handling dates and times in Python.
    # more powerful than time because it supports data arithmetic,formating, and parsing.
    # essential fro projects involving logs, scheduling, timestamps, or reports.

import datetime as dt

#current date and time
cur = dt.datetime.now()
formatted = cur.strftime("%d/%m/%Y %H:%M")
print("Current date and time:", formatted)

#current date or time only 
today=dt.date.today()
print("Today's date: ",today)

cur_time=dt.datetime.now().time()
print("TIme: ",cur_time)

#Creating custom date/time
custom_date=dt.date(2026,2,23)
print("Custom date: ",custom_date)

custom_time=dt.time(2,11,11)
print("Custom time: ",custom_time)

custome_date_time=dt.datetime(2026,2,3,7,30,44)
print(f"Custom date and time : {custome_date_time}")

# Date Arithmetic with timedelta
today=dt.date.today()
tomorrow = today + dt.timedelta(days=1)
yesterday=today - dt.timedelta(days=1)
print("Today: ",today)
print("Yesterday: ",yesterday)
print("Tomorrow: ",tomorrow)

# Formatting Dates (strftime)
cur_date_time=dt.datetime.now()
format=cur_date_time.strftime("%Y-%m-%d %H:%M:%S")
print(cur_date_time)

# Parsing Strings into Dates(strptime)
date_str="23-02-2026 18:10"
parsed=dt.datetime.strptime(date_str,"%d-%m-%Y %H:%M")
print(date_str)

# Essentail Operations Summary
    # datetime.datetime.now() - current date and time
    # datetime.date.today() - current date only
    # datetime.datetime(year,month,day,hour,minute,second) - custom datetime
    # datetime.datedelta(days=n) - add/subtract days(or seconds or microseconds)
    # .strftime(format) - format datetime into string
    # .strptime(string_date,format) - parse string into datetime.
