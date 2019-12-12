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
將該問題視為資料關聯問題，使用的cost matrix為**原有目標在當前frame中的預測框**與 **當前frame所測量到的實際框之間IOU**
小於特定IOU則是無效的，且作者發現使用IOU當作指標能夠解決目標短時間被遮擋的問題[解釋1]

##### IOU
IOU - intersection-over-union

#### Metrics
MOTA (Multi-object tracking accuracy)
MOTP (Multi-object tracking precision)
...
a lot, see in code

# Hungarian Algorithm 原理
* 任務分配問題, 組合最佳化, 增廣路徑, 二分圖最大匹配
* 時間複雜度O($N^{3}$)
## 形象化描述
你通過數代人的努力，你終於趕上了剩男剩女的大潮，假設你是一位光榮的新世紀煤人，手上有$N$個剩男，$M$個剩女，每個人都可能對多名異性個有好感，如果一對男女互相有好感，就可以把這一對湊合再一起，現在讓我們暫且無視所有單相思，你會有一張圖，每一條連線都表示互相有好感

<img src='./images/MOT_1.png'></img>

湊合勁量多對情侶的情況下
先給一號男生找妹子，發現第一個和它相連的1號女生還名花無主，got it!

<img src='./images/MOT_2.png'></img>

接著發現2號可以相連到2號

<img src='./images/MOT_3.png'></img>

接著要連線3號，但是3號喜歡1號，怎麼辦呢
我們先把1號男對1號女拆掉(黃色)，我們幫1號男重新找妹子

<img src='./images/MOT_4.png'></img>

結果發現1號男第2喜歡的是2號女，但是2號女被2號男佔走了，怎麼辦呢？
我們把2號男對2號女拆掉，試著給2號男找新的妹子(和1號相比這是一個遞迴!)

<img src='./images/MOT_5.png'></img>

接下來發現2號男要找的3號妹子，沒人選!太棒了，2號男找3號女，1號男找2號女，3號男找1號女，回溯回去解出答案!（藍色線表示配對成功!）

<img src='./images/MOT_6.png'></img>

總結來說，3個步驟之後的配對結果

<img src='./images/MOT_7.png'></img>

接下來是4號男，他喜歡3號妹子!但是如果按照上面弟回的步驟，沒辦法幫其他男生在找妹子了!
4號男gg，無法配對!

本版本的原則我們看得出來，有機會就上，沒機會，roll back看看有沒有機會，挪一挪有機會，就再上!

### 需要改進處
這裡顯示每一條連結是等價的，也就是1號男對1,2,3女喜歡程度相當，所以能夠輕易切換，我們可以給每一條連結加上權重，也就是所謂的Kuhn-Munkres演算法(KM算法)，基本上就是一種升級

## 數學，形象化各半
### 二分圖
匈牙利算法與KM算法都是為了**求解二分圖最大分配問題**
二分圖是啥，能夠分成兩組，U和V，其中U的點不能相互聯通，只能去連V的點，同理，V的點不能互相連通，只能連U的點，這樣的規則下，就稱為二分圖，我們可以發現，目標追蹤在上一個frame，時間$t-1$以及當前的frame時間$t$，各自為二分圖的一邊，目標追蹤即可視為一個二分圖問題，而目標跟蹤就演變成一個**二分圖的最大匹配問題**

<img src='./images/MOT_8.png'></img>

## 改進版本 KM算法(Jugn-Munkres Algorithm)

這次我們將set $U$以及set$V$換成$frame_{t}$以及$frame_{t+1}$所被識別出來的物件
並且給每條連結關係加入權重，這也是我們算法中其他模組給出的志信度分數值
而左邊的頂點賦值為最大權重，右邊賦值為0[註2]

<img src='./images/MOT_9.jpg'></img>

# Code
[star : 1.3k](https://github.com/abewley/sort)

# 註釋
1. abc
2. 我們的Tracking Module是協助classification的，換句說我們沒有一個考靠的置信分數(confidence score)，我們需要用另外的值來取代這個link weight