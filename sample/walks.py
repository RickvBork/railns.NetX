'''


'''
import csv
import networkx as nx
import matplotlib.pyplot as plt
import tkinter # by thom, because of some run errors
import random





def walk1(nodelist, minimum_weight, critical_connections):
		
		# start a list of unique critical tracks the random walk traverses
		critical_connections_traversed = []

		# rand number of tracks 1 up to including 7
		random_tracks = random.randint(1,7)
		# try max number of tracks
		#random_tracks = 7

		# keep track of critical connections that are not used yet
		delete_counter = 0
		total_time = 0

		# print('START track number is: ' + str(random_tracks))

		for track in range(random_tracks):

			# rand start station 0 up to nodelist length - 1 to pick a node in nodelist
			starting_station = nodelist[random.randint(0,len(nodelist) - 1)]
			# print('+++NEW Starting station is: ' + starting_station)
			# print('+++NEW Neighbors are: {}'.format(G[starting_station]))
			time = 0

			# rand time for a given track
			random_time = random.randint(minimum_weight,120)
			# print('+++NEW track length is going to be: ' + str(random_time))

			counter = 0
			while time < random_time:

				# chooses a random key from a dictionary (neighbors), is choosing a random neighbor

				#random_neighbor = random.choice(G[starting_station]).keys()
				random_neighbor = random.choice(list(G[starting_station]))
				# print('Random choise is: ' + random_neighbor)

				# keeps track of time of the track
				time += G[starting_station][random_neighbor]['weight']
				total_time += G[starting_station][random_neighbor]['weight']
				# always pick one track, catch exception of second track being larger than random time
				if time > random_time and counter != 0:
					#print('        CAUGHT EXCEPTION')
					break
				counter += 1

				# print('The time from: ' + starting_station + ' to ' + random_neighbor + ' is: {}'.format(G[starting_station][random_neighbor]['weight']))
				# print('The total time is: ' + str(time))
		
				# make list of unique traversed critical connections
				if ((starting_station, random_neighbor) in critical_connections) or ((random_neighbor, starting_station) in critical_connections):
					if not ((starting_station, random_neighbor) in critical_connections_traversed) and not ((random_neighbor, starting_station) in critical_connections_traversed):
						critical_connections_traversed.append((starting_station, random_neighbor))

					# print('		DELETED: ' + str((starting_station, random_neighbor)))

				# updates the starting station
				starting_station = random_neighbor
				# print('        Updated neighbors are: {}'.format(G[random_neighbor]))

		# print(critical_connections)
		# print(delete_counter)

		# print("+++++++++++++++++++")
		# print(critical_connections_not_traversed)
		
		# percentage of critical tracs traversed
		score = float(len(critical_connections_traversed)) / float(len(critical_connections))
		
		# score function 1
		S = score * 10000 - (random_tracks * 20 + total_time / 100000)

		# rounds S to nearest 10, otherwhise the amount of columns in bar chart is insane...
		S_10 = round(S, -1)

		return score, S_10
