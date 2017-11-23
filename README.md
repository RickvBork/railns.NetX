#Project: RailNL#
*@author Team Stellar Heuristiek*

Program that models railway network into a graph. Using this structure routes can are calculated with certain constraints. Routes are given a score depending on the number of critical conenctions that are driven. Here, a railline between two stations is defined as critical whenever at least of of the two stations is defined as critical. For this definition, a csv file is used. 
Route determining is done both by using a random walk and by random walk with certain restrictions and instructions, the latter leading to routes that score higher scores.
Scores are calculated in different ways. Usually they depend on P, which is fraction of critical railconnections between two station that is passed on by a train at least once in at least one direction. Other variables that are taken into account are the number of trains in a one service (usually varying from one to seven) and the total number of minutes these trains in one service need for their route.

###Structure###
The 'Graaf vis' map contains the results of visualisations. These are graphical displays of the railnetwork as well as barcharts from the scores of train services genereated by different algorithms.
The 'data' map contains the .csv data files containing the stations and connections of the railwaynetwork. These .csv files are used when creating the graph class.
The 'feedback' map contains notes that are made by the authors during the techassist hour with the techassist.
The 'line_creation' map contains the python files that model the graph and the functions used to generate paths and trainservices. There are explained in greater detail in the README within the directory.

###Motivation###
This projected was started as an assigment for the course Heuristieken at the University of Amsterdam.

