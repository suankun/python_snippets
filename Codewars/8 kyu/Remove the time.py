# https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e/train/python
#
# Task Description
# You're re-designing a blog, and the blog's posts have the Weekday Month Day, time format for showing the date and time when a post was made, e.g., Friday May 2, 7pm.
#
# You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.
#
# Write a function that takes the website date/time in its original string format and returns the shortened format.
#
# Input
# Input will always be a string, e.g., "Friday May 2, 7pm".
#
# Output
# Output will be the shortened string, e.g., "Friday May 2".

def shorten_to_date(long_date):
    return long_date[:long_date.find(","):]


print(shorten_to_date("Monday February 2, 8pm")) # "Monday February 2"
print(shorten_to_date("Tuesday May 29, 8pm")) # "Tuesday May 29"
print(shorten_to_date("Wed September 1, 3am")) # "Wed September 1"
print(shorten_to_date("Friday May 2, 9am")) # "Friday May 2"
print(shorten_to_date("Tuesday January 29, 10pm")) # "Tuesday January 29"

# def shorten_to_date(long_date):
#     return long_date.split(',')[0]