#import python libraries 

import random
import math

#parameters declaration 

initial_temprature=1000
max_iterations=100
cool_factor=0.95


def acceptibility(fit1,fit2,temprature):
    if fit2<fit1:
        return 1
    else:
        return math.exp((fit1-fit2)/temprature)

def count_fitness(p,path):
    score=0
    for i in range(len(path)):
        if(i!=(len(path)-1)):
            score += p[path[i]-1][path[i+1]-1]
        else:
            score += p[path[i]-1][0]
    return score

def get_neighbor(current):
    neighbor=list(current)
   
    index1=random.randint(1,len(current)-1)
    index2=random.randint(1,len(current)-1)
    
    temp=neighbor[index1]
    neighbor[index1]=neighbor[index2]
    neighbor[index2]=temp
    
    return neighbor

def simulated(p,current):
    temprature=initial_temprature
    solution=current
    while temprature>1e-6:
        
        for i in range(max_iterations):
            neighbor=get_neighbor(current)

            current_fitness=count_fitness(p,current)
            
            neighbor_fitness=count_fitness(p,neighbor)

            if acceptibility(current_fitness,neighbor_fitness,temprature)>random.random():
                solution=neighbor
                current=neighbor
        temprature *= cool_factor
     
    print(solution)
    print(count_fitness(p,solution))
    
#driver code
p=[[0 for i in range(5)]for j in range(5)]

p[0][1]=p[1][0]=12
p[0][2]=p[2][0]=10
p[0][3]=p[3][0]=19
p[0][4]=p[4][0]=8
p[1][2]=p[2][1]=3
p[1][3]=p[3][1]=7
p[1][4]=p[4][1]=6
p[2][3]=p[3][2]=2
p[2][4]=p[4][2]=20
p[3][4]=p[4][3]=4

initial_solution=[1,2,3,4,5]
simulated(p,initial_solution)
