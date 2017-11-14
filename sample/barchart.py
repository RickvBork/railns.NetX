import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


def draw(scores):
	list = [element for element in scores if element <= 0.5]
	print(list)
	list = []
	objects = ("0 - 0.10", "0.10 - 0.20", "0.20 - 0.30", "0.30 - 0.40")
	number_of_categories = 4
	counter = 0
	categories = [0,0.1,0.2,0.3,0.4]
	performance = []
	for i in range(number_of_categories):
		list = [element for element in scores if element >= categories[counter] and element < categories[counter + 1]]
		performance.append(len(list))
		counter += 1
		
	print(performance)
	print(scores)
	y_pos = np.arange(len(objects))
	#performance = [10,8,6,4,2,1]
	 
	plt.bar(y_pos, performance, align='center', alpha=0.5)
	plt.xticks(y_pos, objects)
	plt.ylabel('Frequency')
	plt.xlabel('Score')
	plt.title('Scores')
	 
	plt.show()

#make_bar_chart([0,1,0.5,0.3,1,0,0,0])