import cvHelper
import numpy as np
import bayes
#cvHelper.lhx_CameraPreview()
dataset,de=bayes.loadDataSet()
r=bayes.createVocabList(dataset)
bayes.testingNB()