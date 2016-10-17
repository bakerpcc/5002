# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:46:32 2016

@author: ThinkPad User
"""


x=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
w0=-0.1
w1=-0.2
w2=0.2
x0=-1.0
alpha=0.05
cnt=0
i=0
step=0
while cnt<4:
    step+=1
    x1=x[i][0]
    x2=x[i][1]
    t=x[i][2]
    #print x1,x2,t
    
    a=round(x0*w0+x1*w1+x2*w2,3)
    #print a
    if (a>0):
        fx=1
    else:
        fx=0
    #print fx

    if(t!=fx):
        print ("No%d: for_tuple:%d w0:%.3f w1:%.3f w2:%.3f current_output:%d error"%(step,i,w0,w1,w2,fx))
        w0=round(w0+alpha*(t-fx)*x0,3)
        w1=round(w1+alpha*(t-fx)*x1,3)
        w2=round(w2+alpha*(t-fx)*x2,3)
        cnt=0
    else:
        print ("No%d: for_tuple:%d w0:%.3f w1:%.3f w2:%.3f current_output:%d correct"%(step,i,w0,w1,w2,fx))
        cnt+=1
        i=(i+1)%4
            
"""

x0=[-1.0]*4
x1=[0.0,0.0,1.0,1.0]
x2=[0.0,0.1,0.0,1.0]
t=[0.0,0.0,0.0,1.0]

w0=-0.1
w1=-0.2
w2=0.2
alpha=0.05

flag,i,step,j=0,0,0,0
while flag<4:
        step+=1
        y=x0[i]*w0+x1[i]*w1+x2[i]*w2
        if y<=0:
            y=0
        else:
            y=1
        if y!=t[i]:
            print("step %d:wrong!current output:y=%d"%(step,y))
            w0=round(w0+alpha*(t[i]-y)*x0[i],3)
            w1=round(w1+alpha*(t[i]-y)*x1[i],3)
            w2=round(w2+alpha*(t[i]-y)*x2[i],3)
            print ("i:%d"%i),w0,w1,w2
            flag=0
        else:
            print("step %d:correct!current output:y=%d"%(step,y))
            flag+=1
        i=(i+1)%4
print("final:%d %d %d"%(w0,w1,w2))

"""






            