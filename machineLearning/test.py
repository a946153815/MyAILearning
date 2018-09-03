import numpy as np
from math import log
import bayes
import cvHelper

#cvHelper.lhx_CameraPreview()
dataset,de=bayes.loadDataSet()
print(dataset)
group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
print(group.transpose(1,0))
bayes.createVocabList(dataset)
bayes.testingNB()
print(log(log(5)))
