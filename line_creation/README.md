
# Line_creation
*@author Team Stellar Heuristiek
Rick van der Bork - 11990503
Dimitri van Cappeleveen - 12017485
Thom Oosterhuis - 10893806*

This folder contains all the code necessary for running the algorithms. It contains the .py files that model a railnetwork using a graph and that create trainservices consisting of multiply trains driving on a traject for a specified amount of time. 
More specifically, this folder contains the folders algorithms and the folder classes. Furthermore it contains the files analysis.py, helpers.py and main.py. All the files contain docstrings and comments to explain their content in more detail than given below.

## Algorithms folder

This folder contains, as the name suggests, our algorithms:

* Random Walk:
Randomly generates a track. No heuristics involved.

Hillclimber:
Uses a randomly generated service as a starting point. Then alters various dimensions of the service to 'climb' to higher scores.
Stops if the maximum number of iterations has been reached.

Hierholzer:
Fills the graph with tracks that, when combined, cover each edge once. Then using certain heuristics, tracks are coupled or shortened to improve the service score.

Depth First Seach (Not finished yet):
From a start node, it walks each valid track possible. Then results of other nodes are combined to form a service with the least number of comflicts and the highest possible coverage of critical tracks.

### Running the algorithms

Main.py sis used to run the different algorithms. In the case 

## Classes folder

This folder contains the classes that model:
 * 1. The graph class that models a railnetwork
 * 2. The node class that models a node, i.e. the connection between two single stations 
 * 3. The service class that models a train service (nl: 'lijnvoering') which consists of several tracks driven by several trains
 * 4. The track class that models the route of a single train. 
All these classes contain relevant information such as the time a train takes for its route, the critical edges a train rides during the route etc.

## Analysis

## Helpers

This python file contains functions that are used by the algorithms. 

## Main

This python file is used to run the algorithms.





The *line_graph_class* file contains the code class with the structure of the Graph. A Graph consists of a graph, defined using networkX. Also a Graph has a name, a list of critical stations, the number of critical edges and the minimal_edge_weight, representing the shortest distance between two stations in minutes.
The *main* contains the code that initialises a Graph and then calls functions on it to generate trainservices. The scores of these trainservices are returned and are passed to a barchar function that gives a graphical visualisation of the scores of the different trainservices.

ref: https://gist.github.com/jxson/1784669

of 

### Break down into end to end tests - ????????????????

Explain what these tests test and why

```
Give an example
```

### And coding style tests - ????????????????????

Explain what these tests test and why

```
Give an example
```

## Deployment - ?????????????????

Add additional notes about how to deploy this on a live system

## Built With - ??????????????????

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Versioning - ??????????????????

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Rick van Bork**, **Dimitri van Capelleveen** and **Thom Oosterhuis** *

## Acknowledgments

We are grateful to Quinten van der Post, Wouter Vrielink and everyone at our workgroup.






