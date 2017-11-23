### Synopsis ###
This directory contains the .py files that model a railnetwork using a graph and that create trainservices consisting of multiply trains driving on a traject for a specified amount of time. 

The *helpers* contains functions that are used by other functions. Score functions to calculate a score for a trainservice are defined in here.

The *line_algorithms* file contains the algorithms that will generate a route for several train constructing together a trainservice. 
An example is the random_walk function. This function takes a instantion of the Graph class and a integer iterator. A random station from the network will be chosen as starting station for a train. After that, one of the stattions neigbors will be choses as the the next destination for the train. Keeping track of the time the train uses to get from the beginning station to the next stations, the train will stop riding after the amount of time exceeds the variable random_time. If the number of trains is lower then random_tracks, a new train will start riding from a new random station as described. When the number of trains equals random_tracks, a trainservice consisting of these train routes is created. The score of this trainservice is then calculated. The whole process of generating a trainservice is then repeated an *iterator* number of times.
Finally the function returns two lists of two different scores of all the trainservices as well as a dictionary containing the five tracks with the best s_score.

The *line_graph_class* file contains the code class with the structure of the Graph. A Graph consists of a graph, defined using networkX. Also a Graph has a name, a list of critical stations, the number of critical edges and the minimal_edge_weight, representing the shortest distance between two stations in minutes.
The *main* contains the code that initialises a Graph and then calls functions on it to generate trainservices. The scores of these trainservices are returned and are passed to a barchar function that gives a graphical visualisation of the scores of the different trainservices.

ref:

