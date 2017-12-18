#!/usr/bin/env python

from classes import graph_class as grc
from algorithms import hierholzer as hh, random_walk as rw, smart_random_walk as srw
from helpers import clear

# initialize datafiles
stations_0 = '../data/StationsHolland.csv'
connections_0 = '../data/ConnectiesHolland.csv'
stations_1 = '../data/StationsNationaal.csv'
connections_1 = '../data/ConnectiesNationaal.csv'

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
		elif choice == '2':
			g = grc.Graph('NH', stations_1, connections_1)

		algo_menu_0(g)

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
			# TODO
			pass

def algo_0(algo, g, hillclimber = False):
	'''
	A simple menu for setting the starting values for a given algorithm. Takes an algorithm (function) and a graph (object).
	'''

	seed = None
	if hillclimber:
		seed = algo_menu_1(g)
		max_track_number, max_track_time, iteration = get_input()

	else:
		# get user inputs
		max_track_number, max_track_time, iteration = get_input()
		services = algo(g, max_track_number, max_track_time, iteration)

		for service in services:
			print('Service score: {}'.format(service.s_score))

# def algo_menu_1(g):
# 	choice = '0'
# 	while choice == '0':
# 		print('Hillclimber seed algorithm menu:\n')
# 		print('Please select the algorithm you want to seed the hillclimber with')
# 		print('1. Random Walk')
# 		print('2. Hierholzer')

# 		choice = input(' >> ')
# 		clear()

# 		# pass the chosen algorithm and the graph
# 		if choice == '1':
# 			pass
# 			# TODO
# 		elif choice == '2':
# 			max_track_number, max_track_time, iteration = get_input()
# 			return hh.hierholzer(g, max_track_number, max_track_time, iteration)

def get_input():

	max_track_time = int(input('Input maximum track time: '))
	max_track_number = int(input('Input maximum number of tracks per service: '))
	iteration = int(input('Input iteration amount: '))

	return max_track_number, max_track_time, iteration

if __name__ == '__main__':
	clear()
	main_menu()