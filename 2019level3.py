#2019 AoC - Day 3 - 18/12/2019 - Python

import re, itertools
import matplotlib.pyplot as plt

input1 = []
input2 = []
intersections = []
bestdistance = 0
routeA = open("2019level3.txt", "r")
routeB = open("2019level3b.txt", "r")
route1 = re.findall('([A-Z])([0-9]+)', routeA.read())
route2 = re.findall('([A-Z])([0-9]+)', routeB.read())

def sanitize(route):
	#converting the steps to int, as the regexp picks a string
	for i, (direction, steps) in enumerate(route):
		route[i] = (direction, int(steps))

def processroute(route1, route2):
	#initial ugly implementation, lots of redundant code, but it works
	lastx1 = 0
	lastx2 = 0
	lasty1 = 0
	lasty2 = 0
	global input1, input2
	for direction, steps in route1:
		if direction == 'U':
			while steps > 0:
				lasty1 = lasty1 + 1
				input1.append(tuple([lastx1, lasty1]))
				steps -= 1
		elif direction == 'D':
			while steps > 0:
				lasty1 = lasty1 - 1
				input1.append(tuple([lastx1, lasty1]))
				steps -= 1
		elif direction == 'L':
			while steps > 0:
				lastx1 = lastx1 - 1
				input1.append(tuple([lastx1, lasty1]))
				steps -= 1
		elif direction == 'R':
			while steps > 0:
				lastx1 = lastx1 + 1
				input1.append(tuple([lastx1, lasty1]))
				steps -= 1
		else:
			print "Error!"
			break
	for direction, steps in route2:
                if direction == 'U':
                        while steps > 0:
                                lasty2 = lasty2 + 1
                                input2.append(tuple([lastx2, lasty2]))
				steps -= 1
                elif direction == 'D':
                        while steps > 0:
                                lasty2 = lasty2 - 1
                                input2.append(tuple([lastx2, lasty2]))
				steps -= 1
                elif direction == 'L':
                        while steps > 0:
                                lastx2 = lastx2 - 1
                                input2.append(tuple([lastx2, lasty2]))
				steps -= 1
                elif direction == 'R':
                        while steps > 0:
                                lastx2 = lastx2 + 1
                                input2.append(tuple([lastx2, lasty2]))
				steps -= 1
		else:
			print "Error!"
			break
	return 0

def find_intersections(route1, route2):
	#find intersections for the two list of tuples we processed
	global intersections
	#original implementation for this was a nested for loop... it took almost 30 min to iterate
	#through almost half of the huge list. A set did it in less than 1 second.
	route1 = set(route1)
	route2 = set(route2)
	intersections = route1 & route2

def manhattan_distance(x1, y1, x2, y2):
	#formula is |x1 - x2| + |y1 - y2|, we already know x2 and y2, being 0,0
	distance = abs(x1 - x2) + abs(y1 - y2)
	return distance

def min_number_of_steps():
	#use the index number of the list to calculate the number of steps.
	global intersections
	index1 = 0
	index2 = 0
	bestindex1 = -1
	bestindex2 = -1

	for i in intersections:
		print i
		index1 = input1.index(i)+1
		index2 = input2.index(i)+1
		if index1 < bestindex1 and index2 < bestindex2:
			bestindex1 = index1
			bestindex2 = index2
		elif bestindex1 == -1 or bestindex2 == -1:
			bestindex1 = index1
			bestindex2 = index2
		else:
			continue
	return bestindex1, bestindex2

sanitize(route1)
sanitize(route2)
processroute(route1, route2)
find_intersections(input1, input2)
for x1, y1 in intersections:
	distance = manhattan_distance(x1, y1, 0, 0)
	if distance < bestdistance or bestdistance == 0:
		bestdistance = distance
	else:
		continue
print "Best distance is", bestdistance
bestindex1, bestindex2 = min_number_of_steps()
bestindex = bestindex1 + bestindex2
print "Fewest Combined steps the wires must take is: ", bestindex
#a little extra :)
input1x = zip(*input1)[0]
input1y = zip(*input1)[1]
input2x = zip(*input2)[0]
input2y = zip(*input2)[1]
plt.plot(input1x, input1y)
plt.plot(input2x, input2y)
plt.show()
