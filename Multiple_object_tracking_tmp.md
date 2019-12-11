1. 多目標追蹤 https://blog.csdn.net/sinat_26917383/article/details/86557399
2. kalman numpy實現, YOLO辯識 + kalman + 匈牙利，追蹤 https://blog.csdn.net/xiao__run/article/details/84374959
3. Kalman + 匈牙利 + Gaussian Mix Modeling https://blog.csdn.net/xiao__run/article/details/77478579
4. Object Tracking using OpenCV https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/
5. OpenCV中的目標追蹤算法介紹 : https://kknews.cc/zh-tw/tech/jl2y94y.html

# Introduction
多目標追蹤的Intro, SORT以及Deep SORT
[Ref 1] (https://zhuanlan.zhihu.com/p/59148865)
多目標追蹤的3種門派
[Ref 2] (https://zhuanlan.zhihu.com/p/77111218)

# Hungarian Algorithm + kalman filter framework
## 2nd introduction
#### State vector
* 假設, frame與frame之間進行等速度運動(所以需要夠高的FPS來輔助)
$$
x = [u, v, s, r, \dot{u}, \dot{v}, \dot{s}]^{T}
$$
x表示每個目標狀態 : u, v 為目標中心的x座標, y座標, s, r為目標BBox的尺寸大小以及比例, 且長寬比應該為一個常數, 後3項則為相對應的速度項
#### data association
將該問題視為資料關聯問題，使用的cost matrix為**原有目標在當前frame中的預測框**與**當前frame所測量到的實際框之間IOU**
小於特定IOU則是無效的，且作者發現使用IOU當作指標能夠解決目標短時間被遮擋的問題[解釋1]
##### IOU
IOU - intersection-over-union

#### Metrics
MOTA (Multi-object tracking accuracy)
MOTP (Multi-object tracking precision)
...
a lot, see in code

# Code
[star : 1.3k](https://github.com/abewley/sort)