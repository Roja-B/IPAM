''' This program reads from ResolvedEmails and creates a hash table, then replaces all the relevant email entries in the EdgelistPlusDates '''

from PARAMETERS import *

f1 = open(DataPATH+'/ResolvedEmails',"r")
f2 = open(PATH+'/myIntermediateFiles/EdgeList',"r")
t = open(PATH+ '/myIntermediateFiles/EdgeList_resolved',"w")
resolved = dict()

for line in f1:
	emails = line.strip().split('\t')
	resolved[emails[1]] = emails[2]

f1.close()


for line in f2:
	elements = line.strip().split('\t')
	program = elements[0]
	email = elements[1]
	try: replaceEmail = resolved[email]
	except: replaceEmail = email
	t.write(program+'\t'+replaceEmail+'\n')

f2.close()
t.close()	
	
