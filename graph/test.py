
# coding: utf-8

# In[141]:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
import time


# #### Create plot + add subplots 

# In[142]:

fig = plt.figure()
axis = fig.add_subplot(1,1,1);


# In[143]:

def genCoords(i):
    xvals = []
    yvals = []
    x = 0
    while(x < 10):
        x+=1
        randY = randint(0,9)
        xvals.append(x)
        yvals.append(randY)
        axis.clear()
        axis.plot(xvals,yvals)       


# #### Animation function

# In[144]:

def animate(i):
    imported = open("sample.txt","r").read()
    data = imported.split('\n')
    xvals = []
    yvals = []
    for line in data:
        if len(line)>1:
            x,y = line.split(',')
            xvals.append(int(x))            
            yvals.append(int(y))
        axis.clear()
        axis.plot(xvals,yvals)


# In[145]:

pretty = animation.FuncAnimation(fig,genCoords,interval=0.1)


# In[146]:

plt.show()


# In[ ]:



