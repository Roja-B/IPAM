#!/bin/bash
# this is for creating the paths
python communityEvolution.py
Num=40
while [ $i -lt $Num ]; do
        python communityEvolutionPaths.py $i
#       python CommunityTopicBalatarin.py $i 
        i=$((i + 5))
        echo $i
done

# python communityEvolutionPathsTopics.py to get a list of topics for each community on the path of community evolutions


