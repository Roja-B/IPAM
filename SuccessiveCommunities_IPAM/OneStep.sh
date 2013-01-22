#!/bin/bash

mkdir myIntermediateFiles
mkdir myIntermediateFiles/Bipartite
mkdir myIntermediateFiles/Unipartite
mkdir myIntermediateFiles/Programs
mkdir myIntermediateFiles/TemporalGraphs
mkdir myRawData
mkdir myResults

cp IPAM_Data.txt myRawData/
cp Program_Mapping myRawData/
cp ResolvedEmails myRawData/
cp OMITlist myRawData/

python map_programs.py # to map sub-programs to their respective long programs
echo map_programs
python userProgramEdgelist_ipam.py # to create edgelists
echo userProgramEdgelist_ipam
python resolveEmails_ipam.py # to resolve emails
echo resolveEmails_ipam
python divideTemporally_ipam.py # to create temporally divided edgelists
echo divideTemporally_ipam
python makeBipartite_ipam.py # to create bipartite graphs with desired window size and sliding amount
echo makeBipartite_ipam
python projectGraph_programs_ipam.py # to create unipartite graphs
echo projectGraph_programs_ipam

bfilenames=$(ls myIntermediateFiles/Bipartite/)
ufilenames=$(ls myIntermediateFiles/Unipartite/)
pfilenames=$(ls myIntermediateFiles/Programs/)
for filename in $bfilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]")
        mkdir myResults/$dirname
        echo $dirname
        cp myIntermediateFiles/Bipartite/$filename myResults/$dirname/bipartite.txt
done
for filename in $ufilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]") # create directories named by year
        cp myIntermediateFiles/Unipartite/$filename myResults/$dirname/unipartite.txt
done
for filename in $pfilenames; do
        dirname=$(echo $filename | tr -dc "[:digit:]")
        echo $dirname
        cp myIntermediateFiles/Programs/$filename myResults/$dirname/ProgramSizes.txt
done
dnames=$(ls myResults/)
for dname in $dnames; do
        echo $dname
        cp *.R myResults/$dname/
        cd myResults/$dname/
        R --save < main_ipam.R
        cd ../.. 
done


python transitionProbs_ipam.py
python communityEvolution_ipam.py
python createComEvolutionNetwork_ipam.py
python CommunitySizesPath_ipam.py
python layered_ipam.py

rm -r myIntermediateFiles
rm -r myRawData
