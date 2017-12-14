
# Line_creation
*@author Team Stellar Heuristiek*

This file contains 

van oude readme;
The 'line_creation' map contains the python files that model the graph and the functions used to generate paths and trainservices. There are explained in greater detail in the README within the directory.
This directory contains the .py files that model a railnetwork using a graph and that create trainservices consisting of multiply trains driving on a traject for a specified amount of time. 

The *helpers* contains functions that are used by other functions. Score functions to calculate a score for a trainservice are defined in here.

The *line_algorithms* file contains the algorithms that will generate a route for several train constructing together a trainservice. 
An example is the random_walk function. This function takes a instantion of the Graph class and a integer iterator. A random station from the network will be chosen as starting station for a train. After that, one of the stattions neigbors will be choses as the the next destination for the train. Keeping track of the time the train uses to get from the beginning station to the next stations, the train will stop riding after the amount of time exceeds the variable random_time. If the number of trains is lower then random_tracks, a new train will start riding from a new random station as described. When the number of trains equals random_tracks, a trainservice consisting of these train routes is created. The score of this trainservice is then calculated. The whole process of generating a trainservice is then repeated an *iterator* number of times.
Finally the function returns two lists of two different scores of all the trainservices as well as a dictionary containing the five tracks with the best s_score.

The Hierholzer Algorithm
Finally the *Hierholzer* algorithm creates an amount of services determined by the user via the iterator variable. For each service it creates, it creates as much tracks as needed to traverse all connections, unless the amount of tracks exceeds the maximum amount of tracks allowed. For each of these tracks, a random starting point is chosen, however, the starting station should have, if possible, only one available connection. After that all the other station in the track are also chosen randomly, provided that the connection between the stations is not traversed yet, also not by another track. If a station does not have a connection that is untraversed, the track ends, and a new starting station is chosen, again one with only one untraversed connection if possible. After the tracks have been made, there is some optimization: if two tracks have the same starting station, or the same starting and ending station (the same ending and ending station doesn't occur, since in that case the first laid track needs to stop with a station that still has untraversed connections), and if the time of these two tracks combined doesn't exceed the maximum track time, these two tracks will be combined to form a new track.

The *line_graph_class* file contains the code class with the structure of the Graph. A Graph consists of a graph, defined using networkX. Also a Graph has a name, a list of critical stations, the number of critical edges and the minimal_edge_weight, representing the shortest distance between two stations in minutes.
The *main* contains the code that initialises a Graph and then calls functions on it to generate trainservices. The scores of these trainservices are returned and are passed to a barchar function that gives a graphical visualisation of the scores of the different trainservices.

ref: https://gist.github.com/jxson/1784669

......................................





## Running the algorithms

Main.py sis used to run the different algorithms. In the case of 

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






