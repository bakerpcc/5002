# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 14:43:28 2016

@author: ThinkPad User
"""

from numpy import *
import time
import matplotlib.pyplot as plt

def EuclDistance(vector1,vector2):
    return sqrt(sum(power(vector2-vector1,2)))
    
def initCentroids(testdata,k):
    centroids=zeros((k,2))
    centroids[0,:]=testdata[7,:]
    centroids[1,:]=testdata[2,:]
    centroids[2,:]=testdata[3,:]
    return centroids
    
def my_kmeans(testdata,k):
    numSamples=testdata.shape[0]
    clusterResult=mat(zeros((numSamples,2)))
    clusterChanged=True
    
    centroids=initCentroids(testdata,k)
    
    while clusterChanged:
        clusterChanged=False
        for i in xrange(numSamples):
            minDist=1000
            minIndex=0
            for j in range(k):
                distance=EuclDistance(centroids[j,:],testdata[i,:])
                if distance<minDist:
                    minDist=distance
                    minIndex=j
            if clusterResult[i,0]!=minIndex:
                clusterChanged=True
                clusterResult[i,:]=minIndex,minDist**2
                
        for j in range(k):
            pointsInCluster=testdata[nonzero(clusterResult[:,0].A==j)[0]]
            centroids[j,:]=mean(pointsInCluster,axis=0)
                    
        print 'successfully'
        return centroids,clusterResult
            
def showCluster(testdata,k,centroids,clusterResult):
    numSamples,dim=testdata.shape
    
    mark=['or','ob','og']
    
    for i in xrange(numSamples):
        markIndex=int(clusterResult[i,0])
        plt.plot(testdata[i,0],testdata[i,1],mark[markIndex])
        
    mark=['Dr','Db','Dg']
    for i in range(k):
        plt.plot(centroids[i,0],centroids[i,1],mark[i],markersize=12)
        
    plt.show()