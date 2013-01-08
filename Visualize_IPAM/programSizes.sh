#!/bin/bash

prognames=$(more myRawData/INCLUDElist)
echo $prognames
for progname in $prognames; do
	grep $progname myIntermediateFiles/EdgeList_resolved | wc -l
done


