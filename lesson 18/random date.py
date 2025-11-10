import random
import time

def randomdate(startdate,enddate):
    randomgenerator =  random.random()
    dateformat ="%m/%d/%Y"

    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))

    randomtime = starttime + randomgenerator*(endtime - starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print(randomdate("4/9/2022","1/4/2030"))