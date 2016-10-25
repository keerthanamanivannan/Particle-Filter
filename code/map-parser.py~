#!/usr/bin/env python
import os.path
import matplotlib.pyplot as plt

def parser():
	basePath = os.path.dirname(__file__)
	filePath = os.path.abspath(os.path.join(basePath,"..","data","map","wean.dat"))
	f = open(filePath,"r")
	words = f.read().split()
	
	m, f2 = [], []
	for i in range(len(words)):
		if words[i] == 'robot_specifications->global_mapsize_x':
			global_mapsize_x = int(words[i+1])
		elif words[i] == 'robot_specifications->global_mapsize_y':
			global_mapsize_y = int(words[i+1])
		elif words[i] == 'robot_specifications->resolution':
			resolution = int(words[i+1])
		elif words[i] == 'robot_specifications->autoshifted_x':
			autoshifted_x = int(words[i+1])
		elif words[i] == 'robot_specifications->autoshifted_y':
			autoshifted_y = int(words[i+1])
		elif words[i] == 'global_map[0]:':
			mapsize_x = int(words[i+1])
			mapsize_y = int(words[i+2])
			m = [[] for t in range(mapsize_x)]  
			for x in range(0,mapsize_x):
				for y in range(0,mapsize_y):
					m[x].append(float(words[i+3+x*mapsize_y+y]))

	plt.imshow(m, extent=(0,800,0,800))
	plt.show()
	return m

def main():
	m = parser()

if __name__ == "__main__": 
	main()
