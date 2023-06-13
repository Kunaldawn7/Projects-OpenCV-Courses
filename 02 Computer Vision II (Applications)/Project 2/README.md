# <img src = "https://opencv.org/wp-content/uploads/2021/06/OpenCV_logo_black_.png">  Computer Vision II (Applications)

For this project, we have fine-tuned **YOLOv3** and **YOLOv4** detection models from  AlexeyAB's **DarkNet** [repository](https://github.com/AlexeyAB/darknet ).

The models have been fine-tuned to detect faces of persons with and without masks.

After training both the models, the evaluation metric (**mAP @ 0.5**) are approximately similar. However, on real life video inferences, **YOLOv4** appears to perform slightly better.



The metrics plots for both YOLOv3 and YOLOv4 are shown below:

```
| **YOLOv3** | **YOLOv4** |
| ---------|----------|
| ![](./YOLOv3/map_yolov3.png?raw=true)    | ![](./YOLOv4/map_yolov4.png?raw=true) |
```



Finally, we comparison through inferences across a few video samples:

#### Video 1:



#### Video 2:



The video inference samples can be downloaded from [here](https://www.dropbox.com/s/o2nupjhbmym2q7n/yolo_v3_v4_video_inferences.zip?dl=1).

---
