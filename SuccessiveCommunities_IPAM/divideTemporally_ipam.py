''' This program divides the data in EdgeListPlusDates_resolved into separate files named according to year (e.g. Edgelist2005)'''

from PARAMETERS import *

f = open(PATH+'/myIntermediateFiles/EdgeListPlusDates_resolved',"r")

temporal = dict()
year = START_YEAR
for year in range(START_YEAR,END_YEAR+1):
	temporal[str(year)] = []

for line in f:
	elements = line.strip().split('\t')
	program = elements[0]
	year = elements[1]
	email = elements[2]
	temporal[year].append(program+'\t'+email+'\n')
f.close()


for year in range(START_YEAR,END_YEAR+1):
	t = open(PATH+'/myIntermediateFiles/TemporalGraphs/EdgeList'+str(year),"w")
	for item in temporal[str(year)]:
		t.write(item)
	t.close()


