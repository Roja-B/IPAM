
To run a complete round of the algorithm, you need to 
i) Place the followng in one directory:
	- all the python code (*.py), R code (*.R), and the script files (*.sh)
	- the file PARAMETERS.py (modifed for the correct Path of current directory (PATH) and the correct parameters (START_YEAR, etc)) in one directory, 
	- the data file named: IPAM_Data.txt
	- the list of 'programs' to be omitted, named OMITList
	- the list of all resolved emails, named ResolvedEmails 
ii) In the command line in that same directory type: ./OneStep.sh
Results will be produced in the directory automatically created and named myResults

To only look at the communities of long programs (28 of them):
in step i above, add the file INCLUDEList to the directory (this is the list of long programs in upper case)
in step ii, instead of running OneStep.sh, type: ./LongProgs.sh

====================================================
Below is a more detailed description of steps that are taken and programs that are executed in the algorithm:
=====================================================
These two steps are not used here because they have been already done once:
00) create list of email addresses to be resolved
0) run source("bipartiteAnalysis.R") this produces degree distributions of programs and participants

-------
CREATE GRAPHS:

1) run python userProgramEdgelist.py 
(this program creates edgelists, it also automatically omits programs in the file OMITlist)
2) run python resolveEmails.py to resolve emails
3) run python divideTemporally.py to create temporally divided edgelists

with different PARAMETER values for window size and slide amount now we can do the following:

4) run python makeBipartite.py to create bipartite graphs with desired window size and sliding amount
5) run python projectGraph_programs.py to create unipartite graphs

-------
CREATE COMMUNITIES:
6) run ./step1.sh to execute  main_ipam.R and create communities per time

-------
CREATE PATHS:
7) find transition probabilities
run python transitionProbs_ipam.py 
8) run communityEvolution.py
9) run createComEvolutionNetwork.py
10) run CommunitySizesPath_ipam.py 

-------
VISUALIZE:
11) run layered_ipam.py 
