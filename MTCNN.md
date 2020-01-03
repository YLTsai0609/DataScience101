# MTCNN
* Multi-task Cascaded Convolutional Networks
* [Ref 1](https://blog.csdn.net/fuwenyan/article/details/73201680)
* [Ref 2](https://blog.csdn.net/fuwenyan/article/details/77573755?fbclid=IwAR17XKFkn2RNiK_ZP1WQ947rpSggVEW0HgaNENkc7X7WB70w2kwpuJ8GV6o)
* [論文 引用1227次， IEEE, Signal Processing, 2016年](https://arxiv.org/pdf/1604.02878.pdf)
* Object Detection
* 是否能夠看到各種臉的偵測分數，以及沒有通過Net的原因? 能否簡單地調整閥值，讓臉能夠被偵測到?
* Pnet -> Rnet -> Onet
* 基本上是三個網路串連來輸出face confidence shape = (1,1,2), bounding box(x1, y1, w, h) shape = (1,1,4), facial landmark localization shape = (1,1,10)，所以輸出非常多東西
* 本質上就是淺層的網路架構，透過Boosting的方式來實作
* 從粗略到細緻
* 困難樣本生成策略可以進一步提升性能
每個階段的網路都是一個多任務網路，處理任務有3個

1. 人臉/非人臉 - cross-entropy
   * face confidence shape = (1,1,2) 
   $math formula$
2.  bounding box - 回歸MSE
   * $math formula$
3.  特徵點定位
   * 歐式距離損失函數
   * $math formula$
   * $alpha$三個任務中在當前階段的網路中損失所佔比重，$\beta$採樣類型指示, 取值為{0,1}，非人臉時，box和landmark的$\beta=0$，$det=1$，人臉時，$\beta=1$，$det=1$

## 詳述
1. Preprocessing:resize
2. 淺層CNN，全卷積層，P-Net，獲取候選人臉窗口以及人臉回歸向量，基於人臉回歸向量時對候選窗口進行校正，之後採用NMS合併高重疊率的候選窗口(IOU threshold)
3. P-Net的$\alpha$取值為{1.0, 0.5, 0.5}