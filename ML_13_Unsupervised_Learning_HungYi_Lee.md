# ML Lecture 13: Unsupervised Learning - Linear Methods
* 李宏毅
* 目的 : 快速掃過一遍相關算法，原理，關鍵字，評估方式，不求完整理解，但求知道這些名詞
* [Video](https://www.youtube.com/watch?v=iwh5o_M4BNU&list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49&index=22)

## Unsupervised Learning
* 三種用途，大約分成兩種概念
* 化繁為簡(Clustering & Dimension Reduction(Feature Extraction))
* 無中生有(Generation)

這裡focus在Feature Extraction上，而且是Linear的方法

<img src='./images/un_1.png'></img>

## Clustering
### KMeans 

<img src='./images/un_2.png'></img>

## Hierarchical Agglomerative Clustering(HAC)

* 先排列data，計算similarity(最像的，或是所謂距離最小的)
* 兩個最像的merge起來，做出一個虛擬的代表(例如把vector做平均)
* 做一顆樹出來
* 接著選個threshold，就可以決定你想分幾群
* [Demo case on Iris dataset](/demo/demo_plot_agglomerative_dendrogram.py)

<img src='./images/un_3.png'></img>
* 優 : 和distance matrix一樣，可以清楚地觀察inner cluster的相似以及outer cluster的相似，在多維情況也適用
* 比KMneas優的地方，可以看著樹狀結構來決定要幾個群數，因為KMenas的決定方式比較數學，有時候不一定符合實際情況，解釋性也比較差

## Soft Cluster(Distirbuted Representation)
* 上述兩個招式(KMenas, HAC)都是硬分類，有時候容易遇到以偏概全的感覺，軟性分類可以mix屬於各種cluster的比例
* 舉例，如果只說小傑是強化系，會丟失很多資訊，應該要像一個表格搬來表示小傑，用一個分佈(或是你說是一個vector)
<img src='./images/un_4.png'></img>
* 所以如果用圖片(high dimension) -> 變成一個6,7維度的vector，那就是所謂feature extraction
* feature extraction其實和soft clustering是同一件事情，只是有不同的稱呼而已

## Dimnesion Reduction
* 3D空間中的地毯其實2D就能夠表示得很好，那幹嘛不用2D呢?
<img src='./images/un_5.png'></img>
* 更具體來說，來看看MNIST
* 如果我們假設有1排3，
  * 原本 : 28*28，但是其實根本沒必要
  * 只要用1個維度，因為其實表示角度就可以了

<img src='./images/un_6.png'></img>


* 一些方法
  * Feature selection
  * PCA

## PCA 觀點1
* max variance 
<img src='./images/un_7.png'></img>

<img src='./images/un_8.png'></img>

<img src='./images/un_9.png'></img>
* 解法一 Lagrange Multiplier
* 解法二 Gradient Descent using linear network


## PCA的性質
* eigen-vectors是一組orthonormal set
* 會把原本的feature set 去相關性(去耦合) decorrelation
  * 不同eigen vector相乘為0，同時covariance也為0，這樣做有什麼好處，有些model是假設Gaussian distribution而且不**互相影響**，特徵數量可以減少，避免overfitting

<img src='./images/un_10.png'></img>

## PCA另一種直觀的解釋
Key : min Reconstruction error
* 從手寫數字來看，Basic Component可能是人的一些筆畫
* 例如下式，$x=7 = c_1u^1 + c_2u^2 + c_3u^3$

<img src='./images/un_11.png'></img>

<img src='./images/un_12.png'></img>

解min Reconstruction error是一個SVD問題

<img src='./images/un_13.png'></img>

## PCA的弱點
* Unsupervised，很難真正了解該群，這時候引入Label data會比較好，即LDA，LDA是一種Supervised Feature Extraction方法(LDA : linear discriminant analysis)
* Linear
* 想要把流線型曲線拉直，其實是強人所難的，是一個NonLinear tranformation，PCA是做不到的，只能產生下面這種藍色跟紅色疊再一起的情況

## PCA 和 SVD之間的關係
[【机器学习】降维——PCA（非常详细）贊同800+](https://zhuanlan.zhihu.com/p/77151308?fbclid=IwAR3FvbzHWpRUTIit-Gi1F5pKMo-on2s7PDBt7uUip3nZo-sdyvLSdpyCHOY)

<img src='./images/un_14.png'></img>

## PCA - Pokemon
* 800 Pokemons, 6 features(HP, Atk, Def, Sp Atk, Sp Def, Speed) 
* 要有幾個PC就像要有幾個hidden layer，要有幾個neuron一樣，是要自己決定的，data viz時或許需要直接放到2維或是3維，可以透過eigen value ratio來表示解釋度

<img src='./images/un_15.png'></img>

## PCA on Pokemon
* input 6維度可解釋性feature
* output 使用4個PC來做projection，而且可以先針對4個PC進行解釋
  * 因為4個PC都會是原始6個feature的linear combination
  * 只要PC是能夠被原始特徵解釋的，那麼PC軸仍然能夠具有足夠解釋性

<img src='./images/un_16.png'></img>

<img src='./images/un_17.png'></img>

## PCA on MNIST

<img src='./images/un_18.png'></img>

有些PC看起來看得懂有些則不，第一個PC看起來像1，第2個看起來像9

* 基本上，上面這些PC會被稱為eigen digits

## PCA on Face
 
<img src='./images/un_19.png'></img>

* 每個PC都是完整的臉? 為什麼不是筆劃?或是子部分?
* 因為線性疊加的係數可正可負，這意味著可以先很複雜，在扣除
* 舉例來說我想要畫一個9，我可以先畫一個8，然後把下面的圈圈扣掉，然後在畫上一槓
* 如果你想要的是筆畫而不是很多瑪雅文字?那麼你就要限定你的線性疊加係數壹定要是正的，這樣的技術是Non-negtive matrix factorization(NMF)

## PCA vs NMF
* PCA其實可以視為對Covariance matrix做SVD，係數可正可負
* 但是NMF會強迫係數都是正的
* 如此一來就不能說，先畫一個複雜的東西，然後再去掉
* 並且，eigen vector的每一個component也都會強迫是正的，這樣，就會更像筆畫!

## NMF on MNIST

<img src='./images/un_20.png'></img>

* 如同我們講的，更像是筆劃了


## NMF on Face

<img src='./images/un_21.png'></img>

* 可以看到更多局部，例如第5個是人中，第6個是眉毛
* 這樣的結果更接近我們想要找的，像是人臉的各個局部

## Matrix Factorlization
* 調查每個人中有動畫公仔的數目，基本上我們點找出每個人對公仔的偏好，但又並非是喜歡涼宮春日這麼直接，而是說A可能喜歡某個類型的
* 有買涼宮春日的，很有可能也有買御凡美琪的，有姐寺的就很有可能有小維，這並不是巧合，feature之間具有相關性

<img src='./images/un_22.png'></img>

* 拿Domain Knowledge來說，動漫宅，或許可以分成兩種，喜歡傲嬌的跟喜歡天然的
* 每個宅可以用一個傲嬌跟呆萌的vector來表示屬性，同樣地，每個動漫人物也是，而inner product越大，則越有可能喜歡

<img src='./images/un_23.png'></img>

* 但是這樣的vector是沒人知道的，是latent vector

<img src='./images/un_24.png'></img>

* 我們有的資料就是一個這樣的購買matrix

<img src='./images/un_25.png'></img>

我們的假設，matrix中的每個element都來自一兩個二維向量的inner product
$$
r^A r_1 = 5
$$

$$
r^B r_2 = 4
$$

數學式

$$
X_{M, N} = R_{M, K} T_{K, N} 
$$
然後 min reconstruction error 其實就是SVD
你說SVD不是有三個Matrix嗎? 其實你就看你要把中間的$\Sigma$併到左邊還是右邊就可以了

<img src='./images/un_26.png'></img>

## Missing information
* 當然你也可以把missing填0硬幹一波，不過這就假設他們都不買那些missing的

<img src='./images/un_27.png'></img>

* 但其實可以用另一種做法，依樣假設latent vector，然後只對那些有值的寫一個loss function，接著用Gradient descent做

<img src='./images/un_28.png'></img>

* 你無法知道1, 2維度具體來說代表什麼意思，但是可以表達為什麼$A$買了$1,2$比較多

<img src='./images/un_29.png'></img>

* 同樣的你可以透過把$r^A$跟$r^3$內積來得到可能的購買數量

Netflix的比賽在最初的版本就會用這樣的技術來做一個推薦系統

## More about Matrix Factorization
* 考慮角色或是買家本身自己有偏好(bias)
  * 例如$b_{A}$代表該買家本身喜歡買公仔的程度
  * 例如$b_{1}$代表該角色本身在市場上的受歡迎度
* 我們就可以改一下Loss function
* 同樣地就是GD硬解一波即可，你也可以加上regularization，例如你覺得買家要馬都是萌系要馬都是傲嬌系那就加上L1 regularizer

<img src='./images/un_30.png'></img>

## Suvvy for Non-Negtive Matrix Factorization

(Algorithms for Non-negative Matrix Factorization 非負矩陣分解)[https://www.itread01.com/content/1542798604.html]
* 非負矩陣分解可以從L2 distance也可以從KL divergence，兩者都是做最小化，其中使用KL散度會無法做新資料的transform，因為KL divergence並不是一個對稱度量，不能被稱為距離
* 優化方法可以選擇GD(加法更新規則)，或是乘法更新規則

非負矩陣分解NMF(https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/560096/)
* 用武之地 : 影像處理，文字探勘 非常常用，因為維度高，非結構化，而且負值不具解釋性等三項原因
* 影像 
  * 衛星發回的影像儲存
  * 自動識別太空垃圾
  * 辨識星體
  * 自動識別進出機場的可疑恐怖份子
* 文字
  * Oeaclw : 文字特徵提取及分類
* 語音
  * 語音擷取
  * 音樂調式識別
* 機器人控制
  * 影像訊息儲存及壓縮

[非负矩阵分解(NMF)简介](https://zhuanlan.zhihu.com/p/22043930)
* 贊同 355
* 比較PCA, VQ, NMF
針對矩陣分解問題
$$
V_{M\times N} ~ W_{M\times K}H_{K\times N}
$$
* VQ要求$H$的每一列只有一個元素為1，其他為0，相當於將m個數據歸納成了k個代表，原數據映射過去就是取$k$個basis當中與原向量距離最小的來重新表示，所以以臉來說，$VQ$的basis都是一張張完整臉，它們都是最具代表性的臉
* PCA求的是一組標準正交basis，第一個basis的方向取元數據方差最大的方向，然後第2個basis再取剩下的最大方差，所以PCA是去相關性的，但也比較難有直觀的物理意義，因為原本的臉對於basis是加加減減得到的
* NMF則約束了非負，因此只能把basis相加，不能相減，意味著basis和basis通過拼接組合來還原影像，所以會看到sub component

[Projected Gradient Methods for Nonnegative Matrix
Factorization 2007](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=ACAE3131E5FA09D0798DF7D967F42000?doi=10.1.1.538.997&rep=rep1&type=pdf)
* cited : 1700次
* 說明了1990到現在解NMF的方法，Overiew article

[漫谈 Clustering (番外篇): Vector Quantization](http://blog.pluskid.org/?p=57)
* 解釋Vector Quantization，scipy中利用kmeans以及vq function可以實作

## Matirx Factorization for Topic analysis

* 把矩陣分解用在文字探勘中，就叫做LSA，完全一模一樣，只是換矩陣的標的物
* 值 TFIDF，row : 詞彙，column : 文本
* latent vector : 主題 : 財經，政治，娛樂，...
* 有各種變形，例如Probability LSA，以及LDA(latent Dirichlet allocation)

<img src='./images/un_31.png'></img>

## References
* Dimension reduction的方法多如牛毛，這邊列出一些跟PCA比較像的

<img src='./images/un_32.png'></img>

* MDS : 不需要每一個data的feature vector，只需要data之間的distance : 一般是舉例城市的距離，其實PCA會保留data point的距離，在高維空間中是接近的，在低維空間終究會是接近的
* PCA 機率版
* PCA 非線性版
* CCA 有聲音訊號，有圖片訊號
* ICA 
* LDA

## FA, PCA, SVD, ICA,LPP, LDA歸納介紹
[Ref](https://blog.csdn.net/qiusuoxiaozi/article/details/50810521?fbclid=IwAR3V_sACRKfa9mCHfaBYGnxKElJgRXc6xO2FQU1HsI6_8mW_J29o-dUY14U)
* FA : 高維樣本點實際上油滴為樣本點經過**高斯分佈，線性變換，誤差擾動生成**，從高維樣本中分解出低微向量
* PCA : 根據Andrew的教學，PCA有9, 10種詮釋方式，而且Andrew的課程中，application會很有啟發，PCA有超多種用途
  * Visualization
  * Copmression
  * Learning : 特徵維度太大時Overfitting
  * Anomaly detection : 從reconstruction error來看每個樣本點
  * Matching/distance calculations
    * 例如人臉識別，在PCA空間來計算L2 distance
    * 兩個documents的相似性，如果使用cosine distance，study將會和learn正交，相似度為0，而PCA則避免了這個缺點，用PCA的距離來行量，learn和study仍然保留正的相關性
* FA和PCA 基本上是認為數據存在在子空間中，GMM和KMeans則是認為數據集合在數據塊中，使用哪種方法取決於妳認為數據屬於情況1還是情況2
* SVD : 從Andrew的課來看，SVD相當於PCA的實作方法
  * 現在計算機計算SVD的招數很成熟，Andrew本人說SVD的普遍程度就像計算平方
  * 用SVD來實作的話，避免了高維度的共變數矩陣計算，scikit-learn中也是利用SVD來實作PCA
* ICA 獨立成分分析 - ICA被稱為盲源分離(Blind Source Separation, BSS)，源指的是信號，即獨立成分，例如雞尾酒會中的說話者，而盲指的是我們對混合矩陣所知甚少，僅僅對信號做非常弱的假設，推荐电子工业出版社的一本中译本教材《独立成分分析》
* 局部保留投影（LPP）
最早是何晓飞（芝加哥大学，现在在浙大CAD）发表在NIPS上的文章提出来的，原文摘要称”LPP should be seen as an alternative to Principal Component Analysis (PCA)”.

* 线性判别式分析( LDA)
LDA也叫做Fisher线性判别(Fisher Linear Discriminant ,FLD)，是模式识别的经典算法，它是在1996年由Belhumeur引入模式识别和人工智能领域的。线性鉴别分析的基本思想是将高维的模式样本投影到最佳鉴别矢量空间，以达到抽取分类信息和压缩特征空间维数的效果，投影后保证模式样本在新的子空间有最大的类间距离和最小的类内距离，即模式在该空间中有最佳的可分离性。

# Case Study of PCA
