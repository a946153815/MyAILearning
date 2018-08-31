import cvHelper
import numpy as np
import bayes
import numpy as np

#cvHelper.lhx_CameraPreview()
dataset,de=bayes.loadDataSet()
<<<<<<< HEAD
print(dataset)
group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
print(group.transpose(1,0))
=======
r=bayes.createVocabList(dataset)
bayes.testingNB()
>>>>>>> e88870b72a5b325083320bc28c74d7d6c5437a62
