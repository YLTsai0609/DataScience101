* [Lee](https://www.youtube.com/watch?v=BZh1ltr5Rkg)
* Feature Scaling 不同得feature，會需要不同的learning rate，變得較不好訓練
* [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/pdf/1502.03167.pdf)
  * 2015
  * 18008 citations

# Hidden Layer?
* $a^{1}$其實是layer2的feature，我們可以想像網路前面幾層是feature extractor，同理，每一層的input都可以是下一層的feature
* 這種做法對NN很有幫助，解決了一個稱作Ibternal Covariate Shift的問題
<img src='./images/bn_1.png'></img>

* 如果對於每一個layer，input feature都是mean是0 variance是1，那麼training就會更容易一點
* 當網路越深層，ICS越大
* 而因為layer的weight一直改變，導致我們無法很輕易地得知每一次中間輸出的參數的mean跟variance，因此解決這個問題的技術就是Batch mormalization

# Batch
<img src='./images/bn_2.png'></img>
* 一批有3筆資料for example

# Batch normalization
可以apply在activation func的input也可以apply在activation func的output，現存比較多的是apply在activation func的input
$x^{1}$ -> $z^{1}$ -> $a^{1}$
* 其實我們不喜歡input值落在activation func的平緩處，因為這樣會有梯度消失的問題，因此先做normalization就比較容易在把值控制在附近，那些地方的微分值會比較大

<img src='./images/bn_3.png'></img>
* 其實我們希望的是該batch可以代表整個training set的statitsic，所以當你batch size太小時，就別用了!
<img src='./images/bn_4.png'></img>
* 注意 `sigma`是elementwise的?

<img src='./images/bn_5.png'></img>
* 這樣怎麼train?
* 事實上$\mu$和$\sigma$也是變數，不能被視為const，BP需要通過他們，從$z$到$z'$中間也必須視為一個網路
* 當你改動了$W_1$等同於改動了$z_1$等同於改動了$\mu$, $\sigma$

## Modified
* 如果你使用的activation func gradient最大不是在0，或是mean和vatiance不是0跟1，在其他的地方會表現得更好，那麼你可以改動他，做一個線性轉換
<img src='./images/bn_6.png'></img>

## Testing stage?
* 事實上我們需要的是training set的stats，如果遇到整個training set太大，或是你的training是online的，那就很困擾
* 通常預測一直也只預測一筆data....

<img src='./images/bn_7.png'></img>

* 可以取最靠近training結束時的mean和variance來代表整個training set的參數

## Benefit?
* 讓訓練變簡單 - which means 可以設大一點的learning rate
* 更少產生梯度爆炸和梯度消失
* 原本如果使用sigmoid func，那麼很容易產生前面兩個結果，不過用了BN，如果你的activation func是sigmoid或是tanh，那麼就會特別有幫助
* 對參數的initialization影響更小

<img src='./images/bn_8.png'></img>

* BN也可以視為一種normalization，因為遇到outlier會更robust
* BN主要是在training效果不好的時候作用較大

# Concerns
* Batch normalization在testing時使用training的stats，但是如果測試時目標離training時較不同(transfer task)，表現較差
* 如果特定的training process，無法用較大的batch數，那麼也會很差(例如object detection)，Group Normalization有解決方法