import numpy as np
import cv2

points=[]
point=()

def on_mouse(action, x, y, flags, userdata):
        # Referencing global variables 
        global point, points, img
        
        ht, width = img.shape[:2]
        
        if action==cv2.EVENT_LBUTTONDOWN:
            point = (x,y)
            #print(point)
            
            
        elif action==cv2.EVENT_LBUTTONUP:
            
            if (((point[0] - 15) >=0 and (point[0] + 15) <= width) and ((point[1] - 15) >=0 and (point[1] + 15) <= ht)):
                patch = img[point[1]-15:point[1]+15, point[0] - 15:point[0]+15]
                
                
            else:
                pt1 = np.clip(point[0] - 15,0,width)
                pt2 = np.clip(point[0] + 15,0,width)
                pt3 = np.clip(point[1] - 15,0,ht)
                pt4 = np.clip(point[1] + 15,0,ht)
                
                patch = img[pt3:pt4, pt1:pt2]
                
                patch = cv2.resize(patch,(30,30))
            
            output = cv2.GaussianBlur(patch,(25,25),50,50)
            mask = 255 * np.ones(output.shape, output.dtype)
            img = cv2.seamlessClone(output,img, mask, point, cv2.NORMAL_CLONE)
                
            
        cv2.imshow("Blemish Remover", img)
            
            

img = cv2.imread("blemish.png")

cv2.namedWindow("Blemish Remover")

cv2.setMouseCallback("Blemish Remover", on_mouse)



k = 0
# loop until escape character is pressed
while k!=27 : 
    
    cv2.imshow("Blemish Remover", img)
        
    k = cv2.waitKey()
              
        
cv2.destroyAllWindows()
