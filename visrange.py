import cv2
import numpy as np
import easygui

img=cv2.imread('sample_image/smog.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


barely=[]
clearly=[]
notvis=[]
def classify(corners,distance):
	if(corners>=15):
		clearly.append(distance)
		return ("clearly visible",(0,255,0))

	elif(corners>1 and corners<15):
		barely.append(distance)
		return ("barely visible",(0,200,200))
	else:
		notvis.append(distance)
		return ("not visible",(0,0,255))

coords=[]
distances=[]
count=0
def mouseRGB(event,x,y,flags,param):
	global xmouse,ymouse,count
	if event == cv2.EVENT_LBUTTONDOWN: 
		coords.append((x,y))
		if count%2==1:
			cv2.rectangle(img,coords[count-1],coords[count],(255,0,0),2)
			cv2.imshow('img',img)
			dst=easygui.enterbox("enter landmark distance in km")
			distances.append(int(dst))
		count+=1

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouseRGB)

cv2.imshow('img',img)
cv2.waitKey(0)


print(f'distances:{distances}')
gray=np.float32(gray)
mask=cv2.cornerHarris(gray,2,3,0.04)
mask=cv2.dilate(mask,None)
ret, mask = cv2.threshold(mask,2000,255,0)
mask=np.uint8(mask)
img[mask.astype(bool)]=[0,0,255]


for i in range(0,len(coords),2):
	c1=coords[i]
	c2=coords[i+1]
	x1,y1,x2,y2=c1[0],c1[1],c2[0],c2[1]
	patch=mask[y1:y2,x1:x2]
	centroids=cv2.connectedComponentsWithStats(patch)[3].astype(int)
	corners=len(centroids)
	result,color=classify(corners,distances[int(i/2)])
	cv2.rectangle(img,c1,c2,color,2)
	cv2.putText(img,str(result),c1,cv2.FONT_HERSHEY_SIMPLEX,1,color, 2)

clearly=sorted(clearly)
barely=sorted(barely)
notvis=sorted(notvis)


if(len(notvis)==0): 
	visrange=(barely[-1] if len(barely)!=0 else clearly[-1])
elif(len(barely)!=0): visrange=(barely[-1]+notvis[0])/2
elif(len(barely)==0 and len(clearly)!=0): visrange=(clearly[-1]+notvis[0])/2
else: visrange=0

cv2.putText(img,'visiblity: '+str(visrange)+'km',(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,200), 2)

with open('visrange.txt','w') as file:
	file.write(str(visrange)+'km')
print(f'visibility range: {visrange} km')

cv2.imshow('out',img)
#cv2.imwrite('result.jpg',img)
cv2.waitKey(0)
