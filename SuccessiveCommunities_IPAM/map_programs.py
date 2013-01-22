''' This program maps program names in IPAM_Data.txt to their respective mapping as specified in Program_Mapping'''

from PARAMETERS import *
from string import upper
def mappingTable():
	Map = dict()
	f1 = open(DataPATH+"/Program_Mapping","r")
	for line in f1:
		elements = line.strip().split("\t")
		prog_id = elements[0].upper().replace(":","")
		mapping = elements[1].upper()
		Map[prog_id] = mapping
	f1.close()
	return Map

f = open(DataPATH+"/IPAM_Data.txt","r")
t = open(DataPATH+"/Mapped_Data.txt","w")

M = mappingTable()
for line in f:
	line = line.strip()
	elements = line.split('\t')
	#prog = line.split('\t')[0]
	prog = elements[0].upper()
	try: mapping = M[prog]
	except:
#		print prog
		continue 
	if mapping == "EXCLUDE": continue
	elif mapping == "KEEP": i=0 # do nothing
	else: elements[0] = mapping
	for element in elements: t.write(element+"\t")
	t.write('\n')

f.close()
t.close()

