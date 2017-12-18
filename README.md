# Project: RailNL
*@author Team Stellar Heuristiek \
Rick van der Bork - 11990503 \
Dimitri van Cappeleveen - 122 \
Thom Oosterhuis - 10893806*

This programm models railway networks into a graph. Tracks are calculated with certain constraints and are given a score depending on the number of critical connections that are traversed. Here, a railline between two stations is defined as critical whenever at least of of the two stations is defined as critical. For this definition, a csv file is used. 
Route determining is done by several algorithms. The score is calculated with the following formula:

Score = p \cdot 10000 - (t \cdot 20 + min/100000)

P is the percentage of critical connections traversed, t the number of tracks and m the total number of minutes of all the tracks combined.

## Motivation

This project is for the course Heuristieken, part of the Minor Programming, of the University of Amsterdam.

## Getting started

Download the project from the current git directory:
*https://github.com/RickvBork/railns.NetX.git*

Next, from the source directory, run the requirements.txt. See **Prerequisites**.

### Prerequisites

In the project source folder (Heuristieken) you will find the file requirements.txt. Next run the following command:

pip install -r requirements.txt

## Structure

* Data: Contains the .csv data files containing the stations and connections of the railwaynetwork. These .csv files are used when creating the graph class. It also contains some scores from the Hierholzer algorithm (see the folder line_creation) for experimentation.
* Feedback: This folder contains the feedback which we received, mainly during techassist (credits to Quinten van der Post) while we were working on this project.
* Line_creation: Contains the python files that model the graph and the functions used to generate paths and trainservices. There are explained in greater detail in the README within the directory. How to actually run the algorithms is also explained in the README file in this folder.
* Trash: The name says it all.
* Visualization: Contains the results of visualisations. These are graphical displays of the railnetwork as well as barcharts from the scores of train services genereated by different algorithms. It also contains a folder with histograms based on the results of the data of the Hierholzer experiments in the Data folder.

## Contributors

Since this is a school assignment, this project is not open for contributing.

## Acknowledgments

We are grateful to Quinten van der Post, Wouter Vrielink and everyone at our workgroup.

