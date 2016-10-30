#!/usr/bin/env python
import os.path
import numpy as np
import matplotlib.pyplot as plt

def parser():
	OData = []
	LData = []
	basePath = os.path.dirname(__file__)
	filePath = os.path.abspath(os.path.join(basePath,"..","data","log","ascii-robotdata3.log"))
	f = open(filePath,"r")
	#with open('robotdata1.log') as f:
	lines = f.read().splitlines()
	f.close()

	for i,line in enumerate(lines):
		if lines[i][0] == 'L':
			l = lines[i].split()
			LData.append([float(l[x]) for x in range(1,len(l))])

			if lines[i+1][0] == 'O':
				l = lines[i+1].split()
				OData.append([float(l[x]) for x in range(1,len(l))])	
	OData = np.array(OData)
	LData = np.array(LData)
	#plt.plot(OData[:,0],OData[:,1])
	#plt.show()
	#print OData
	return OData, LData

#def main():
#	OData, LData = parser()

#if __name__ == "__main__": 
#	main()
