# python2_drunks_go_home
This code is designed to simulate helping a drunk find his way home.
## move.py purpose
I'm gooing to make a Agent class, in a new move.py module, and put the code(move,add) that initialises the agents. I initialise move() and add().
## Function move()
Function of move() is going to give the drunks a random direction and then have him move a random unit in that direction.
## Function add()
Function of add() is to add one value in the blank file when the drunks pass by.
## Usage  
```python
import random
class Agent():
    def __init__(self,environment):
        self.environment = environment
        self.x = random.randint(138, 158)
        self.y = random.randint(128, 148)

    def move(self):
        if random.random() < 0.25:
            self.x = (self.x + 1) % 300
        elif random.random() < 0.5:
            self.x = (self.x - 1) % 300
        elif random.random() < 0.75:
            self.y = (self.y + 1) % 300
        else:
            self.y = (self.y - 1) % 300
        return (self.x, self.y)
    
    def add(self, environment):
        environment[self.x][self.y] = environment[self.x][self.y] + 1
```  
## Idea and method
I first thought of creating an agent to contain my main control motion model.In order to achieve the goal of bringing drunks home, I think two motion models are needed.One is to control the random movement of drunks, and the other is to control the coordinates of the path of drunks.And I've defined here where the drunk starts.Then in the move model, I divide the random number generated from 0 to 1 into 4 parts.When a number between 0 and 0.25 is generated, the drunk moves one unit to the east.When a number between 0.25 and 0.5 is generated, the drunk moves one unit to the west.When a number between 0.5 and 0.75 is generated, the drunk moves one unit north.When a number between 0.75-1 is generated, the drunk moves one unit south.In the add model, I want to record every move of the drunk in a blank file of 300 by 300 with coordinates 0,0.Every time a drunkard passes a coordinate, the value of that coordinate is multiplied by one.That way, when 25 drunks randomly walk home, we get a map of the density.
# main body
## Import
I use matplotlib.pyplot and move(I just created before).
## Function
Call matplotlib to draw and call the agent you created earlier to move.
## Usage
``` pyhton
import matplotlib.pyplot as ppt
import move
```
## Create a new list
Here I create a list of 300*300, set the initial value to 0, and assign the density value to the corresponding coordinate.
## Usage
``` python
density = []
for i in range(300):
    rowlist = []
    for j in range(300):
        rowlist.append(0)
        density.append(rowlist)
```
## Add the environment
``` python
f = open('drunk.txt') 
environment = []
for row in f:			
    parsed_row = str.split(row,",")
    Rlist = []
    for value in parsed_row:				
        Rlist.append(float(value))
    environment.append(Rlist)
f.close()
```
## Mark bar location
We need to determine the exact location of the bar, where all the drunks started.I selected the bars that were originally lit at 1 and set them to 100 so that they would show up clearly on the map.
## Usage
``` python
for a in range(300):
    for b in range(300):
        if environment[a][b] == 1:
           environment[a][b]=100
```
## Identify the drunk's starting point and label the house
The starting point of a drunkard is within a range, so randomly generate a starting point within that range as the starting point of a drunkard.Associate the number of the drunk with the number of the corresponding home.
## Usage
``` python
for j in range(num_of_agents):
    houseno = (j + 1) * 10
    house_labels.append(houseno)
    
for i in range(num_of_agents):
    drunks.append(move.Agent(environment))

for k in range(num_of_agents):
    while environment[drunks[k].x][drunks[k].y] != house_labels[k]:
        drunks[k].move()
        drunks[k].add(density)
    print('I am No.', k+1, 'to arrive', 'at', ':', drunks[k].x, drunks[k].y)
```
## Generate two images
Finally, we will generate two images, one of all 25 drunks returning home, and another of the density of drunks walking.
## Usage
``` python
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
```
