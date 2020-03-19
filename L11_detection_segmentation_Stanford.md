# detection and segmentation

<img src='./images/seg_1.png'></img>

<img src='./images/seg_2.png'></img>

<img src='./images/seg_3.png'></img>

# Semantic Segmentation
input : $N \times M \times 3$
output : $N \times M \times c$ 

* 對於semantic segmentation這樣的任務一個有趣的地方是，他並不是要區分實體
* 所以在下圖中，右邊兩張圖都是牛(cow)，但我們不care這兩隻牛有沒有分開，這樣能夠比較好的處理整個任務(當然，把牛分開應該就是所謂的instance segmentation)
<img src='./images/seg_4.png'></img>

* 所以你可以想像，做semantic segmentation一種可能的做法是Sliding window，當作分類問題，這樣可以work，但是基本上有一堆缺點。

<img src='./images/seg_5.png'></img>
  * 計算量超級超級大
  * 各個小塊與小塊之間會重疊計算很多次
  * 所以這是一個糟糕的idea但是開始思考semantic segmenation時會想到這一步

<img src='./images/seg_6.png'></img>
* 第2個想法則是Full Convoliutional Network(FCN)
  * 然後用個zero padding，直接學爆他
  * 最後一層Convolution layer就直接output $w \times h \times c$
  * 然後我們可以想像loss function就是pixel level cross entropy然後average(sum) over all pixels，per data or per mini-batch。
  * 接著就back propagation
  * QA1 : training data怎麼拿? 
    * 基本上非常貴，所以我們會在網路上畫畫圖什麼的，然後把區域圈出來說，這是貓，這樣子
  * QA2 : loss function可以在講細一點嗎?
    * 就是上面我理解的這樣，沒啥新的
  * QA3 : 這樣的做法是否藏著一個假設 : 我們知道model推論時的圖片會看到什麼，就好像我們知道所有的訓練類別一樣
    * 是的，所以如果沒看過的class，就會fail掉
  * 在實務上，CNN的架構會稍作調整，不會全部的size都是跟input image相同，通常會做一些down sampling以及up sampling

<img src='./images/seg_7.png'></img>

### Upsampling?
你可能會好奇說，upsampling這種東西!?!?!?!?
1. 在網路裡面到底長怎樣?
2. 參數增加時是不是有什麼可用的策略或是思考的著力點?
好的現在我們來講Upsampling的策略
其中一招叫做**Unpooling**

#### Unpooling
* 有pooling，那當然就要有unpooling囉
* 這裡我們舉例max pooling or average pooling

下兩張圖對應到 input 2x2 output 4x4的 upsampling
1. 下左圖對應到的是使用average pooling，我們先把output展開，然後怎麼做呢，就取展開點的那個值，就是一個**anti average pooling**，稱作Nearest Neighbor
2. 下右圖則是對應到max pooling，因為已經取了max，所以基本上也回不去了，其他的就補0(這稱作Bed of Nails)，這樣取名是因為你會有一大堆0，然後這些max pooling的值會是一些peak，整張圖就會變成很平坦但是每過幾格就會有peak這樣

<img src='./images/seg_8.png'></img>

所以說基本上你會在網路架構中看到Encoder的部分有一個Max pooling，那麼Decoder那邊就會有一個Unpooling(Bad of Nails)，而且還要記得對應做max pooling的位置，因為Unpooling的時候要用到(the corresponding max pooling step earlier in the network)，在下圖中用特別的顏色做標示

<img src='./images/seg_9.png'></img>

* QA : 為甚麼這樣會是有用的? - 因為pooling丟失了圖片的空間訊息，但是我們的預測希望在pixel level，因此我們希望把空間訊息補回來，所以才使用unpooling
* QA : 這樣的設計對backpropergagtion有什麼影響嗎 - 基本沒對參數傳遞沒有造成什麼影響


#### Transpose Convolution
* 另一種你會看到拿來做Upsampling的方法 - Transpose Convolution
* 剛剛講到的unpooling，都只是固定形式的函數，他們並沒有辦法被更改(或稱為被學習)，那麼convolution應該要對應到什麼? inverse convolution?
* 有的，有這樣的東西，而且說穿了其實只是另一種convoltuion

* Recall 最簡單的3x3 convoltuion stride 1 pad 1
<img src='./images/seg_10.png'></img>

* 以下則是3x3 convoltuion **stride 2** pad 1
<img src='./images/seg_11.png'></img>
* 我們可以看到當stride = 2時，基本上就是對原本的圖做down sampling，factor為2

* 所以說我們想要剛剛上面提到的反操作，怎麼做呢?
* 這次我們不做內積，對於input的pixel，將其當作weight，經過一個filter，基於一個scaler x vector 的乘法丟到output裡面，然後把重疊的部分加起來

<img src='./images/seg_12.png'></img>

所以2D的版本就長成這樣

<img src='./images/seg_13.png'></img>
同樣地, stride就會變成input和output之間的放大倍率，而他有多種名稱，`Deconvolution`, `Upconvolution`, `Fractionally strided convolution`, `Backward strided convolution`，但其實你可以看到，他就只是一種convolution

##### Convolution as Matrix Multiplication(1D)
<img src='./images/seg_14.png'></img>

<img src='./images/seg_15.png'></img>

* QAs : 重疊的部分為什麼是sum而不是average? - 這是一個好問題，其實sum只是為了符合tranpose convolution，但是這樣確實有一個問題就是重疊的部分會有比較大的scale，所以在upsampling的部分也有學者去探討這個問題

<img src='./images/seg_16.png'></img>

以上就是semantic segmentation的基本概念，接下來我想談談Classification + Localization的方法

<img src='./images/seg_17.png'></img>


# Classification + Localization
* 基於一個基本的假設，圖片中有一個或是多個你想尋找的物體
* 同樣的，我們會有一個巨大的網路(這裡假設一個全監督的情況)，例如這邊是AlexNet，但這次我們希望輸出的是Class Scores以及Box Corrdinates，如此一來我們產生了兩項loss, 一項是classification loss(這裡使用Softmax-loss)，另一項則是localization loss(這裡使用L2 loss)，會有其他人用L1, smooth L1，或是其他的，但是基本上就是在處理regression loss
* QAs:
  * Q : 一次做兩件事沒有問題嗎? 例如分錯的時候?
  * A : 大部分的時候運作起來沒什麼問題，但是分錯累的時候就會有問題了，所以有些人對此做了改進
  * Q : 這兩種loss的單位不同，是不是貢獻到total loss的時候需要經過一些normolizarion?
  * A : 在這樣的場景下，我們會將此稱為multi-task loss，這樣的場景下，我們會設置一組參數來控制兩組loss，在貢獻到total loss當中，然後把最後的loss取gradient，這挺tricky的，因為這組weight是一個你必須給定的參數，但這個參數和以前你看到的超參數不太一樣，這組參數的變更會更改整個loss function，所以要設置這一組參數其實有一些困難的地方，在實務場景上，case by case，通常會用最後的performance metric來選這個值要是多少
  * Q : 為什麼不分開作要一起做?
  * A : 也可以分開做，但是一起做可以更充分的利用資訊

<img src='./images/seg_18.png'></img>

## Human Pose Estimation

<img src='./images/seg_19.png'></img>

* 也有另一種形式的定位，就是Pose Estimation

作法基本上就是一樣經過一個大的網路，最後出了一個feature vector，然後分成14x2的matrix，接著用regression loss來進行處理，這裡有趣的是，應該會針對點座標做L2 loss，在全部相加起來

<img src='./images/seg_20.png'></img>

* localization有一個令人困擾的地方是，你不總是知道圖片中有幾個你想辨識的物體

# Object Detection

<img src='./images/seg_21.png'></img>

* 這是一個很有料的主題，幾乎是電腦視覺的核心
* 同樣地我們先從一個固定種類的方法開始講起


[TBD 42:00](https://www.youtube.com/watch?v=nDPWywWRIRo&list=PLf7L7Kg8_FNxHATtLwDceyh72QQL9pvpQ&index=12&t=0s)

# Other Resource
* [semantic segmentation](https://kknews.cc/zh-tw/tech/mgqvl9.html)
  * 傳統使用Clustering，像是Mean shift，15年之後隨著FCN的發展，將DL帶入semantic segmentation
* [SEMANTIC IMAGE SEGMENTATION WITH DEEP CONVOLUTIONAL NETS AND FULLY CONNECTED CRFS - 菜逼八看論文
](https://ithelp.ithome.com.tw/articles/10223557)
  * FCN, 2014年, citation : 2215 - 從圖片萃取feature vector相對容易，從feature vector重建image則相對難，CNN界的AutoEncoder!