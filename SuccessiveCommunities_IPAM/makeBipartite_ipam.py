# This program creates bipartite graphs of programs and participants using the desired window size and slide amount 
# Roja Bandari
# September 2012
# parameters
#SLIDE = 1 # in years
#PATH = "/media/data3/roja/IPAM"
#START_YEAR = 2000
#END_YEAR = 2013

from PARAMETERS import *

t = open(PATH+"/myIntermediateFiles/BipartiteNamesAndPaths","w")
# make bipartite graphs using the data from each year
year = START_YEAR
while year <= END_YEAR+1-WINDOW:
	print year
	if MODE == "NORMAL":
	        bgraphname = PATH+"/myIntermediateFiles/Bipartite/Bipartite"+'_'+str(year)+'_'+str(year+WINDOW-1)
	# to aggregate from start year:
	elif MODE == "AGGREGATE":
		bgraphname = PATH+"/myIntermediateFiles/Bipartite/Bipartite"+'_'+str(START_YEAR)+'_'+str(year+WINDOW-1)
	t.write(bgraphname+"\n")
	tt = open(bgraphname,"w")
#        if MODE == "NORMAL": 
	#for n in range(year,year+WINDOW):
	# to aggregate from start year:
#	elif MODE == "AGGREGATE":
	for n in range(START_YEAR,year+WINDOW):
		f = open(PATH+"/myIntermediateFiles/TemporalGraphs/EdgeList"+str(n),"r")
		for line in f: tt.write(line)
		f.close()
	tt.close()
	year += SLIDE
t.close()
