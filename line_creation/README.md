
# Line_creation
*@author Team Stellar Heuristiek \
Rick van der Bork - 11990503 \
Dimitri van Cappeleveen - 12017485 \
Thom Oosterhuis - 10893806*

This directory contains all the code necessary for running the algorithms. It contains the .py files that model a railnetwork using a graph and that create trainservices consisting of multiple trains driving on a traject for a specified amount of time. More specifically, this directory contains the directories algorithms and the directory classes, and it contains the files analysis.py, helpers.py and main.py. Below some description of these directories and files is given, but all the files contain docstrings and comments to explain their content in more detail.

## Algorithms directory

This directory contains, as the name suggests, our algorithms (for a description on how to actually run the algorithms, see Main below):

* Hierholzer: Fills the graph with tracks that, when combined, cover each edge once. Then using certain heuristics, tracks are coupled or shortened to improve the service score.
* Hillclimber: Uses a randomly generated service as a starting point. Then alters various dimensions of the service to 'climb' to higher scores. Stops if the maximum number of iterations has been reached.
	* Hillclimber helper: Helper file which contains functions specifically for the Hillclimber
	* Hillclimber Simulated Annealing: TODO.
* Random Walk: Randomly generates a track. No heuristics involved.
* Smart Random Walk: A variation of the Random Walk, with some heuristics: TODO.
* Depth First Seach (Not finished yet): TODO - From a start node, it walks each valid track possible. Then results of other nodes are combined to form a service with the least number of comflicts and the highest possible coverage of critical tracks.

## Classes directory

This directory contains several classes used by the algorithms:

 * The Graph class: This models a railnetwork, using Networkx.
 * The Node class: Models a node, i.e. the connection between two single stations.
 * The Service class: Models a train service (nl: 'lijnvoering') which consists of several tracks (objects of the class described below) driven by several trains. Objects of this class are returned when the algorithms are finished.
 * The Track class: Models the route of a single train.

All of these classes contain relevant information such as the time a train takes for its route, the critical edges a train rides during the route etc.

## Analysis

TODO

## Helpers

This python file contains functions used by the algorithms.

## Main

This python file is used to run the algorithms. After you run main.py, you will be asked to:
Please select the files you want to load, and you will be given two options: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. North Holland \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Netherlands \
After you choose either 1 or 2, specific .csv files will be loaded, and Networkx will be used to generate specific graphs. Now, you can choose which of the algorithms you would like to run: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1. Random Walk \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2. Smart Random Walk \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3. Hierholzer \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4. Hillclimber \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5. Hillclimber with Simulated Annealing \
After an algorithm is chosen, TODO

## Built With

* [Networkx](https://networkx.github.io) - Used to generate the graphs.
TODO?




