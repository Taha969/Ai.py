import cv2
import easyocr

img = cv2.imread('AI.py.png')

reader = easyocr.Reader(['en'] , gpu=False)
result = reader.readtext(img)

for text in result:
    p1 = text[0][0]
    p2 = text[0][2]
    detctedText = text[1]
    
    
    cv2.rectangle(img, p1, p2,  (0, 255, 0 ), 3)
    cv2.putText(img, detctedText, p1, cv2.FONT_HERSHEY_COMPLEX, 0.75,(255, 0,150 ), 3)

cv2.imshow('Image', img)
cv2.waitKey(0)
