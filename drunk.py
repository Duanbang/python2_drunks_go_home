# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:42:07 2020

@author: 戴尔
"""
import matplotlib.pyplot as ppt
import move
num_of_agents = 25
house_labels = []
drunks = []
density = []
for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
        density.append(rowlist)
#添加环境
f = open('drunk.txt') 
environment = []
for row in f:			
    parsed_row = str.split(row,",")
    Rlist = []
    for value in parsed_row:				
        Rlist.append(float(value))
    environment.append(Rlist)
f.close() 	
#标记酒吧位置	
for a in range(300):
    for b in range(300):
        if environment[a][b] == 1:
           environment[a][b]=100


#ppt.show
#确定醉汉起始点/给予房子标签
for j in range(num_of_agents):
    houseno = (j + 1) * 10
    house_labels.append(houseno)
    
for i in range(num_of_agents):
    drunks.append(move.Agent(environment))
#不停移动醉汉（25个起点）直到抵达房子
for k in range(num_of_agents):
    while environment[drunks[k].x][drunks[k].y] != house_labels[k]:
        drunks[k].move()
        drunks[k].add(density)
    print('I am No.', k+1, 'to arrive', 'at', ':', drunks[k].x, drunks[k].y)


fig = ppt.figure()
ax = fig.add_subplot(111)
ppt.xlim(0, 300)
ppt.ylim(0, 300)
ppt.title('Drunks route')
for m in range(num_of_agents):
    ppt.scatter(drunks[m].y, drunks[m].x)
ppt.imshow(environment)
ppt.show()        
            
fig = ppt.figure()
ax = fig.add_subplot(111)
ppt.xlim(0, 300)
ppt.ylim(0, 300)
ppt.title('Walking density map')
ppt.imshow(density)
ppt.show()





















