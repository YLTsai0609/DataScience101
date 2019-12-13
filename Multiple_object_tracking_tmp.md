1. [多目標追蹤](https://blog.csdn.net/sinat_26917383/article/details/86557399)
2. [kalman numpy實現, YOLO辯識 + kalman + 匈牙利，追蹤](https://blog.csdn.net/xiao__run/article/details/84374959)
3. [Kalman + 匈牙利 + Gaussian Mix Modeling](https://blog.csdn.net/xiao__run/article/details/77478579)
4. [Object Tracking using OpenCV](https://www.learnopencv.com/object-tracking-using-opencv-cpp-python/)
5. [OpenCV中的目標追蹤算法介紹](https://kknews.cc/zh-tw/tech/jl2y94y.html)
6. [多目标跟踪：SORT和Deep SORT](https://zhuanlan.zhihu.com/p/59148865)

# Introduction
多目標追蹤的Intro, SORT以及Deep SORT
[Ref 1](https://zhuanlan.zhihu.com/p/59148865)
多目標追蹤的3種門派
[Ref 2](https://zhuanlan.zhihu.com/p/77111218)

# Hungarian Algorithm + kalman filter framework
Reference by 
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
Reference by
1. [wiki](https://zh.wikipedia.org/wiki/%E5%8C%88%E7%89%99%E5%88%A9%E7%AE%97%E6%B3%95)
2. [趣写算法系列之--匈牙利算法](https://blog.csdn.net/dark_scope/article/details/8880547)
3. [带你入门多目标跟踪（三）匈牙利算法&KM算法](https://zhuanlan.zhihu.com/p/62981901)
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

## 數學工具
### 二分圖
匈牙利算法與KM算法都是為了**求解二分圖最大分配問題**
二分圖是啥，能夠分成兩組，$U$和$V$，其中$U$的點不能相互聯通，只能去連$V$的點，同理，$V$的點不能互相連通，只能連$U$的點，這樣的規則下，就稱為二分圖，我們可以發現，目標追蹤在上一個frame，時間$t-1$以及當前的frame時間$t$，各自為二分圖的一邊，目標追蹤即可視為一個二分圖問題，而目標跟蹤就演變成一個**二分圖的最大匹配問題**

<img src='./images/MOT_8.png'></img>

## KM算法(Kugn-Munkres Algorithm)
## 形象化描述
這次我們將set $U$以及set$V$換成$frame_{t}$以及$frame_{t+1}$所被識別出來的物件
並且給每條連結關係加入權重，這也是我們算法中其他模組給出的confidence score置信分數值[註2]
<img src='./images/MOT_9.jpg'></img>

#### 第一步 - 初始化
對每個頂點賦值 - 稱之為**頂標**
左邊的圖$U$根據所連線的權重，取最大值給到頂標
e.g : 
* 1號老奶奶有兩條連結，分數為0.8, 0.6 - 頂標取值為0.8
* 2號大叔有兩條連結, 分數為0.3, 0.9 - 頂標取值為0.9
* 依此類推
右邊的圖$V$，頂標值全部給0

<img src='./images/MOT_10.jpg'></img>


#### 第二步 - 開始匹配

> 匹配原則 : 紙盒權重與左邊頂點分數相同的邊進行匹配，如果找不到匹配邊，對此條路徑所有左邊頂點分數$-d$，所有右邊頂點分數$+d$，參數$d$我們在此處取值為$0.1$

對於左1, 與頂標值相同的邊標為藍色

<img src='./images/MOT_11.jpg'></img>

接下來是左2, 與頂標相同的邊標為藍色

<img src='./images/MOT_12.jpg'></img>

接下來是左3, 但是要配上連線時，發現右1已經和左1搭上藍色邊，這時候和原始匈牙利算法的不同 : 

匈牙利 : 把左1和右1的邊拆了，開始幫左1找secend option
KM : 暫且不拆邊，遇到衝突，所有遇到衝突的左邊頂標都$-d$，右邊頂標都$+d$
     note : 這樣的情況發生時，左邊衝突的頂標應該會有多個，右邊衝突的只會有1個，因為衝突是多個要搶一個造成的

<img src='./images/MOT_13.jpg'></img>

接著發現左3多了一條可匹配的邊，因為此時左3對右2的匹配要求只需要權重大於等於$0.8+0$即可，所以左3配右2

<img src='./images/MOT_14.jpg'></img>

接著進行左4的匹配，由於左4的唯一匹配對象右3已經被左2匹配，衝突發生
進行一輪$-d, +d$操作，在匹配，左4還是失敗，兩輪之後左4頂標降為0，放棄匹配左4

至此完成二分圖最大匹配

### 小結
KM算法流程結束，三對目標成功匹配，甚至左3目標在預測不夠精確的情況下(預測分數右1最高)，也能夠得到正確的匹配(因為左1配得更好!)
可見引入權重之後，匹配成功率大大提高
並且讀完了匈牙利以及KM兩算法之後，我們可以了解
**匈牙利算法得到的最大匹配並不唯一**，預設匹配邊，匹配順序不同，都會造成多種最大匹配情況，所以引入KM算法的想法是，我們用匈牙利算法找到最大匹配，接著比較每個最大匹配的權重，再選出最大權重的配邊方式，當然這種方法時間複雜度較高，隨著目標數越來越多(maybe > 100)，消耗的時間會大大增加，這是一個concern的點。

# Code
[star : 1.3k](https://github.com/abewley/sort)

# 註釋
1. 我們的Tracking Module是協助classification的，換句說我們沒有一個考靠的置信分數(confidence score)，我們需要用另外的值來取代這個link weight，例如predcition與actual frame的distance - 或許需要經過一層normolize，在SORT的論文中，score使用IOU(Intersection over union)