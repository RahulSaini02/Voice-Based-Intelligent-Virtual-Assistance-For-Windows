import datetime
import calendar

# A function to know the Time
def getTime():
    now = datetime.datetime.now()
    meridiem = ''
    if now.hour >= 12 :
        meridiem = 'p.m'
        hour = now.hour - 12
    else:
        meridiem = 'a.m'
        hour = now.hour
    # Convert minute to string

    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)

    return 'It\'s '+str(hour)+ ':'+minute+ ' '+meridiem

