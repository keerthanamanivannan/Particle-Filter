import numpy as np
import sys
import time
import math


# variables :
# LaserReadings = [x, y, theta, xl, yl, thetal, r1......r180]
#
# parameters :
# zHit, zRand, zShort, zMax, sigmaHit, lambdaShort
# zMax = 1000
# L = 25

def rayCasting(ztk, xt, m):
    theta = xt[2]
    phi = ztk[2]
    xt_true = xt[0] + L*math.cos(theta) + zt*math.cos(theta + phi)
    yt_true = yt[0] + L*math.sin(theta) + zt*math.sin(theta + phi)
    zt_true = math.sqrt((xt_true*xt_true) + (yt_true*yt_true))
    return zt_true

def get_pHit(ztk, zt_true):
    if ztk >= 0 and ztk <= zMax:
        #pHit = np.random.normal(zt_true, sigmaHit)
        pHit = math.exp((-0.5*((ztk - zt_true)**2)/(sigmaHit**2)))/math.sqrt(2*math.pi*sigmaHit**2)
        return zHit * pHit
    else:
        return 0

def get_pShort(ztk, zt_true):
    if (ztk >= 0 and ztk <= zt_true):
        eta = 1/(1-math.exp(-lambdaShort*zt_true))
        pShort = eta * lambdaShort * math.exp(-lambdaShort*ztk)
        return zShort * pShort
    else:
        return 0

def get_pMax(ztk):
    if ztk == zMax:
        return 1
    else:
        return 0

def get_pRand(ztk):
    if ztk >= 0 and ztk < zMax:
        return 1/zMax
    else:
        return 0

def beamRangeFinderModel(zt, xt, m):
    q = 1
    zt_true = [0]*len(zt)
    for k in range(len(zt)):
        zt_true = rayCasting(zt[k], xt, m)        # ray casting step
        p = max(get_pHit(zt[k], zt_true), get_pShort(zt[k], zt_true), get_pMax(zt[k]), get_pRand(zt[k]))
        q = p*q
    return q

'''def learnIntrinsicParameters(Z, X, m):    # might not have to do this
    if not converged:
        for zi in range(len(Z)):'''
