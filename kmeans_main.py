# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 14:25:38 2016

@author: ThinkPad User
"""

from numpy import*
from my_kmeans import *
import matplotlib.pyplot as plt

print "1.load data"
testdata=[]
myfile=open('testdata1.txt')
for line in myfile.readlines():
    lineEach=line.strip().split(' ')
    testdata.append([int(lineEach[0]),int(lineEach[1])])
    
print "2.clustering"
testdata=mat(testdata)
k=3
centroids,clusterResult=my_kmeans(testdata,k)

print "3.show results"
showCluster(testdata,k,centroids,clusterResult)