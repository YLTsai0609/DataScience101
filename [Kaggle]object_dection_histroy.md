# Object Detection Techniques
Object Detection Techniques | Kaggle 重點節錄
* [Kaggle NoteBook](https://www.kaggle.com/infernop/object-detection-techniques)
* [講者 - AdamyaTripathi Vote : 33](https://www.kaggle.com/rtatman/kernels?sortBy=dateCreated&group=everyone&pageSize=20&userId=1162990)

# Hsitory (2001 - 2017)
1. The first efficient Face Detector (Viola-Jones Algorithm, 2001)
    * 可以即時辨識(real time)
    * 被實作在openCV中，稱作Viola and Jones algorithm.
    * 概念
      1. 拿一堆face data
      2. 硬幹一些臉部特徵(feature of a face)
      3. SVM
      4. 模型上線 
<img src = 'images/object_dection_1.png'></img>
* 缺點 : 臉一但轉一下角度，往轉，下轉，或是wearing a mask, 就掛了
2. Much more efficient detection technique (Histograms of Oriented Gradients, 2005)
   * 同樣hardcode臉部特徵 
   * 對於每個pixel, 看他周圍的pixel, 去辨識該pixel周圍的pixel有多黑?
   * 往最黑的方向取一個gradient，當作此pixel的gradient
   * 對每個pixel都做這件事
   * 這樣的gradient可以展示出整張圖片亮暗之間的Flow
   * 這種特徵萃取方式稱作HOG(Histograms of Oriented Gradients)
<img src = 'images/object_dection_2.png'></img>
* 缺點 : 或多或少減緩了Viola-Jones Algorithm, 2001的問題，但扔然是一種hardcode的方式，一但noise變大，或是背景東西一多，就分不好了
##  Deep Learning Era begins(2012)
1. CNN
2. R-CNN
   * 一些更新版本 R-CNN, Fast R-Cnn, Faster R-CNN, Mask R-CNN
3. YOLO
   * YoLO v1, v2, v3 
