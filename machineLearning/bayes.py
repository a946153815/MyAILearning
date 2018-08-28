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
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs=len(trainMatrix)
    pass