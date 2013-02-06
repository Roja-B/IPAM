

# Unipartite Projection 
# Creates Unipartite graph using Jaccard Index from a bipartite graph 
# Input: Bipartite Graph
# 	Form: "EdgeList"

import sys
from string import lower,upper
from PARAMETERS import *
bgraphname = PATH+"/myResults/20002012/bipartite.txt"
f1 = open(bgraphname,"r")
Participants = dict()
for line in f1:
	L1 = line.strip().split("\t")
	program = upper(L1[0])
	participant = L1[1]
	try: Participants[program].add(participant)
	except KeyError:
		Participants[program] = set()
		Participants[program].add(participant)
f1.close()

print "IPAM data has been loaded."
Answer = raw_input('Would you like to see participant overlaps between two programs? Enter y or n: ')
while Answer == 'y':
	prog1 = raw_input('Enter first program: ')
	prog2 = raw_input('Enter second program: ')
	CommonParticipants = set.intersection(Participants[upper(prog1)],Participants[upper(prog2)])
	print "People who participated in both programs are as follows:"
	print list(CommonParticipants)
	Answer = raw_input('Enter y if you want to enter two other programs, otherwise press any key: ')


