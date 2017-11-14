'''
Random walk on rails
'''

import Graph
import csv
import random
import networkx

# FILE: Graph.py
# Python v27
# 
# This file loads in stations and tracks from two csv files.
# It then seperates them in critical and non critical stations and edges, and stored in lists.
# These are used by NetworkX to plot the graph with the important data.
# By seperating stations and tracks into categories, different colors can be used to distinguish
# between them.

import csv
import networkx as nx
import pylab as py
import random

critical_stations = []

# define G
G = nx.Graph()

# read in stations from csv and put each station as node in graph
with open('csv_files/StationsHolland.csv') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in stations:

        if row[3] == "Kritiek":
            critical_stations.append(row[0])
            G.add_node(row[0],
                pos = (float(row[2]), float(row[1])),
                label = str(row[0]))
        else:
            G.add_node(row[0], 
                pos = (float(row[2]), float(row[1])),
                label = str(row[0]))

critical_neighbours = []

# add connections between nodes (=stations) into graph
with open('csv_files/ConnectiesHolland.csv') as csvfile:
    stations = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in stations:
        if row[0] and row[1] in critical_stations:
            # both are critical, color edge red
            G.add_edge(row[0], row[1], weight=int(row[2]))

        elif row[0] or row[1] in critical_stations:
            # one is a critical station, color edge blue
            G.add_edge(row[0], row[1], weight=int(row[2]))

        else:
            # neither is critical, color edge black
            G.add_edge(row[0], row[1], weight=int(row[2]))
            
'''
determine critical connections and make list
'''
critical_lines = 0
critical_connections = []
for v in G:
    print v
    for w in G[v]:
        print w
        vid = v
        wid = w
        #print(w)
        #print(wid)

        # check wether station name is critical
        if vid in critical_stations and [vid, wid] not in critical_connections and [wid, vid] not in critical_connections:

            # for every neighbour, add 1 critical line
            for n in G[vid]:
                critical_lines += 1
            print('( %s , %s, %3d), CRITICAL'  % ( vid, wid, G[v][w]['weight']))
            # add connection in list in both directions
            critical_connections.append([vid,wid,])
            
        else:
            print('( %s , %s, %3d)'  % ( vid, wid, G[v][w]['weight']))

        '''# check wether station name is critical
        elif wid in critical_stations and [wid, vid] not in critical_connections:
            # for every neighbour, add 1 critical line
            for n in G[wid]:
                critical_lines += 1
            print('( %s , %s, %3d), CRITICAL'  % ( vid, wid, G[v][w]['weight']))
            # add connection in list in both directions
            critical_connections.append([vid,wid])
            critical_connections.append([wid,vid])
        '''
        
            
print(critical_connections)


# link position attibute to node and call this 'pos'
pos = nx.get_node_attributes(G,'pos')

# make node lists
critical_node_list = []
non_critical_node_list = []

# define nodes
nodes = G.nodes()

# iterate over nodes
for node in nodes:
    if node in critical_stations:
        critical_node_list.append((node))
    else:
        non_critical_node_list.append((node))

# make edge lists
critical_edge_list = []
non_critical_edge_list = []
super_critical_edge_list = []

# define edges
edges = G.edges()

# iterate over tuples in edges (from, to) = (u,v)
for u,v in edges:
    if u in critical_stations and v in critical_stations:
        super_critical_edge_list.append((u,v))
    elif u in critical_stations or v in critical_stations:
        critical_edge_list.append((u,v))
    else:
        non_critical_edge_list.append((u,v))


# make dict keyed by tuple (from, to) : weight
edge_labels = {}
weight_list = []
# iterate over tuples in edges (from, to) = (u,v) 
# DEBUG: DOUBLE iterate edges earlier in code!
for u,v in edges:
    weight = G[u][v]['weight']
    weight_list.append(weight)
    edge_labels[u,v] = weight



critical_total = 0
not_critical_total = 0

# DEBUG: DOUBLE iterate edges earlier in code!
for u,v in edges:
    if u in critical_stations or v in critical_stations:
        critical_total += edge_labels[u,v]
    else:
        not_critical_total += edge_labels[u,v]

print((critical_total % 60))
print(critical_total // 60)
print((not_critical_total % 60))
print(not_critical_total // 60)

# Laat python tussen 0 en 21 berekenen en kies beginstation uit lijst.

# make list of all nodes (G.nodes() returns an object that is not accessable with nodes[i])
nodelist = critical_node_list + non_critical_node_list
minimum_weight = min(weight for weight in weight_list)

# rand number of tracks 1 up to including 7
random_tracks = random.randint(1,7)
# keep track of critical connections that are not used yet
critical_connections_not_traversed = critical_connections
length_critical_connections = len(critical_connections)
print('START track number is: ' + str(random_tracks))
for track in range(random_tracks):

    # rand start station 0 up to nodelist length - 1 to pick a node in nodelist
    starting_station = nodelist[random.randint(0,len(nodelist) - 1)]
    print('+++NEW Starting station is: ' + starting_station)
    print('+++NEW Neighbors are: {}'.format(G[starting_station]))
    time = 0

    random_time = random.randint(minimum_weight,120)
    print('+++NEW track length is going to be: ' + str(random_time))

    counter = 0
    delete_counter = 0
    while time < random_time:

        # chooses a random key from a dictionary (neighbors), is choosing a random neighbor
        random_neighbor = random.choice(G[starting_station].keys())

        print('Random choise is: ' + random_neighbor)

        # keeps track of time of the track
        time += G[starting_station][random_neighbor]['weight']

        # always pick one track, catch exception of second track being larger than random time
        if time > random_time and counter != 0:
            print('        CAUGHT EXCEPTION')
            break
        counter += 1

        print('The time from: ' + starting_station + ' to ' + random_neighbor + ' is: {}'.format(G[starting_station][random_neighbor]['weight']))
        print('The total time is: ' + str(time))
        
        # delete connection from critical_connections_not_traversed
        if [starting_station, random_neighbor] in critical_connections_not_traversed:
            critical_connections_not_traversed.remove([starting_station, random_neighbor])
            delete_counter += 1
            print([starting_station, random_neighbor])
        
        if [random_neighbor, starting_station] in critical_connections_not_traversed:
            critical_connections_not_traversed.remove([random_neighbor, starting_station])

        # updates the starting station
        starting_station = random_neighbor

        print('        Updated starting station is: ' + starting_station)
        print('        Updated neighbors are: {}'.format(G[random_neighbor]))




print(critical_connections)
print(delete_counter)

score = float(1 - float(len(critical_connections_not_traversed)) / float(length_critical_connections))
print(score)
print(float(len(critical_connections_not_traversed)))
print(float(length_critical_connections))
