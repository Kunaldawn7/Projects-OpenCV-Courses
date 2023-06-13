import numpy as np
import cv2


confThreshold = 0.5       # Confidence threshold
nmsThreshold = 0.4        # Non-maximum suppression threshold
inpWidth = 416            # Width of network's input image
inpHeight = 416           # Height of network's input image


tracker_type = "KCF"
classesFile = "coco.names"
classes = None

with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# Give the configuration and weight files for the model and load the network using them.
modelConfiguration = "yolov3.cfg"
modelWeights = "yolov3.weights"

net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)

def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i - 1] for i in net.getUnconnectedOutLayers()]


def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]
    
    classIds = []
    confidences = []
    boxes = []
    # Scan through all the bounding boxes output from the network and keep only the
    # ones with high confidence scores. Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > confThreshold and classes[classId] == 'sports ball':
                    center_x = int(detection[0] * frameWidth)
                    center_y = int(detection[1] * frameHeight)
                    width = int(detection[2] * frameWidth)
                    height = int(detection[3] * frameHeight)
                    left = int(center_x - width / 2)
                    top = int(center_y - height / 2)
                    classIds.append(classId)
                    confidences.append(float(confidence))
                    boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    
    
    for i in indices:
        box = boxes[i]
        left, top, width, height = box[0], box[1], box[2], box[3]
        cv2.rectangle(frame, (left, top), (left + width, top + height), (255, 178, 50), 2, 1)
           
    return frame, boxes


def detect(frame):
    
    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(frame, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)
    
    # Sets the input to the network
    net.setInput(blob)
    
    # Runs the forward pass to get output of the output layers
    outs = net.forward(getOutputsNames(net))
    #outs = net.forward()
    
    
    # Remove the bounding boxes with low confidence
    frame, bbox = postprocess(frame, outs)
    
    if len(bbox) > 0:
        return frame, bbox[0]
    
    else:
        return frame, -1


video = cv2.VideoCapture("soccer-ball.mp4")
ok, frame = video.read()

frame, bbox = detect(frame)
cv2.putText(frame, "Detection", (20,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0),2);


red = (0,0,255)
green = (0,255,0)

tracker = cv2.TrackerKCF_create()

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, tuple(bbox))

cv2.imshow("Video",frame)
k = cv2.waitKey(500)


count = 0
k = 0
ch = 0
ch1 = 0

while True:
    # Read a new frame
    ret, frame = video.read()
    
    if not ret or k == 27 or ch == 27 or ch1 == 27:
        break

    # Update tracker
    ok, bbox = tracker.update(frame)    

    # Draw bounding box
    if ok:
      # Tracking success
      p1 = (int(bbox[0]), int(bbox[1]))
      p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
      
      cv2.rectangle(frame, p1, p2, green, 2, 1)
      
      cv2.putText(frame, tracker_type + " Tracker", (20,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0),2);
                  
      cv2.putText(frame, "Status: Tracking going on...", (20,50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0),2);
                  
      cv2.imshow("Video",frame)
      ch = cv2.waitKey(50)
      
    else :
      # Tracking failure
      for i in range(10):
          
          ret, frame = video.read()
          if not ret:
              break
          frame_cpy = frame.copy()
          cv2.putText(frame_cpy, tracker_type + " Tracker", (20,20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0),2);
          cv2.putText(frame_cpy, "Status: Tracking failure detected", (20,50), 
                      cv2.FONT_HERSHEY_SIMPLEX, 0.75,red,2)
          cv2.imshow("Video",frame_cpy)
          ch1 = cv2.waitKey(25)
      
      
      frame, bboxes = detect(frame)
      
      if bboxes != -1:
          cv2.putText(frame, "Detection going on...", (20,20), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,150,10),2)
          
          #tracker.release()
          tracker = cv2.TrackerKCF_create()

          # Initialize tracker with first frame and bounding box
          ok = tracker.init(frame, tuple(bboxes))    
          
      cv2.imshow("Video",frame)
      k = cv2.waitKey(300)
    

video.release()
cv2.destroyAllWindows()
    
    