#!/usr/bin/env python

'''
Authors:
Dimitri van Capelleveen
Thom Oosterhuis
Rick van Bork

Team Stellar Heuristieken
'''

from classes import graph_class as grc
from algorithms import hierholzer as hh, random_walk as rw, smart_random_walk as srw, hillclimber as hc, hillclimber_sim_an as hs
from helpers import clear
from analysis import draw_graph

# initialize datafiles
stations_0 = '../data/StationsHolland.csv'
connections_0 = '../data/ConnectiesHolland.csv'
stations_1 = '../data/StationsNationaal.csv'
connections_1 = '../data/ConnectiesNationaal.csv'

error0 = 'Please select a valid integer!\n'

def main_menu():

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

	choice = '0'
	while choice == '0':
		print('Algorithm menu:\n')
		print('Please select the algorithm you want to run')
		print('1. Random Walk')
		print('2. Smart Random Walk')
		print('3. Hierholzer')
		print('4. Hillclimber')
		print('5. Hillclimber with Simulated Annealing')

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
		elif choice == '5':
			algo_0(hs.run_hillclimber_sim_an, g, True)
		else:
			print(error0)
			choice = '0'

def algo_0(algo, g, hillclimber = False):

	seed = None
	if hillclimber:
		seed = algo_1(g)

		print('\nYou have created a service object!\nPlease select preferred values for the Hillclimber. Suggestions for viable simulations are behind the inputs:\n')

		max_track_number, max_track_time, iteration = get_input()
		service = algo(seed, max_track_number, max_track_time, iteration)

	else:
		max_track_number, max_track_time, iteration = get_input()
		services = algo(g, max_track_number, max_track_time, iteration)

		draw_menu(services, g)

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

	while True:
		try:
			max_track_time = int(input('Input maximum track time (1 - 180): '))
			max_track_number = int(input('Input maximum number of tracks per service (1 - 20): '))
			iteration = int(input('Input iteration amount (5 - 10.000): '))
		except ValueError:
			print('Please provide a valid integer!')
		else:
			if iteration < 5:
				clear()
				print('Iteration number must be at least 5!')
				continue
			else:
				break

	clear()
	return max_track_number, max_track_time, iteration

def get_small_input():

	print('Please select small values to allow Hillclimber to \'climb\' to better services. Suggestions for generating a bad service are behind the inputs:\n')

	while True:
		try:
			max_track_time = int(input('Input maximum track time (1 - 50): '))
			max_track_number = int(input('Input maximum number of tracks per service (1 - 3): '))
			iteration = int(input('Input iteration amount (1 - 10): '))
		except ValueError:
			print('Please provide a valid integer!')
		else:
			if iteration < 5:
				clear()
				print('Iteration number must be at least 5!')
				continue
			else:
				break

	clear()
	return max_track_number, max_track_time, iteration

def draw_menu(services, g):

	clear()

	choice = '0'
	while choice == '0':

		# print service scores
		i = 0
		print('Service\tScore')
		for service in services:
			print('   {}.\t{}'.format(i + 1, service.s_score))
			i += 1

		print('\nDraw menu:\n')
		print('Please select a service you want to visualize.\nServices are saved in: \'visualization\plots\', as seperate PNG')
		print('1. Service 1')
		print('2. Service 2')
		print('3. Service 3')
		print('4. Service 4')
		print('5. Service 5')

		choice = input(' >> ')
		clear()

		# pass the chosen algorithm and the graph
		if choice == '1':
			draw_graph(g, services[0])
		elif choice == '2':
			draw_graph(g, services[1])
		elif choice == '3':
			draw_graph(g, services[2])
		elif choice == '4':
			draw_graph(g, services[3])
		elif choice == '5':
			draw_graph(g, services[4])
		else:
			print(error0)
			choice = '0'

if __name__ == '__main__':
	clear()
	main_menu()