'''
used to test functions, file is ignored by git.
'''

import line_algorithms as alg
import line_analysis as ana
import line_graph_class
import helpers as hlp
import csv
import numpy
import service_class as sc
import track_class as tc
import hillclimber as hh

# initialize path files for Noord Holland graph
path_stations_file = '../data/StationsHolland.csv'
path_tracks_file = '../data/ConnectiesHolland.csv'

# initialise graph class
Graph = line_graph_class.Graph

# make graph instance (Noord Holland)
g = Graph("NH", path_stations_file, path_tracks_file)

#all_paths_dijkstra_path_length(g.G[])
# get scores
scores, p_scores, best_tracks = alg.random_walk(g, 1000)

# create service from best_tracks
service1 = sc.service(g)
number_of_tracks = 7
for i in range(number_of_tracks):
	track1 = best_tracks[0]['tracks']['1']
	trackc = tc.track(track1, g)
	service1.add_track(trackc)

# now use hillclimber to improve service
number_of_tries = 10
for i in range(number_of_tracks):
	for j in range(number_of_tries):
		hh.hillclimber(service1,i)
		print(service1.get_s_score())

	
	

## print besttracks
#for track in range(len(best_tracks)):
#	print(best_tracks[track])
#	print("+++++++++++++++++++++++++++++++++")
#
#print("mean")
#print(numpy.mean(scores))
#print(numpy.std(scores))
#
## analyse and visualise scores
#ana.draw_barchart(scores)


# write scores to csv
# ref: https://stackoverflow.com/questions/39282516/python-list-to-csv-throws-error-iterable-expected-not-numpy-int64
# ref: https://docs.python.org/3/library/csv.html
#with open('../data/results.csv', 'w', newline='') as myfile:
#	wr = csv.writer(myfile,delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#	wr.writerows(map(lambda x: [x], scores))
#
