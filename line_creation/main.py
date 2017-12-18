#!/usr/bin/env python

from classes import graph_class as grc
from algorithms import hierholzer as hh, random_walk as rw, smart_random_walk as srw, hillclimber as hc
from helpers import clear

# initialize datafiles
stations_0 = '../data/StationsHolland.csv'
connections_0 = '../data/ConnectiesHolland.csv'
stations_1 = '../data/StationsNationaal.csv'
connections_1 = '../data/ConnectiesNationaal.csv'

error0 = 'Please select a valid integer!\n'

def main_menu():
	'''
	A main menu for loading different datafiles necessary to initiate a graph (object). Calls another menu function.
	'''

	choice = '0'
	while choice == '0':
		print('Datafiles menu\n')
		print('Please select the files you want to load')
		print('1. North Holland')
		print('2. Netherlands')

		choice = input(' >> ')
		clear()

		# build chosen graph object
		if choice == '1':
			g = grc.Graph('NH', stations_0, connections_0)
			algo_menu_0(g)
		elif choice == '2':
			g = grc.Graph('NH', stations_1, connections_1)
			algo_menu_0(g)
		else:
			print(error0)
			choice = '0'

def algo_menu_0(g):
	'''
	A simple menu for choosing between different functions. Takes a graph object, and calls another menu function passing the graph and the chosen algorithm.
	'''

	choice = '0'
	while choice == '0':
		print('Algorithm menu:\n')
		print('Please select the algorithm you want to run')
		print('1. Random Walk')
		print('2. Smart Random Walk')
		print('3. Hierholzer')
		print('4. Hillclimber')
		print('5. Simulated Annealing')

		choice = input(' >> ')
		clear()

		# pass the chosen algorithm and the graph
		if choice == '1':
			algo_0(rw.random_walk, g)
		elif choice == '2':
			algo_0(srw.smart_random_walk, g)
		elif choice == '3':
			algo_0(hh.hierholzer, g)
		elif choice == '4':
			algo_0(hc.run_hillclimber, g, True)
		else:
			print(error0)
			choice = '0'

def algo_0(algo, g, hillclimber = False):
	'''
	A simple menu for setting the starting values for a given algorithm. Takes an algorithm (function) and a graph (object).
	'''

	seed = None
	if hillclimber:
		seed = algo_1(g)
		
		# print(seed.s_score)
		# for track in seed.tracks:
		# 	print(track.edges)

		max_track_number, max_track_time, iteration = get_input()
		service = algo(seed, max_track_number, max_track_time, iteration)

	else:
		max_track_number, max_track_time, iteration = get_input()
		services = algo(g, max_track_number, max_track_time, iteration)

		for service in services:
			print('Service score: {}'.format(service.s_score))

def algo_1(g):

	choice = '0'
	while choice == '0':
		print('Hillclimber seed algorithm menu:\n')
		print('Please select the algorithm you want to seed the hillclimber with')
		print('1. Random Walk')
		print('2. Smart Random Walk')

		choice = input(' >> ')
		clear()

		# pass the chosen algorithm and the graph
		if choice == '1':
			max_track_number, max_track_time, iteration = get_small_input()

			return rw.random_walk(g, max_track_number, max_track_time, iteration)[0]
		elif choice == '2':
			max_track_number, max_track_time, iteration = get_small_input()

			return srw.smart_random_walk(g, max_track_number, max_track_time, iteration)[0]
		else:
			print(error0)
			choice = '0'

def get_input():

	print('You have created a service object! Please select preferred values for the Hillclimber Suggestions for viable simulations are behind the inputs:\n')

	max_track_time = int(input('Input maximum track time (1 - 180): '))
	max_track_number = int(input('Input maximum number of tracks per service (1 - 20): '))
	iteration = int(input('Input iteration amount (1 - 10.000): '))
	clear()

	return max_track_number, max_track_time, iteration

def get_small_input():

	print('Please select small values to allow Hillclimber to \'climb\' to better services. Suggestions for generating a bad service are behind the inputs:\n')

	max_track_time = int(input('Input maximum track time (1 - 50): '))
	max_track_number = int(input('Input maximum number of tracks per service (1 - 3): '))
	iteration = int(input('Input iteration amount (1 - 10): '))
	clear()

	return max_track_number, max_track_time, iteration

if __name__ == '__main__':
	clear()
	main_menu()