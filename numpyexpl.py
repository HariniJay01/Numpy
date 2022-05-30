#NUMPY

import numpy as np 

a=np.array([1,2,3,4,5])

#slicing
b = a[1:3]

#assign value with list
select = [0, 2, 3, 4]
d = a[select]       #arr[1,3,4,5]
a[select] = 100000  #arr[10000,2,10000,10000,100000]


#size
a.size  ---->5

#no.of dimensions
a.ndim   ---->1

#shape
a.shape    ---->(5,)



#mean of elements
mean=a.mean()

#standard deviation
st=a.std()

#maximumvalue
max_val=a.max()

#minimumvalue
min_value=a.min()





#Array addition
u=np.array([1,0])
v=np.array([2,1])
z=np.add(u,v)   #------>arr([3,1]) 
d=np.subtract(u,v)   #to subtract
f=np.multiply(u,v)   #to multiply
g=np.divide(u,v)   #to divide
j=np.dot(u,v)      #to find DOT PRODUCT




x = np.array([0, np.pi/2 , np.pi])   #array in radians
y = np.sin(x)        #sine of the values

#linspace
np.linspace(-2, 2, num=5)
np.linspace(5, 4, num=9)


#PLOTTING GRAPH BETWEEN X AND Y

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec1(u, z, v):
    
    ax = plt.axes()          # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)                 # Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')                    #Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)          # Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')                    #Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')                    #Adds the text z to the Axes 
    plt.ylim(-2, 2)                              #set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)                              #set the xlim to left(-2), right(2)

Plotvec1(u,z,v)
