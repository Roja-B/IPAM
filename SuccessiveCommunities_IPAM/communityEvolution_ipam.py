# This program takes matrices of transition probabilities (between two consecutive temporal windows) and creates lines where each line is a list of next most probably communities for each community at time ti.
import os
from PARAMETERS import *
#PATH = "/media/data3/roja/IPAM/myResults"
#SLIDE = 1 # years 
#WINDOW = 2 # years
#START_YEAR = 2000
#END_YEAR = 2013
def consecutiveComs(filename):
	try:f = open(filename, "r")
	except:
                print "could not find TransitionProbs", year
	nextComs = []
	maxprobs = []
	for line in f:
	        line = line.strip()
        	try: probs = [float(p) for p in (line.split('\t'))]
#		print probs
		except ValueError: probs = [0  for p in (line.split('\t'))] 
		m = max(probs)
		nextComs.append([i for i, j in enumerate(probs) if j == m])
		maxprobs.append(m)
	print nextComs
	print maxprobs
	return [maxprobs,nextComs]
t = open(PATH+"/myResults/ComEvolutions","w")
tt = open(PATH+"/myResults/Dates","w")
year = START_YEAR
while year <= END_YEAR+1-WINDOW:
        print year
	if MODE == "NORMAL":
	        filename = ''.join([PATH,"/myResults/",str(year),str(year+WINDOW-1),"/TransitionProbs"])
	elif MODE == "AGGREGATE":
		filename = ''.join([PATH,"/myResults/",str(START_YEAR),str(year+WINDOW-1),"/TransitionProbs"])
        print filename
	#[maxprobs,nextComs] = consecutiveComs(filename)
	try: [maxprobs,nextComs] = consecutiveComs(filename)
	except: 
		year += SLIDE
		continue
	t.write(str(year)+"\t")
	tt.write(str(year)+'\n')
	for i in range(len(nextComs)):
		t.write("("+str(i)+","+str(maxprobs[i])+","+str(nextComs[i])+")\t")
	t.write('\n')
	year += SLIDE
t.close()
tt.close()
