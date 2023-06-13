# <img src = "https://opencv.org/wp-content/uploads/2021/06/OpenCV_logo_black_.png">  Computer Vision I (Introduction)

In this project, we have created a **Video Analysis** application that performs detection and tracking. 

Specifically, the application performs 2 tasks:

1. Detecting the soccer ball using **YOLOv3**.
2. Perform tracking using **KCF** tracker.

If the application looses tracking, we continue looking for the next `n` frames (in our case, `n`is set to `10`) until the detector is able to detect the soccer ball again. Subsequently, the tracker then takes over for tracking it further.



One can start the application by running:

`python c1_project2_detect_and_track.py`


A sample video output is shown below.


![c1_project2_detection_and_tracking](https://github.com/Kunaldawn7/Projects-OpenCV-Courses/assets/47062478/9590c14f-e931-4e31-9552-0ee66d35500a)


---

