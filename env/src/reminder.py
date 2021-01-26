import time
import datetime
import win10toast

# Function to make reminders
def getGivenTime(Rtime):
    present_time = datetime.datetime.now()
    minute = []
    merdian = []
    Rtime = Rtime.split(':')
    given_hour = Rtime[0]
    for i,j in enumerate(Rtime[1]):
        if j>='0' and j<= '9':
            minute.append(j)
        elif j>='a' and j<='z':
            merdian.append(j)
   
    given_minute = ''
    given_merdian = ''

    for i in minute:
        given_minute = given_minute + i
    for j in merdian:
        given_merdian = given_merdian + j
    
    present_hour = present_time.hour
    present_minute = present_time.minute
    if given_merdian == 'pm':
        present_hour = present_hour - 12
    
    
    remind_hour = int(given_hour) - present_hour
    remind_minute = int(given_minute) - present_minute
    remind_hour = remind_hour * 60 * 60
    remind_minute = remind_minute * 60
    remind_time = remind_hour + remind_minute
    return remind_time

def getTime(Rtime):
    Rtime = Rtime.replace("o'clock", "");
    return Rtime

def makeRemainderTime(Rtime):
    remind_time = ''
    if ':' in Rtime or 'p.m.' in Rtime or 'a.m.' in Rtime:
        remind_time = getGivenTime(Rtime)
    elif "o'clock" in Rtime:
        remind_time = getTime(Rtime)

    return remind_time
   

def makeRemainder(content,Rtime):
    remind_time = makeRemainderTime(Rtime)
    return 'reminder is set'
    time.sleep(remind_time)
    toaster = win10toast.ToastNotifier()
    toaster.show_toast('Virtual Assistant',content,duration = 10)
    

