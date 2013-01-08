# makes the file paths for word scores for a given "path" or "trajectory"

import sys
year = sys.argv[1]
com = sys.argv[2]
PATH = "/media/data3/roja/IPAM/myResults"
WINDOW = 3

filename = ''.join([PATH,'/',str(year),str(int(year)+WINDOW-1),'/community',str(com)])
f = open(filename,"r")
programs = []
for line in f:
	programs.append(line.strip())
f.close()

print programs
