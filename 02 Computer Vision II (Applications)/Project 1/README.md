# <img src = "https://opencv.org/wp-content/uploads/2021/06/OpenCV_logo_black_.png">  Computer Vision II (Applications)

In this Project, we have tried to build a virtual makeup application using facial landmarks. The application consists of two features:



### Feature 1: Hair Segmentation

For the first feature, the hair color of the girl  is changed using seamless cloning and saturation.

The hair segmentation is carried out using OpenCV's **grabCut** feature to generate a segmentation mask.

Then we saturate the hair color of the girl to a certain value by converting the image into **HSV** color space and change the saturation value.

Once, this is done, we apply seamless cloning with **NORMAL_CLONE** to the segmented hair and the original image.



### Feature 2: Applying Lipstick and Glasses

For the second feature, we have applied lipstick and glasses to the modified image in **Feature 1**.

Again for the lipstick part, we have applied OpenCVs **grabCut** feature to generate a mask of lips. After this, landmark points are manually added using **imglab** tool ( [https://imglab.in/](https://imglab.in/ ) ) and saved to `lips_landmarks.txt`.

We then calculate the **Delaunay triangles** with respect to the landmark points of the lips.

We also find the landmark points of the image and only use the landmark points of the mouth as the feature points (i.e. indices: 48, 49, ..., 67 in **dlib's** 68-point predictor). We then warp triangles for the lips and the alpha mask as well. The generated mask is then blurred using Gaussian Blur.

Finally we apply alpha blending to the warped lips and the image.


 Additionally, we added a pair of glasses to the image using alpha blending. The width and height are computed using simple heuristics. For instance, the glass width is computed using the width difference of the jawline (i.e., difference between the x coordinates of dlib's landmarks points 1 and 16), and the height is computed by maintaining the aspect ratio.

Finally, alpha blending is applied to the glasses and the image.

**P.S.**: We might get better results if **Delaunay triangulation** and **triangle warping** is used for the glasses!



A sample output is shown below:

![c2_project1_virtual_makeup](https://github.com/Kunaldawn7/Projects-OpenCV-Courses/assets/47062478/de0639a1-67dd-4db8-87fe-50acd0055cc5)


---
