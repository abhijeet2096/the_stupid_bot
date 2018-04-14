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
#print(out)

# writer = csv.writer(open("output_M.csv", "wb"))
for row in out:
    print(row)

# with open("output_M.csv", 'w') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(out)

#np.savetxt('output_M.csv', np.asarray(out) , delimiter=',')

with open('output_M.csv','w') as out1:
    csv_out=csv.writer(out1)
    #csv_out.writerow(out[0])
    for row in out:
        if(row!=out[0]):
            csv_out.writerow(row)
