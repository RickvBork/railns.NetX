from classes import graph_class as grc
from algorithms import random_walk as rw, hierholzer as hh
import sys, os

# initialize datafiles
stations_0 = '../data/StationsHolland.csv'
connections_0 = '../data/ConnectiesHolland.csv'
stations_1 = '../data/StationsNationaal.csv'
connections_1 = '../data/ConnectiesNationaal.csv'

# function for clearing the console
clear = lambda: os.system('cls')

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

		algo_menu(g)

def algo_menu(g):
	'''
	A simple menu for choosing between different functions. Takes a graph object, and calls another menu function.
	'''

	choice = '0'
	while choice == '0':
		print('Algorithm menu:\n')
		print('Please select the algorithm you want to run')
		print('1. Random Walk')
		# TODO ADD MORE ALGO's

		choice = input(' >> ')
		clear()

		# pass the chosen algorithm and the graph
		if choice == '1':
			algo_0(rw, g)

def algo_0(algo, g):
	'''
	A simple menu for setting the starting values for a given algorithm. Takes an algorithm (function) and a graph (object).
	'''

	# get user inputs
	max_track_time = int(input('Input maximum track time: '))
	max_track_number = int(input('Input maximum number of tracks per service: '))
	iteration = int(input('Input iteration amount: '))

	# TODO make arguments consistent for similar algo's
	algo(g, iteration, max_track_number, max_track_time)

if __name__ == '__main__':
	main_menu()