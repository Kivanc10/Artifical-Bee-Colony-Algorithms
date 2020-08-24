# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:16:37 2020

@author: Kivanc
"""

#%%
from random import uniform,randint,sample

def randomBees(size):
    return [randint(1,nVezir) for _ in range(nVezir)]

def changed(x):
    n = len(x)
    c = randint(0,n-1)
    m = randint(1,n)
    x[c] = m
    return x

def approachToGood(bees):
    changed(bees)
    changed(bees)
    return bees

def removeBees(bees):
    changed(bees)
    changed(bees)
    changed(bees)
    return bees

def fitness(bee):
    horizontalCollisions=sum([bee.count(queen)-1 for queen in bee])/2
    diagonalCollisions=0
    n=len(bee)
    leftDiagonal=[0]*2*n
    rightDiagonal=[0]*2*n
    for i in range(n):
        leftDiagonal[i+bee[i]-1]+=1
        rightDiagonal[len(bee)-i+bee[i]-2]+=1
    diagonalCollisions=0
    for i in range(2*n-1):
        counter=0
        if leftDiagonal[i]>1:
            counter+=leftDiagonal[i]-1
        if rightDiagonal[i]>1:
            counter+=rightDiagonal[i]-1
        diagonalCollisions+=counter/(n-abs(i-n+1))
    return int(maxFitness-(horizontalCollisions+diagonalCollisions))


def probability(bees,fitness):
    return fitness(bees)/maxFitness


def randomPick(population,probabilities):  #○ this function retun a population
    populationWithProbability = zip(population,probabilities)
    total = sum(w for c,w in populationWithProbability) # toplam uygunluk değeri
    r = uniform(0,total) # rastgele seçilen uygunluk değeri
    upto = 0
    for c,w in zip(population,probabilities):
        if upto+w >= r:
            return c
        upto+=w

def randF():
    return uniform(0.0001,0.9999)

def printBees(bees):
    print("Bees : {},fitness = {}".format(str(bees),fitness(bees)))
    


if __name__ == "__main__":
    nVezir = int(input("Enter count of queen"))
    iteration = 100
    maxFitness=(nVezir*(nVezir-1))/2
    generation=1
    workerBees=int(0.5*nVezir) # işçi sayısı 
    numFeeds=int(0.5*nVezir) # besin sayısı
    limitsOfTry=3 # deneme limiti
    goMethods = int(2 + ((randF()-0.5) * 2) * (2.5 - 1.2))
    bees = [randomBees(nVezir) for _ in range(iteration)] # başlangıç jenerasyonu
    while not maxFitness in [fitness(n) for n in bees]:
        print("Generation = {}".format(str(generation)))
        print("Max fitness = {}".format(max([fitness(n) for n in bees])))
        generation+=1
        bestBees = bees[randint(0,goMethods)]
        count = 0
        for j in range(nVezir):
            morePowerBees = approachToGood(bestBees)
            if (bees[j][1] > morePowerBees[1]):
                bees[j] = morePowerBees
            else:
                limitsOfTry+=1
        bees.sort(key=lambda x : x[1])
        probabilities = [probability(n,fitness) for n in bees]
        for i in range(nVezir-workerBees,nVezir):  # selection observer bee inside of worker bees
            observer = randomPick(bees,probabilities)
        for l in range(workerBees,nVezir): # append list who has best costs
            bees[l] = observer
        count+=1
        if (count > limitsOfTry):
            for k in range(nVezir):
                bees[k] = removeBees(bees[k])        
        bees.sort(key = lambda x : x[1])
    beesOut = [] # list that have max fitness value
    for n in bees:
        if fitness(n) == maxFitness:
            beesOut = n
            printBees(n)
    board = []
    for x in range(nVezir):
        board.append([" X "]*nVezir)
    
    for i in range(nVezir):
        board[nVezir-beesOut[i]][i] = " V "
    
    def printBoard(board):
        for row in board:
            print("".join(row))
    
    printBoard(board)
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
