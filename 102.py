#given three points, find the area of the triangle they create
#add the origin to the set of points, and calculate the total area of each of the three new triangles
#if the area of the latter exceeds that of the former, the origin lies outside the triangle

import math

solutions = 0

fname = "p102_triangles.txt"

with open(fname) as f:
	pointsets = f.readlines()

for e,p in enumerate(pointsets):
	my_list = p.split(',')
	if '\n' in my_list:
		my_list.remove('\n')
	list_of_tuples = list()
	for l in range(0,len(my_list)/2):
		list_of_tuples.append(tuple([int(my_list[2*l]),int(my_list[2*l+1])]))
	pointsets[e] = list_of_tuples

def points_length(points):
	return math.sqrt((points[1][0]-points[0][0])**2+(points[1][1]-points[0][1])**2)

def tri_area(points):
	lengths = list()
	for e,p in enumerate(points):
		lengths.append(points_length([points[e],points[e-1]]))
	s = sum(lengths)/2
	return math.sqrt(s*(s-lengths[0])*(s-lengths[1])*(s-lengths[2]))

for t in pointsets:
	area = tri_area(t)
	origin_area = 0
	for e,p in enumerate(t):
		origin_area += tri_area([t[e-1],t[e],(0,0)])
	print "origin_area %s area %s" % (int(origin_area), int(area))
	# round off any decimal noise
	if abs(origin_area-area) < 1:
		solutions += 1

print solutions
