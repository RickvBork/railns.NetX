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