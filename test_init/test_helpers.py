from collections import Counter

'''
Helpers file.

Here all functions not directly important to
algorithm functioning and classes are defined
'''

'''
Gets the percentage of critical connections traversed.
'''
def get_p(critical_connections_traversed, critical_connections):
	return len(critical_connections_traversed) / len(critical_connections)

'''
Calculates the score and rounds to nearest 10.
m term small, hence the rounding. Plus makes searching for
score occurrence easier.
'''
def get_score(p, t, m):
	return round(p * 10000 - (t * 20 + m / 100000), -1)

'''
Checks wether a certain connection is critical in any direction.
And wether the critical connection has already been travelled in any direction.
'''
def update_critical_connections_travesed(tuple, critical_edges, critical_edges_traversed):
	edge = tuple
	edge_reversed = (tuple[1], tuple[0])

	if (edge in critical_edges) or (edge_reversed in critical_edges):
		if not (edge in critical_edges_traversed) and not (edge_reversed in critical_edges_traversed):
			critical_edges_traversed.append(edge)
	return critical_edges_traversed

def print_score_information(score_list):

	# get range of score list, ints otherwhise range(min, max) does not take floats
	minimum = int(min(score_list))
	maximum = int(max(score_list))

	# make count dict
	count_dict = Counter(score_list)

	print('\nscore, amount\n++++++++++++++')

	# loop through all possible scores
	for i in range(minimum, maximum + 1, 1):

		score_count = count_dict[i]

		# only print relevant scores
		if score_count != 0:
			print("{:<10}".format(i), end='')
			print(count_dict[i])

	print("++++++++++++++\n")
	print("minimum: {}".format(minimum))
	print("maximum: {}\n".format(maximum))