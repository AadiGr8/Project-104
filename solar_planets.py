import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(2,255,255))

cv2.putText(img,"Mercury",(110,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.4,(200,25,255))

cv2.putText(img,"Venus",(200,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.6,(2,25,25))

cv2.putText(img,"Earth",(300,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.7,(20,55,255))

cv2.putText(img,"Mars",(400,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.6,(240,2,25))

cv2.putText(img,"Jupiter",(500,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(2,25,255))

cv2.putText(img,"Saturn",(730,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(180,5,255))

cv2.putText(img,"Uranus",(960,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(100,100,100))

cv2.putText(img,"Neptune",(1100,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(200,5,5))


cv2.imshow("output",img)
cv2.waitKey(0)
