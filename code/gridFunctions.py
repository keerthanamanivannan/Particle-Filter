#!/usr/bin/env python
import numpy as np 
import math

def occupancy(x, resolution, map):
	xMap = int(math.floor(x[0]/resolution))
	yMap = int(math.floor(x[1]/resolution))
	return (map[xMap, yMap])

def checkLimits(x, resolution, mapSize):
	xMap = math.floor(x[0]/resolution)
	yMap = math.floor(x[1]/resolution)
	if (xMap >= 0) and (xMap < mapSize[0]) and (yMap >= 0) and (yMap < mapSize[1]):
		return True
	else:
		return False
