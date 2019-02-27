import operator
import os
import sys
from imp import reload

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import cv2
import cvHelper


def createDataSet():
        group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels=['A','A','B','B']
        return group,labels
#kNN核心算法
def classify0(inX,dataSet,labels,k):
	dataSetSize=dataSet.shape[0]
	diffMat=np.tile(inX,(dataSetSize,1))-dataSet
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**0.5
	sortedDistIndicies=distances.argsort()
	classCount={}
	for i in range(k):
		voteIlabel=labels[sortedDistIndicies[i]]
		classCount[voteIlabel]=classCount.get(voteIlabel,0)+1
		sortedClassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]
def file2matrix(filename):
        fr=open(filename)
        arrayOLines=fr.readlines()
        numberOfLines=len(arrayOLines)
        returnMat =np.zeros((numberOfLines,3))
        classLabelVector=[]
        index=0
        for line in arrayOLines:
                line=line.strip()
                listFromLine=line.split('\t')
                returnMat[index,:]=listFromLine[0:3]
                classLabelVector.append(int(listFromLine[-1]))
                index+=1
        return returnMat,classLabelVector
#归一化
def autoNorm(dataSet):
	minVals =dataSet.min(0)
	maxVals =dataSet.max(0)
	ranges=maxVals-minVals
	normDataSet=np.zeros(np.shape(dataSet))
	m=dataSet.shape[0]
	normDataSet=dataSet-np.tile(minVals,(m,1))
	normDataSet=normDataSet/np.tile(ranges,(m,1))
	return normDataSet,ranges,minVals
#图片转数组向量
def img2vector(imgpath):
	img=cv2.imread(imgpath)
	img=cvHelper.lhx_local_threshold(img)
	returnVect=np.zeros((1,3600))
	for i in range(60):
		linestr=img[i]
		for j in range(60):
			returnVect[0,60*i+j]=int(linestr[j])
	return returnVect
def handwritingClassTest():
	hwLabels=[]
	trainingFileList =os.listdir('trainingDigits')
	m=len(trainingFileList)
	trainingMat =np.zeros((m,3600))
	for i in range(m):
		fileNameStr=trainingFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('-')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:]=img2vector('trainingDigits/%s' % fileNameStr)
	testFileList=os.listdir('testDigits')
	errorCount=0.0
	mTest=len(testFileList)
	for i in range(mTest):
		fileNameStr=testFileList[i]
		fileStr=fileNameStr.split('.')[0]
		classNumStr=int(fileStr.split('-')[0])
		vectorUnderTest=img2vector('testDigits/%s' % fileNameStr)
		classifierResult=classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print("the classifier came back with :%d,the real answer is:%d"%(classifierResult,classNumStr))
		if(classifierResult!=classNumStr):errorCount+=1.0
	print("\nthe total number of error is :%d"%errorCount)
