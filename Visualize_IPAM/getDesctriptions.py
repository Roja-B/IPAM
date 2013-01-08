
'''Get descriptions of the programs in each community'''

from string import upper
NUMCOMS = 4
t = open("AllLongProgramList.txt","r")

Descriptions = dict()
for line in t:
	elements = line.strip().split('\t')
	programCode = upper(elements[1])
	programDesc = elements[2]
	Descriptions[programCode] = programDesc


for i in range(NUMCOMS):
	print "------------------------"
	try:f = open("myIntermediateFiles/community"+str(i),"r")
	except: continue
	for line in f: print line.strip(),Descriptions[line.strip()]
	f.close()


