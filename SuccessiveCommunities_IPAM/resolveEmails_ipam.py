''' This program reads from ResolvedEmails and creates a hash table, then replaces all the relevant email entries in the EdgelistPlusDates '''

from PARAMETERS import *

f1 = open(DataPATH+'/ResolvedEmails',"r")
f2 = open(PATH+'/myIntermediateFiles/EdgeListPlusDates',"r")
t = open(PATH+ '/myIntermediateFiles/EdgeListPlusDates_resolved',"w")
resolved = dict()

for line in f1:
	emails = line.strip().split('\t')
	resolved[emails[1]] = emails[2]

f1.close()


for line in f2:
	elements = line.strip().split('\t')
	program = elements[0]
	year = elements[1]
	email = elements[2]
	try: replaceEmail = resolved[email]
	except: replaceEmail = email
	t.write(program+'\t'+year+'\t'+replaceEmail+'\n')

f2.close()
t.close()	
	
