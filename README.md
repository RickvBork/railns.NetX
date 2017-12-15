# Project: RailNL
*@author Team Stellar Heuristiek*

One paragraph of project description goes here

  Program that models railway networks into a graph. Tracks are calculated with certain constraints and are given a score depending on the number of critical conenctions that are covered. Here, a railline between two stations is defined as critical whenever at least of of the two stations is defined as critical. For this definition, a csv file is used. 
Route determining is done both by using a random walk and by random walk with certain restrictions and instructions, the latter leading to routes that score higher scores.

  Scores are calculated in different ways. Usually they depend on P, which is fraction of critical railconnections between two station that is passed on by a train at least once in at least one direction. Other variables that are taken into account are the number of trains in a one service (usually varying from one to seven) and the total number of minutes these trains in one service need for their route.


## Getting started

Download the project from the current git directory:
*https://github.com/RickvBork/railns.NetX.git

Next, from the source directory, run the requirements.txt. See **Prerequisites**.

### Prerequisites

Move to the directory where requirements.txt is located. It is located in the project source folder (Heuristieken). Next run the following command:

pip install -r requirements.txt

### Installing

TODO: A step by step series of examples that tell you have to get a development env running

Say what the step will be

'''
Give the example
'''

And repeat

'''
until finished
'''

End with an example of getting some data out of the system or using it for a little demo

## Running the algorithms

TODO:
User runs main.py
Console prints a choice to load csv file:
* Noord Holland 
* Netherlands

Next, the console prints a choice list of algorithms. Here, if applicable, the user can set:
*Maximum track number per service
*Maximum track length 
*number of iterations (e.g. for the random walk or hillclimber)
*plot service
*plot barchart (if applicable)

### Algorithms

Random Walk:
Randomly generates a track. No heuristics involved.

Hillclimber:
Uses a randomly generated service as a starting point. Then alters various dimensions of the service to 'climb' to higher scores.
Stops if the maximum number of iterations has been reached.

Hierholzer:
Fills the graph with tracks that, when combined, cover each edge once. Then using certain heuristics, tracks are coupled or shortened to improve the service score.

Depth First Seach (Not finished yet):
From a start node, it walks each valid track possible. Then results of other nodes are combined to form a service with the least number of comflicts and the highest possible coverage of critical tracks.

## Authors

* **Rick van Bork**, **Dimitri van Capelleveen** and **Thom Oosterhuis** *

## Acknowledgments

We are grateful to Quinten van der Post, Wouter Vrielink and everyone at our workgroup.


oude readme, kan denk ik weg, hiervoor kijken mensen wel in de directory's zelf (moeten er niet ook readme's voor deze allemaal komen?)
### Structure ###
The 'visualization' map contains the results of visualisations. These are graphical displays of the railnetwork as well as barcharts from the scores of train services genereated by different algorithms.
The 'data' map contains the .csv data files containing the stations and connections of the railwaynetwork. These .csv files are used when creating the graph class.
The 'feedback' map contains notes that are made by the authors during the techassist hour with the techassist.
The 'line_creation' map contains the python files that model the graph and the functions used to generate paths and trainservices. There are explained in greater detail in the README within the directory.


