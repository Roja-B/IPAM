#!/bin/bash

#mkdir myIntermediateFiles
#mkdir myRawData
#mkdir myResults

#cp IPAM_Data.txt myRawData/
#cp ResolvedEmails myRawData/
#cp INCLUDElist myRawData/

python userProgramEdgelist_ipam_vis.py # to create edgelists
echo userProgramEdgelist_ipam
python resolveEmails_ipam.py # to resolve emails
echo resolveEmails_ipam
python projectGraph_programs_ipam_vis.py # to create unipartite graphs
echo projectGraph_programs_ipam

cp *.R myIntermediateFiles/
cd myIntermediateFiles
R --save < main_ipam.R
cd ..

