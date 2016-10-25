#!/usr/bin/python
import random
import math

def motionModel(uCurrent, uPrev, xPrev, alpha):
	odomRot1 = math.atan2(uCurrent[1] - uPrev[1], uCurrent[0]- uPrev[0]) - uPrev[2]
	odomTrans = math.sqrt((uCurrent[0] - uPrev[0])**2 + (uCurrent[1] - uPrev[1])**2)
	odomRot2 = uCurrent[2] - uPrev[2] - odomRot1

	trueRot1 = odomRot1 - sample(alpha[0]*odomRot1 + alpha[1]*odomTrans)
	trueTrans = odomTrans -  sample(alpha[2]*odomTrans + alpha[3]*(odomRot1 + odomRot2))
	trueRot2 = odomRot2 - sample(alpha[0]*odomRot2 + alpha[1]*odomTrans)

	xCurrent[0] = xPrev[0] + trueTrans * math.cos(xPrev[2] + trueRot1)
	xCurrent[1] = xPrev[1] + trueTrans * math.sin(xPrev[2] + trueRot1)
	xCurrent[2] = xPrev[2] + trueRot1 + trueRot2

	return xCurrent

def sample(sigma):
	return random.gauss(0, sigma)

