# <img src = "https://opencv.org/wp-content/uploads/2021/06/OpenCV_logo_black_.png">  Computer Vision III (Deep Learning with PyTorch)

The notebook: `Project2_License_Plate_Detection.ipynb` was used to build a License Plate Detector Model.

### About the Dataset

The dataset consisted of `5694` images samples of in **License plates**.  A few samples are shown below.

![](./visuals/license-plate-data.png?raw=true)

Out of these `5694` image samples,  `5308` samples consisted of the train data and `386` samples from the validation data.

The annotations are in the form of `[xmin, ymin, xmax, ymax]` format. The dataset shared the following hierarchy:

```
Dataset
├── train
│  └── Vehicle registration plate
│      └── Label
└── validation
    └── Vehicle registration plate
        └── Label
```



---

### Detection Model used for Fine-tuning

[RetinaNet ResNet50 FPN 3x](https://github.com/facebookresearch/detectron2/blob/main/MODEL_ZOO.md#retinanet) was used for fine-tuning on the dataset.



### Training Hyperparameters:

* Batch size: `8`

* Epochs: `2`; Iterations: `int(epoch * train_img_count / BATCH_SIZE`  = `1327`

* Initial LR: `1e-4`

  

### Evaluation Metrics

The final COCO primary metric (**mAP@0.5:0.95**) was **`0.553`**, while the **mAP@0.5** (VOC metric) was **`0.817`**. The overall metric statistics is:

```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.553
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.817
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.672
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.184
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.659
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.663
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.518
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.645
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.663
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.389
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.748
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.751
```



The tensorboard logs can be found [here](https://tensorboard.dev/experiment/51u0JVyzRPSQykdDZLjphw/).


### Sample Video Inference


https://github.com/Kunaldawn7/Projects-OpenCV-Courses/assets/47062478/de385e33-e02b-4ac3-9bce-6c1d64264d56

---

