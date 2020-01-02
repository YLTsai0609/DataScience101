# The 5 Computer Vision Techniques That Will Change How You See The World
* Author : James Le
* 4.2k+ claps
* [Link](https://heartbeat.fritz.ai/the-5-computer-vision-techniques-that-will-change-how-you-see-the-world-1ee19334354b)

### Image Classification
* Convolutional Neural Networks (CNNs) - using sliding window to extract features
* ImageNet
* AlexNet
* ZFnet
* GoogLeNet
* VGGNet
* ResNet(2015)
* DenseNet(2016)
### Object Detection
The task to define objects within images usually involves outputting bounding boxes and labels for individual objects. This differs from the classification / localization task by applying classification and localization to many objects instead of just a single dominant object. You only have 2 classes of object classification, which means object bounding boxes and non-object bounding boxes. For example, in car detection, you have to detect all cars in a given image with their bounding boxes.
* Sliding window 
* Selective Search
* Region-based CNN (RCNN), CNN(feature extractor), SVM(classification), Linear Regression(tighten bounding box)
* Fast R-CNN
* Faster R-CNN
* You Only Look Once(YOLO)
* Single Shot MultiBox Detector(SSD)
* Region-Based Fully Convolution Networks(R-FCN)
### Object Tracking
Divided into 2 categories : generated methods, discriminative method
* gererative method : PCA - reconstruction error to search the object
* discriminative method : stacked auto encoder(SAE), CNN
* fully-convolution network tracker(FCNT)
  * CNN feature maps can be used for **localization and tracking**
  * Many CNN features are noisy or un-related for the task of object from background
  * GNet, SNet
* multi-domain CNN(MD Net)
### Sematic Segmentation
* Fully Convolution Networks (FCN)
* SegNet
### Instance Segmentation
* Mask R-CNN

### Tutorial and Github
[Stanford University School of Engineering](https://www.youtube.com/watch?v=nDPWywWRIRo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=11)
[Code on class Star 300, Fork 171](https://github.com/khanhnamle1994/computer-vision)