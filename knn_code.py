import csv
import random
import math
import operator
from time import sleep

# Split the data into trainingset
def loadDataset1(filename,split,trainingSet=[] ):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(128):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
              
# Split the data into TestSet

def loadDataset2(filename,split,testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(128):
                dataset[x][y] = float(dataset[x][y])
          
            if random.random() < split:
                testSet.append(dataset[x])



                
    ## finding the ecuclideanDistance 
          
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((float(instance1[x]) - float(instance2[x])), 2)
          return math.sqrt(distance)
    print("euclid   ")


    ## here we will get the neighbors


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        print("euclid1   ")
        distances.append((trainingSet[x], dist))
        
    distances.sort(key = operator.itemgetter(1))
   
    print("sdds")
    neighbors = []
  
    for x in range(k):
        neighbors.append(distances[x][0])
       # print(neighbors)
       # sleep(2)
    return neighbors
    


## here we will get the class votes


def getResponse(neighbors):
    # Creating a list with all the possible neighbors
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        #print(response)
        #sleep(2)
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
        print(classVotes)
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=False)
    print(sortedVotes)
    return sortedVotes[0][0]
 
   ## finding accuracy

def getAccuracy(testSet, predictions):
    correct = 0
    for y in range(len(predictions)):
        for x in range(len(testSet)):
            if testSet[x][-1] == predictions[y]:
                correct += 1
                print(correct)
        #print(len(testSet))
    return (correct/float(len(testSet))) * 100.0
 

               
def main():
    trainingSet=[]
    testSet=[]
    split = 1
    loadDataset1('minitrain.csv',split,  trainingSet)
    loadDataset2('minitest.csv', split, testSet)
    print ('Train set: ' + repr(len(trainingSet)))
    print ('Test set: ' + repr(len(testSet)))    
    predictions=[]
    k = 3
    for x in range(len(testSet)):
        print(len(testSet))
        #sleep(2)
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        
    accuracy = getAccuracy(testSet, predictions)
    
main()
