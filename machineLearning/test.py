import cvHelper
import bayes
import numpy as np

#cvHelper.lhx_CameraPreview()
dataset,de=bayes.loadDataSet()
print(dataset)
group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
print(group.transpose(1,0))