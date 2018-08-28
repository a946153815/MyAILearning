import operator
from imp import reload

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import cv2


#摄像头预览
def lhx_CameraPreview():
	cap=cv2.VideoCapture(0)
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Our operations on the frame come here
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		# Display the resulting frame
		cv2.imshow('frame',gray)
		if cv2.waitKey(1)  == ord('q'):
			break
		elif cv2.waitKey(2)  == ord('p'):
			cap.release()
			cv2.destroyAllWindows()
			return gray;
	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
#时间计数器
def lhx_getTicketCount():
	return cv2.getTickCount()
#计算程序运行耗时
def lhx_getApplicationRuntime(e2,e1):	
	time = (e2 - e1)/ cv2.getTickFrequency()
	return time
#图片信息
def lhx_getImageShapeInfo(path):
	img=cv2.imread(path)
	return img.shape
#
def lhx_threshold(image):
    	"""图像二值化：全局阈值"""
    	#图像灰度化
    	gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    	#变为二值图像
    	#gary：灰度图像
    	#0：阈值，如果选定了阈值方法，则这里不起作用
    	ret ,binary=cv2.threshold(gray,0,255,cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    	return binary
 
 #
def lhx_local_threshold(image):
    	"""局部阈值"""
    	# 图像灰度化
    	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    	# 变为二值图像
    	binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,10)
    	return binary
 #
def lhx_custom_threshold(image):
    	"""局部阈值"""
    	# 图像灰度化
    	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    	h,w=gray.shape[:2]
    	m=np.reshape(gray,[1,w*h])
    	mean=m.sum()/(w*h)
    	# 变为二值图像
    	binary = cv2.threshold(gray,mean,255,cv2.THRESH_BINARY)
    	return binary
#
def lhx_Otsu_threshold(img):
	# Otsu's thresholding after Gaussian filtering
	# ( 5,5 )为高斯核的大小, 0 为标准差
	blur = cv2.GaussianBlur(img,(5,5),0)
	# 阈值一定要设为 0 !
	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	return th3
	
#
def lhx_2D_Convolution(img):
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	return dst
########图像模糊(图像平滑)
#平均
def lhx_average(img):
	return cv2.blur(img,(5,5))
#高斯模糊
def lhx_GaussisanBlur(img):
	return cv2.GaussianBlur(img,(5,5),0)	

# 中值模糊
def lhx_MedianBlur(img):
	return cv2.medianBlur(img,5)

#腐蚀
def lhx_Erode(img):
	kernel = np.ones((5,5),np.uint8)
	erosion = cv2.erode(img,kernel,iterations = 1)
	return erosion
#膨胀
def lhx_Dilate(img):
	kernel = np.ones((5,5),np.uint8)
	return cv2.dilate(img,kernel,iterations = 1)

#开运算
def lhx_MorphologyOpenEx(img):
	kernel = np.ones((5,5),np.uint8)
	return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#闭运算
def lhx_MorphologyCloseEx(img):
	kernel = np.ones((5,5),np.uint8)
	return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#Canny 边缘检测
def lhx_Canny(img):
	edges = cv2.Canny(img,100,200)
	return edges

#轮廓
def lhx_FindContours(img):
	imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(imgray,127,255,0)
	return cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
def lhx_DrawContours(img, contours):
	return cv2.drawContours(img, contours, 3, (0,255,0), 3)	

#模板匹配
def lhx_templateMatch(img,template,meth):
	img2 = img.copy()
	w, h = template.shape[::-1]
	# All the 6 methods for comparison in a list
	methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
	'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
	img = img2.copy()
	#exec 语句用来执行储存在字符串或文件中的 Python 语句。
	#例如,我们可以在运行时生成一个包含 Python 代码的字符串,然后使用 exec 语句执行这些语句。
	#eval 语句用来计算存储在字符串中的有效 Python 表达式
	method = eval(methods[meth])
	# Apply template Matching
	res = cv2.matchTemplate(img,template,method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	# 使用不同的比较方法,对结果的解释不同
	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		top_left = min_loc
	else:
		top_left = max_loc
	bottom_right = (top_left[0] + w, top_left[1] + h)
	cv2.rectangle(img,top_left, bottom_right, 255, 2)
	return img,top_left, bottom_right
#
def lhx_GrabCut(img,rect):
	mask = np.zeros(img.shape[:2],np.uint8)
	bgdModel = np.zeros((1,65),np.float64)
	fgdModel = np.zeros((1,65),np.float64)
	# 函数的返回值是更新的 mask, bgdModel, fgdModel
	cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
	mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
	img = img*mask2[:,:,np.newaxis]
	return img

#Harris 角点检测
def lhx_HarrisCornorCheck(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	#• img - 数据类型为 float32 的输入图像。
	#• blockSize - 角点检测中要考虑的领域大小。
	#• ksize - Sobel 求导中使用的窗口大小
	#• k - Harris 角点检测方程中的自由参数,取值参数为 [0,04,0.06]
	# 输入图像必须是 float32 ,最后一个参数在 0.04 到 0.05 之间
	dst = cv2.cornerHarris(gray,2,3,0.04)
	#result is dilated for marking the corners, not important
	dst = cv2.dilate(dst,None)
	return dst
