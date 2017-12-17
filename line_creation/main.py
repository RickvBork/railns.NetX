from classes import graph_class as grc
from algorithms import random_walk as rw, hierholzer as hh
import sys, os

# initialize path files for Noord Holland graph
stations_0 = '../data/StationsHolland.csv'
connections_0 = '../data/ConnectiesHolland.csv'
stations_1 = '../data/StationsNationaal.csv'
connections_1 = '../data/ConnectiesNationaal.csv'

g = None
max_track_time = 0
max_track_number = 0
iterator = 0

clear = lambda: os.system('cls')

def menu():

	choice = '0'
	while choice == '0':
		print('Main menu\n')
		print('Please select the files you want to load')
		print('1. North Holland')
		print('2. Netherlands')

		choice = input(' >> ')
		clear()

		if choice == '1':
			g = grc.Graph('NH', stations_0, connections_0)
		elif choice == '2':
			g = grc.Graph('NH', stations_1, connections_1)

		algo_menu(g)

def algo_menu(g):
	print('Please make a choice: ')

	choice = '0'
	while choice == '0':
		print('Main menu:')
		print('1. Random Walk')
		# TODO ADD MORE ALGO's

		choice = input('Please make a choice: ')
		clear

		if choice == '1':
			algo_0(rw, g)

def algo_0(algo, g):
	max_track_time = int(input('Input maximum track time: '))
	max_track_number = int(input('Input maximum number of tracks per service: '))
	iteration = int(input('Input iteration amount: '))

	# TODO make arguments consistent for similar algo's
	algo(g, iteration, max_track_number, max_track_time)

if __name__ == '__main__':
	menu()