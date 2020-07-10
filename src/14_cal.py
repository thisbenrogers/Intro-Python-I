"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

today = datetime.today()

cal = calendar.Calendar()

length = len(sys.argv)
arguments = sys.argv

if length == 1:
    print(cal.monthdatescalendar(today.year, today.month)) # print calendar for this month
elif length == 2:
    print(cal.monthdatescalendar(today.year, int(arguments[1]))) # assume arg is month and print that month's calendar for this year
elif length == 3:
    print(cal.monthdatescalendar(int(arguments[2]), int(arguments[1]))) # print the requested calendar
else:
    print("This program requires two or fewer arguments, the first argument should be the month value and the second should be the year value for the calendar you wish to view")