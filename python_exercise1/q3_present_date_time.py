"""
3. Write a Python program to display the current date and time.

"""
import datetime
now=datetime.datetime.now()
print("current date and time:\n",now.strftime("%Y/%m/%d-%H:%M:%S"))
"""
%Y-year
%m-month
%d-date
%H-hours
%M-minutes
%S-seconfs


"""