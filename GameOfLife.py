#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import numpy as np
import random


# In[8]:


def main():
#     print("1")
    w.delete("all")
    ngrid = np.zeros_like(cgrid)
    curr_grid=np.copy(cgrid)
    #COUNTING NEIGHBORS
    #-----------------------------------------------------------
    for row in range(1, GRIDSIZE+1):
        for col in range(1, GRIDSIZE+1):
            ngrid[row][col] = np.sum(cgrid[row-1:row+2, col-1:col+2]) - cgrid[row][col]
    #-----------------------------------------------------------
    #UPDATING GRID
    for row in range(1, GRIDSIZE+1):
        for col in range(1, GRIDSIZE+1):
            if (ngrid[row][col] == 3) or (cgrid[row][col] == 1 and ngrid[row][col] == 2):
                cgrid[row][col] = 1
            else:
                cgrid[row][col] = 0
    #-----------------------------------------------------------
    #if previous and curr generation is same then quit
    if (np.array_equal(cgrid,curr_grid)):
        print("both equal")
        master.destroy()
    #-----------------------------------------------------------
    else:
        #Check if previous and current+1 generation is same. It means it is stuck in infinite loop
        nextgridcheck = np.zeros((GRIDSIZE+2, GRIDSIZE+2), dtype='int')
        for row in range(1, GRIDSIZE+1):#neighbor count of present grid
            for col in range(1, GRIDSIZE+1):
                ngrid[row][col] = np.sum(cgrid[row-1:row+2, col-1:col+2]) - cgrid[row][col]
        #-----------------------------
        for row in range(1, GRIDSIZE+1):
            for col in range(1, GRIDSIZE+1):
                if (ngrid[row][col] == 3) or (cgrid[row][col] == 1 and ngrid[row][col] == 2):
                    nextgridcheck[row][col] = 1
                else:
                    nextgridcheck[row][col] = 0
        #---------------------------------
        if (np.array_equal(curr_grid,nextgridcheck)):#checking if next generation is same is (present-1)
            master.destroy()
    #-----------------------------------------------------------
    #DRAWING BOARD
    for i in range(GRIDSIZE):
        for j in range(GRIDSIZE):
            if cgrid[i][j] == 1:
                w.create_rectangle(i*21, j*21, i*21 + 20,j*21 + 20, fill='chartreuse2')
            else:
                w.create_rectangle(i*21, j*21, i*21 + 20, j*21+20, fill='brown4')
    #-----------------------------------------------------------
    w.after(250,main)#call main() again after every 1/4 of second (250 millisecond) which means frame rate is 4 frames per sec


# In[9]:


master = Tk()

global flag
flag=False
w = Canvas(master, width=220,height=220)#creating canvas
GRIDSIZE = 10
cgrid = np.zeros((GRIDSIZE+2, GRIDSIZE+2), dtype='int')#setting up the board
cgrid[1:-1, 1:-1] = np.random.randint(2, size=(GRIDSIZE, GRIDSIZE))#initializing the board
w.pack()
main() #calling again & again to show new generation of cells  

mainloop()


# In[ ]:





# In[ ]:




