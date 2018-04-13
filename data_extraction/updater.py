import time
import sys
import csv
import numpy as np


r  = csv.reader(open("output.csv"))
lines = list(r)


def valid(t):
    spt = t.split(' ')
    if len(spt) >= 2:
        if spt[1] == 'a.m.' or spt[1] == 'p.m.':
            return True
        else:
            return False
    else:
        return False

out = []
for line in lines:

    times = [line[2], line[3], line[4], line[5]]

    for i,t in enumerate(times):
        if valid(t):
            vt = t.split(' ')

            if vt[1] == 'p.m.':
                bct = vt[0] + ' PM'
            else:
                bct = vt[0] + ' AM'
            strt = time.strptime(bct, '%I:%M %p')
            line[2+i] = time.strftime('%H:%M', strt)

    out.append(line)
# print out