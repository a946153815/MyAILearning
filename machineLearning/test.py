import numpy as np
import pandas as pd
from pandas import DataFrame, Series

import bayes
import cvHelper
import logRegres

#cvHelper.lhx_CameraPreview()
#dataset,de=bayes.loadDataSet()
#r=bayes.createVocabList(dataset)
#bayes.testingNB()0
#arr=Series([1,2],index=['dd','db'])
#print(arr)
arr=np.array([[4,1,0],[4,2,0],[4,3,0],[4,1,0],[4,1,0]])
m=np.mat(arr)
w=np.ones((3,1))
print(logRegres.sigmoid(m*w))
