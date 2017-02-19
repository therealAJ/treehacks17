
# coding: utf-8

# In[67]:

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint
import time


# #### Create plot + add subplots 

# In[68]:

fig = plt.figure()
axis = fig.add_subplot(1,1,1);


# In[80]:

def genCoords(i):
    xvals = []
    yvals = []
    x = 0
    while(x < 500):
        x+=1
        randX = randint(0,9)
        randY = randint(0,9)
        xvals.append(randX)
        yvals.append(randY)
        axis.clear()
        axis.plot(xvals,yvals)       


# #### Animation function

# In[81]:

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


# In[82]:

pretty = animation.FuncAnimation(fig,animate,interval=100)
plt.plot()


# In[ ]:



