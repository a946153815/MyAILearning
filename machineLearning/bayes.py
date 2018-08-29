import numpy as np
def loadDataSet():
    postingList=[['m','y','d','d','d','d','d'],['m','y','d','d','d','d','d'],['m','y','d','d','d','d','d'],['m','y','d','d','d','d','d'],['m','y','d','d','d','d','d'],['m','y','d','d','d','d','d']]
    classVec=[0,1,0,1,0,1]
    return postingList,classVec

def createVocabList(dataSet):
    vocabSet=set([])
    for document in dataSet:
        vocabSet=vocabSet|set(document)
    return list(vocabSet)
def setOfWords2Vec(vocabList,inputSet):
    returnVec=[0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)]=1
        else:print("the word :%s is not in my Vacabulary!"%word)
    return returnVec
    #贝里斯训练
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    numWords=len(trainMatrix[0])
    pAbusive=sum(trainCategory)/float(numTrainDocs)
    p0Num=np.zeros(numWords);p1Num=np.zeros(numWords)
    p0Denom=0.0;p1Denom=0.0
    for i in range(numTrainDocs):
        if trainCategory[i]==1:
            p1Num+=trainMatrix[i]
            p1Denom+=sum(trainMatrix[i])
        else:
            p0Num+=trainMatrix[i]
            p0Denom+=sum(trainMatrix[i])
            pass
        pass
    p1Vect=p1Num/p1Denom
    p0Vect=p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive