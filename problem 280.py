import random
import numpy as np
import matplotlib.pyplot as plt

class grid:
    def __init__(self):
        self.upper = [False,False,False,False,False]
        self.lower = [True,True,True,True,True]
        

class ant:
    def __init__(self):
        self.position = [2,2]
        self.seed = False
        self.moves = 0
        
    def get_move(self):
        if self.position[0] == 0 and self.position[1] == 0:
            move = random.choice(['R','D'])
        elif self.position[0] == 4 and self.position[1] == 0:
            move = random.choice(['U','R'])
        elif self.position[0] == 0 and self.position[1] == 4:
            move = random.choice(['L','D'])
        elif self.position[0] == 4 and self.position[1] == 4:
            move = random.choice(['U','L'])
        elif self.position[0] == 0:
            move = random.choice(['L','R','D'])
        elif self.position[1] == 0:
            move = random.choice(['U','R','D'])
        elif self.position[0] == 4:
            move = random.choice(['L','U','R'])
        elif self.position[1] == 4:
            move = random.choice(['U','L','D'])
        else:
            move = random.choice(['U','R','D','L'])
        
        return move
    
    def move(self):
        move = self.get_move()
        if move == 'U':
            self.position[0] -= 1
        if move == 'R':
            self.position[1] += 1
        if move == 'D':
            self.position[0] += 1
        if move == 'L':
            self.position[1] -= 1
            
        self.moves += 1


def ant_run(ant, grid):
    
    while False in grid.upper:

        ant.move()
        
        if ant.position[0] == 4 and ant.seed == False and grid.lower[ant.position[1]] == True:
            ant.seed = True
            grid.lower[ant.position[1]] = False

        if ant.position[0] == 0 and ant.seed == True and grid.upper[ant.position[1]] == False:
            grid.upper[ant.position[1]] = True
            ant.seed = False

    return ant.moves

moves_list = []

for i in range(30000000):
    grid1 = grid()
    ant1 = ant()
    moves_list.append(ant_run(ant1, grid1))
    if len(moves_list)%10000 == 0:
        print(f'Move number: {len(moves_list)}, mean: {np.mean(moves_list)}')    
    
print(np.mean(moves_list))
