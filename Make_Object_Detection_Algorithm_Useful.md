# Resource
[目标检测算法工程落地 57贊同](https://zhuanlan.zhihu.com/p/69544506?fbclid=IwAR3VHc9R6jA8Qqhv1tc0bUjDPbVQJJYWafXZvlJ53Aal9YIBpxFRoaxvB8g)

<img src='./images/makeObjUseful_1.png'></img>

兩個重點

# backbone選取以及針對realtime的調參手法
網路選取 : 考慮realtime，以及硬體性能，以下幾點是優先選擇
* 參數量小的網路(例如MobileNet系列，現在已經出到v3)
  * 以往都是用VGG，現在使用mobilev2, 可以大幅提升速度
* 更傾向單階段(yolo/ssd的變形結構)
* 初始化，網路蒸餾，去除掉某些基礎特徵層，都是讓網路變小但是精確度損失較小的技巧
* anchor及損失函數的權重會根據你的資料集有不同的影響


# 工程化
* PC端到Edge端
* C++接口開發，並將預測結果提供給Edge端相關軟體，再現實測然後並行修改