import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import threading
import time

import bayes
import cvHelper
import logRegres
#import kNN
#cvHelper.lhx_CameraPreview()
#dataset,de=bayes.loadDataSet()
#r=bayes.createVocabList(dataset)

#bayes.testingNB()0
#arr=Series([1,2],index=['dd','db'])
#print(arr)
# arr=np.array([[4,1,0],[4,2,0],[4,3,0],[4,1,0],[4,1,0]])
# label=np.array([1,1,0,0,1])
# label=np.mat(label).transpose()
# m=np.mat(arr)
# w=np.ones((3,1))
# er=label-logRegres.sigmoid(m*w)
# print(arr)
# print("\n")
# print(w)
# print("\n")
# print(m.transpose())
# print("\n")
# print(er)
# print("\n")
# print(0.001*m.transpose()*er)
#kNN.handwritingClassTest()
def sayHello():
    for i in range(5):
        print("I LOVE YOU!HELLO")
        time.sleep(2)
def sayBye():
    for i in range(5):
        print("I LOVE YOU!bye")
        time.sleep(2)
def main():
    print("create thread")
    t=threading.Thread(target=sayHello)
    t1=threading.Thread(target=sayBye)
    t.start()
    t1.start()
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()