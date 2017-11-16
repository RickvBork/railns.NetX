+++Project: RailNL
@author Team Stellar Heuristiek

Program that models railway network into a graph. Using this structure routes can are calculated with certain constraints. Routes are given a score depending on the number of critical conenctions that are driven. Here, a railline between two stations is defined as critical whenever at least of of the two stations is defined as critical. For this definition, a csv file is used. 
Route determining is done both by using a random walk and by random walk with certain restrictions and instructions, the lather leading to routes that score higher scores.
