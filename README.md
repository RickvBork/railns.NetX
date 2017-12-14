# Project: RailNL
*@author Team Stellar Heuristiek*

One paragraph of project description goes here

Program that models railway network into a graph. Using this structure routes can are calculated with certain constraints. Routes are given a score depending on the number of critical conenctions that are driven. Here, a railline between two stations is defined as critical whenever at least of of the two stations is defined as critical. For this definition, a csv file is used. 
Route determining is done both by using a random walk and by random walk with certain restrictions and instructions, the latter leading to routes that score higher scores.
Scores are calculated in different ways. Usually they depend on P, which is fraction of critical railconnections between two station that is passed on by a train at least once in at least one direction. Other variables that are taken into account are the number of trains in a one service (usually varying from one to seven) and the total number of minutes these trains in one service need for their route.


## Getting started

TODO: These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

TODO: What things you need to install the software and how to install them.

'''
Give examples
'''

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

## Running the tests - ??????????

Explain how to run the automated tests for this system

### Break down into end to end tests - ??????????????

Explain what these tests test and why

```
Give an example
```

### And coding style tests - ?????????????????????/

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


oude readme, kan denk ik weg, hiervoor kijken mensen wel in de directory's zelf (moeten er niet ook readme's voor deze allemaal komen?)
### Structure ###
The 'visualization' map contains the results of visualisations. These are graphical displays of the railnetwork as well as barcharts from the scores of train services genereated by different algorithms.
The 'data' map contains the .csv data files containing the stations and connections of the railwaynetwork. These .csv files are used when creating the graph class.
The 'feedback' map contains notes that are made by the authors during the techassist hour with the techassist.
The 'line_creation' map contains the python files that model the graph and the functions used to generate paths and trainservices. There are explained in greater detail in the README within the directory.


