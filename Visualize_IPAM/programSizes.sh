#!/bin/bash
prognames=$(more myIntermediateData/EdgeList_resolved)
echo $prognames
for progname in $prognames; do
	grep $progname myIntermediateFiles/EdgeList_resolved | wc -l
done


