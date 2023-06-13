# <img src = "https://opencv.org/wp-content/uploads/2021/06/OpenCV_logo_black_.png">  Computer Vision I (Introduction)

This Project contains 2 features:

* Blemish Removal
* Chroma Keying



## 1 Blemish Removal

The objective of this application is to remove blemishes from the screen. This is acheived using:

* **Mouse Callbacks**
* **Gaussian Blur**
* **Seamless Cloning**

You can simply run the following command:

`python c1_project1_feature1.py`

The output below shows the results:



<img src = "https://www.dropbox.com/s/fsnxptu4xjoy29q/c1_project1_feature_1_blemish_removal.gif?dl=1">

---



## 2 Chroma Keying (Green Screen Removal)

The objective of this feature is to build a robust application for green screen matting or chroma keying. This technique is routinely used in the movie and television industry to replace the background of the actor, newscaster, or weatherman.

The application has the following controls:

1. *Color Patch Selector* : The interface displays a video frame and the user can select a patch of green screen from the background. 

2. *Tolerance slider* : This slider controls how different the color can be from the mean of colors sampled in the previous step to be included in the green background.

3. *Softness slider*: This slider will control the softness of the foreground mask at the edges.

   

After running the script using:

`python c1_project1_feature2_chroma_keying.py`

you need to perform the following steps:

1. Press `spacebar` to pause a video frame which needs to be processed (as per user's choice).
2. Select a **green patch** from the background.
3. Use the **tolerance** and **softness** sliders to process the video frame.
4. Press `Esc` when finished.

A sample output is shown below:

<img src = "https://www.dropbox.com/s/6aeii55s75awwhr/c1_project1_feature_2_chroma_keying.gif?dl=1">

---

