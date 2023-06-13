import cv2
import numpy as np


mean_hsv = 0

tolerance = 0
max_tolerance = 100

blurAmount = 0
maxBlurAmount = 50

tol_mask = 0
blend = 0

def on_mouse(action, x, y, flags, userdata):
  # Referencing global variables 
  global top_left,bottom_right,mean_hsv
  
  if action==cv2.EVENT_LBUTTONDOWN:
    top_left=(x,y)
    

  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    bottom_right=(x,y)
    
    if bottom_right[0] == top_left[0] or bottom_right[1] == top_left[1]:
        green_patch  = frame[top_left[1]:bottom_right[1] + 15 ,top_left[0]:bottom_right[0] + 15]
        
    else:
        minx = min(top_left[0],bottom_right[0])
        maxx = max(top_left[0],bottom_right[0])
        miny = min(top_left[1],bottom_right[1])
        maxy = max(top_left[1],bottom_right[1])
        
        green_patch  = frame[miny:maxy,minx:maxx]
    
    mean_patchB = int(np.round(np.mean(green_patch[:,:,0])))
    mean_patchG = int(np.round(np.mean(green_patch[:,:,1])))
    mean_patchR = int(np.round(np.mean(green_patch[:,:,2])))
    
    mean_patch = np.array([[[mean_patchB,mean_patchG,mean_patchR]]], dtype = np.uint8)
    mean_hsv = cv2.cvtColor(mean_patch,cv2.COLOR_BGR2HSV)
        

def BackgroundRemove(frame, mean_hsv, tol, blur):
    
    if tol > 0:
        min_tol = mean_hsv[0,0,0] - tol
        max_tol = mean_hsv[0,0,0] + tol
    
        masked_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        
            
        lower_value = np.array([min_tol,50,50])
        upper_value = np.array([max_tol,255,255])
        tol_mask = cv2.inRange(masked_image, lower_value, upper_value)
    
        
    bl = cv2.GaussianBlur(tol_mask, (2 * blurAmount + 1, 2 * blurAmount + 1),0);
    alpha = cv2.cvtColor(bl, cv2.COLOR_GRAY2BGR)/255.0
    blend = cv2.convertScaleAbs(frame*(1-alpha))
    
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_green = np.array([min_tol, 50, 50])
    upper_green = np.array([max_tol, 255, 255])
    mask = cv2.inRange(masked_image, lower_green, upper_green)
    
    cbg = crop_background.copy()
    
    cbg[mask == 0] = 0
    
    final_image = cbg + blend

    
    return final_image
        
    
def apply_BackgroundRemoval(mean_hsv):
    
    if tolerance > 0:
        min_tol = mean_hsv[0,0,0] - tolerance
        max_tol = mean_hsv[0,0,0] + tolerance
    
        masked_image1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
        if min_tol < 0:
            lower_value = np.array([0,10,0])
        
        else:
            lower_value = np.array([min_tol,50,0])
        
        
        upper_value = np.array([max_tol,255,255])

        tol_mask = cv2.inRange(masked_image1, lower_value, upper_value)
    
        msk = cv2.bitwise_and(frame,frame, mask = 255-tol_mask)

    
        cv2.imshow("Chroma Keying",msk)
    
    
    if blurAmount > 0:
        bl = cv2.GaussianBlur(tol_mask, (2 * blurAmount + 1, 2 * blurAmount + 1),0);
        alpha = cv2.cvtColor(bl, cv2.COLOR_GRAY2BGR)/255.0
        blend = cv2.convertScaleAbs(frame*(1-alpha))
    
        cv2.imshow("Chroma Keying",blend)
    



def tolerance_slider( *args ):
    global tolerance
    tolerance = args[0]
    apply_BackgroundRemoval(mean_hsv)
    pass
    
    
def smoothness( *args ):
    global blurAmount
    blurAmount = args[0]
    apply_BackgroundRemoval(mean_hsv)
    pass
    
    
print("Usage: python <filename>.py") 
print("\nDue to significant amount of processing and slowness of Python, the video frames are slowed down during processing...")
print("\nSteps to be followed...")
print("1. Press spacebar to pause a video frame which needs to be processed (as per user's choice).")   
print("2. Select a green patch from the background.")   
print("3. Use the tolerance and softness slider to process the video frame.")   
print("4. Press Esc when finished.")   

    
cap = cv2.VideoCapture("greenscreen-demo.mp4")

bg = cv2.imread("universe.jpg")
crop_background = cv2.resize(bg,(1920,1080))

cv2.namedWindow("Chroma Keying",cv2.WINDOW_NORMAL)

cv2.setMouseCallback("Chroma Keying", on_mouse)
cv2.createTrackbar("Tolerance", "Chroma Keying", tolerance, max_tolerance, tolerance_slider)
cv2.createTrackbar("Smoothness", "Chroma Keying", blurAmount, maxBlurAmount, smoothness)


frame_count=0
ch = 0
k=0
while(cap.isOpened()):
    
    # Read frame
    ret,frame = cap.read()
    
    
    if ch == 32:
        cv2.imshow("Chroma Keying",frame)
        k = cv2.waitKey()
        
        
    cv2.imshow("Chroma Keying",frame)
    
    frame_count+=1  
    
    ch = cv2.waitKey(29) & 0xFF
      
    if ch == 27 or k == 27 or (not ret):
        break



cap.set(cv2.CAP_PROP_POS_FRAMES, 0) 


frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


outmp4 = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 10, (frame_width,frame_height))

k=0    
while(cap.isOpened()):
    
    ret,frame = cap.read()
    
    if ret == True:
        image_blend = BackgroundRemove(frame, mean_hsv, tolerance, blurAmount)
        outmp4.write(image_blend)
        
        cv2.imshow("Chroma Keying",image_blend)
        k = cv2.waitKey(1)
        
    if not ret or k == 27:
        break
 
        


cap.release()
outmp4.release()
cv2.destroyAllWindows()
