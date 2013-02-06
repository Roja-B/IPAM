
'''Get descriptions of the programs in each community'''
DataFilename = "IPAM_Data.txt"
ResultsDir = "myResults/20002012"
NUMCOMS = 7


from string import upper
t = open(DataFilename,"r")

Descriptions = dict()
for line in t:
	elements = line.strip().split('\t')
	programCode = upper(elements[0])
	try: programDesc = elements[1]
	except: 
		print line
		continue
	Descriptions[programCode] = programDesc
t.close()

print len(Descriptions)

for i in range(NUMCOMS):
	print "------------------------"
	try:f = open(ResultsDir+"/community"+str(i),"r")
	except: continue
	t = open(ResultsDir+"/Description_community"+str(i),"w")
	for line in f: t.write(line.strip()+'\t'+Descriptions[line.strip()]+'\n')
	f.close()
	t.close()


