# This program reads from IPAM_Date.txt and creates a table of programs, dates, and participant emails (EdgeListPlusDates)
# It also excludes the programs that are in the OMITlist
#PATH = "/media/data3/roja/IPAM/myIntermediateFiles"
#DataPATH = "/media/data3/roja/IPAM/myRawData"
#START_YEAR = 2000
#END_YEAR = 2013

from PARAMETERS import *
from string import upper
#OmitEmails = {"rcaflisch@ipam.ucla.edu"}

#OmitEmails = []
f = open(DataPATH+"/IPAM_Data.txt","r")
t = open(PATH+"/myIntermediateFiles/EdgeList","w")
#OMIT = open(DataPATH+"/OMITlist").read()
INCLUDE = open(DataPATH+"/INCLUDElist").read().split('\n')
#print INCLUDE


programs = dict()
for year in range(START_YEAR,END_YEAR+1):
	programs[year] = set()
for line in f:
	line = line.strip()
	programID = upper(line.split('\t')[0])
#	if programID[0:3] in OMIT: 
#		print "program omitted:",programID
#		continue
	if programID not in INCLUDE: continue
	try: 
		email = line.split('\t')[6]
		try: email = email.split(",")[0]
		except: print "." 
		if email in OmitEmails: continue
		programYear = line.split('\t')[2].split('-')[0]
	except:
		print line
		continue
	programs[int(programYear)].add(programID)
	t.write(programID+'\t'+email+'\n')
#print programs
f.close()
t.close()
