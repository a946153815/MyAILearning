import numpy as np
#加载数据集
def loadDataSet():
    dataMat=[];labelMat=[]
    fr=open('testSet.txt')
    for line in fr.readlines():
        lineArr=line.strip().split()
        dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
        pass
    return dataMat,labelMat
def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))