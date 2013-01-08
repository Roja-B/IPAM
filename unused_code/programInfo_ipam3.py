# This program creates a hash table of programs and their descriptions and participants
from PARAMETERS import PATH
f = open(PATH+"/myRawData/IPAM_Data.txt","r")
t = open(PATH+"/myRawData/ProgramInformation","w")
tt = open(PATH+"/myRawData/ProgramInformation_emails","w")

ProgramDescriptions = dict()
ProgramParticipants = dict()
ProgramParticipantEmails = dict()

for line in f:
	L = line.strip().split('\t')
	programID = L[0]
	try: description = L[1]
	except: 
		print "misformed line in data:", line
		continue
	email = L[6]
	participant = '_'.join(L[3:5])
	ProgramDescriptions[programID] = description
	try: 
		ProgramParticipants[programID].add(participant)
                ProgramParticipantEmails[programID].add(email)
	except KeyError: 
		ProgramParticipants[programID] = set()
		ProgramParticipants[programID].add(participant)
		ProgramParticipantEmails[programID] = set()
                ProgramParticipantEmails[programID].add(email)
for programID in ProgramDescriptions:
	participants = ','.join(ProgramParticipants[programID])
	emails = ','.join(ProgramParticipantEmails[programID]) 
	line_names = ''.join([programID,'\t',ProgramDescriptions[programID],'\t',participants,'\n'])
	line_emais = ''.join([programID,'\t',ProgramDescriptions[programID],'\t',emails,'\n'])
	t.write(line)
	tt.write(line)
f.close()
t.close()
tt.close()
