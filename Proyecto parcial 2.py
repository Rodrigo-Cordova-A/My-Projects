# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 08:36:34 2023

@author: Rodrigo
"""
from datetime import datetime, timedelta
import numpy as np
import random

clients = list()
clientid = 1
timebetween = random.randint(0,6)
timesb = list()
hourarrivals = list()
timeactions = list()
hoursstart = list()
hoursend = list()
timeswaiting = list()
inactivity = list()
N = int(input('How many clients do you expect this day?\n'))
opening = datetime.strptime(input('When is the bank opening? (Use hh:mm format)\n'),'%H:%M')
first = random.randint(0,6)
timeaction = random.randint(0,6)
hourarrival = opening + timedelta(minutes=timebetween)
hourarrivals.append(hourarrival)
hourstart = hourarrival
hoursstart.append(hoursstart)
timeactions.append(timeaction)
timesb.append(timebetween)
inactive = timedelta(minutes=0)
inactivity.append(inactive)
hourend = hourstart + timedelta(minutes=timeaction)
hoursend.append(hourend)
timewait = timedelta(minutes=0)
timeswaiting.append(timewait)
sumwaits = list()
suminactive = list()
clientwait = 0
print('clientid  Time between Hour arrival Time action Time start  Time end Time wait Time inactive ', )
print(clientid,'             ',timebetween,'         ',("%s:%s" % (hourarrival.hour,hourarrival.minute)),'         ', timeaction, '       ',("%s:%s" % (hourstart.hour,hourstart.minute)),'    ', ("%s:%s" % (hourend.hour,hourend.minute)),'   ', timewait,'   ', inactive )

while clientid < N:
    clients.append(clientid)
    clientid = clientid + 1
    timesb.append(timebetween)
    hourarrival = hourarrival + timedelta(minutes=timebetween)
    hourarrivals.append(hourarrival)
    timewait = hourend - hourarrival  
    if timewait < timedelta(minutes=0):
        timewait = timedelta(minutes=0)
    timeswaiting.append(timewait)
    timebetween = random.randint(0,12)
    if hourend < hourarrival:
        hourstart = hourarrival
    else:
        hourstart = hourend
    hoursstart.append(hoursstart)
    inactive = hourstart - hourend
    if timewait > timedelta(minutes=0):
        clientwait = clientwait +1
    inactivity.append(inactive)
    timeaction = random.randint(1,8)
    timeactions.append(timeaction)
    hourend = hourstart + timedelta(minutes=timeaction)
    hoursend.append(hourend)
    print(clientid,'             ',timebetween,'         ',("%s:%s" % (hourarrival.hour,hourarrival.minute)),'        ', timeaction, '       ',("%s:%s" % (hourstart.hour,hourstart.minute)),'   ', ("%s:%s" % (hourend.hour,hourend.minute)),'   ', timewait,'   ', inactive )
for wait in timeswaiting:
    minutes = float("%s" % (wait.seconds))/60
    sumwaits.append(minutes)
print('\nThe total time waited was',sum(sumwaits))
for inac in inactivity:
    minute = float("%s" % (inac.seconds))/60
    suminactive.append(minute)
print('The total time inactive was',sum(suminactive))
print('The average time it took for the clients to complete their actions was',sum(timeactions)/N)
print('The average waiting time was',round(sum(sumwaits)/N,2))
print('The probability a client will wait is',round(clientwait/N,2)*100,'%')
totaltime= hourend-opening
total_minutes = float("%s" % (totaltime.seconds))/60
print('The percentage of inactivity was',round((((sum(suminactive))/total_minutes)*100),2),'%')
    
    

    