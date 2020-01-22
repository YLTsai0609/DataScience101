## Face Clustering
* 背景 : 將相似臉型或是臉的骨架相似的新娘臉分成200個類別，用於醫美的臉部微整型推薦
* [資料科學與機器學習](http://yltang.net/tutorial/dsml/14/?fbclid=IwAR0eYAzbzlEfEDejRPv1rajo2cO8auHowWBGA1NrX0eF9kvB4H0WThoLk-w)
* [Chinese Whisper 人脸聚类算法实现](https://blog.csdn.net/u011808673/article/details/78644485?fbclid=IwAR1jtyEYGJr1HJYxcKbSU_PuIoplwxv67ZvmTpRNdt2R_tquEO27phvIkoI)
* [Unsupervised learning: PCA and clustering](https://mlcourse.ai/articles/topic7-unsupervised/?fbclid=IwAR1E7X4GjuPBvszOtwFxOxH9kbwnlRtUJ5cQ--po2UoE6IIoJrLMPQNdcmM)
* [Consensus-Driven Propagation 解說](https://zhuanlan.zhihu.com/p/51806059?fbclid=IwAR1izyhJ6bNqQ-v_sqhz2jKksRaZtrCUexc3iqheyYygbi6aNaLGCBfiz4M)
* [Consensus-Driven Propagation GitHub 300+ stars](https://github.com/XiaohangZhan/cdp?fbclid=IwAR1Dxa2chZjI0TfdancRsfoHOtUpKPm1RSVJ1Q-Xd4_AhQ9qt8BY_oPcAoM)
* [k-means++: The Advantages of Careful Seeding](http://ilpubs.stanford.edu:8090/778/1/2006-13.pdf?fbclid=IwAR3YXfVdete836Aa5drv41rbFEOvjKggWT4GiBhHkw3UJ2aiYTCY7X6h75o)
  * cited : 4766
  * 2007
* [Deterministic Initialization of the K-Means Algorithm Using
Hierarchical Clustering](https://arxiv.org/pdf/1304.7465.pdf?fbclid=IwAR1rZyRX8qKlG8fy6gqIlJv4v66fE4h5ecSAgAySIobwn1MhEyqq1nP3_ig)
  * cited : 51
  * 2012
* [Finding your Lookalike : Measuring Face Similarity Rather than Face Identity](https://arxiv.org/pdf/1806.05252.pdf)
  * cited : 3
  * 2018
## Survey region
* [Deterministic clustering approaches on Cross Validated](https://stats.stackexchange.com/questions/205833/deterministic-clustering-approaches?fbclid=IwAR21mlUSk58zuAd4n2wM5TtLUFvbYByzw7r7TS7x78E48euHykqbw6MuFJQ)
* [TSNE cons](https://www.jianshu.com/p/a67fb39a213a?fbclid=IwAR3TRvKwVzjPQw2TIhmAAyM7MNGjXDmiEhPP6JmTL29r2ZU3e11rbO7_TzU)
* 
## 架構
正臉 - 沒有眼鏡 10000張不同人的新娘照 -> facenet embedding (10000x512) -> distance matrix (10000 x 10000) -> 分成200群
## Outlier
* 對於outlier，本case要分進去確定的類還是output為oulier另行處理?
## Unsupervised learning
各個分群算法的優缺點，侷限點為何
### KMeans
  * 組內差距小，組間差距大
  <img src='/images/face_cluster_1.png'></img>
  * 優點
    * 資源多，方便Survey
  * 缺點
    * 不具方向性，對於分散，歪斜，凹型 - 群聚效果不佳
    <img src='/images/face_cluster_2.png'></img>
    可以看到群組中心分別在凹型的尖端，不適合用於凹型群組
    * 對Outlier以及distance數值敏感，建議先normolize過後在處理
  * 是否具備重現性?
    * scikit-learn : 否，初始點選擇的kmean++並不是保證可重現性的方式
    * 
  * 時間複雜度
    * $O(NKT)$
    * $N$為資料數, $K$為中心數(群數), $T$為迭代次數
  * 空間複雜度
### DBSCAN
* Density-based spatial clustering(密度空間分群)
  * 概念
    * `有min_samples`(最少樣本數)與`eps`(距離)兩個參數
    * 以某資料點為中心，在其周圍的`eps`若有`min_samples`以上個資料點，則稱為密集區(Dense region)
    * 在密集區的資料點稱為核心樣本/核心點(Core samples, core points)
    * 不在密集區的資料被歸類為雜訊(Noise)，亦即不屬於任何群組
    * 尚需survey
    * 最終結果會產生三種標籤 : 核心樣本、核心樣本的鄰居(稱為邊界點Boundary points)、以及雜訊，重複執行DBSCAN可能會造成邊界點屬於不同核心樣本的鄰居，但是核心樣本即雜訊資料點都會一樣
  * 優點
    * 不需設定分群數，可應付複雜群組形狀，可以分辨不屬於任何群組的資料點(outliers)
  * 缺點
    * 不適合處理小規模資料 - 可能遇到沒有密集區的產生 - 全部都是雜訊
  * 是否具備重現性?
    * 以相同順序給出data時具備重現性
  * 時間複雜度
    * $O(N)^{2}$
  * 空間複雜度


### Chinese Whisper

### lookalike network
* 仍然使用network來做
* 有人工標記的ground-truth, 但每個人看得都不一樣
* 仍然不具有解釋性
* 採用Supervised, ranking problem的框架來思考
## 評估方式
* 除了商業邏輯200類之外 - 如何評量分群品質?
* Adjusted Rand Index(ARI)
  * 需要ground truth
* Adjusted Mutial Information(AMI)
  * 需要ground truth
* Homogeneity, completeness, V-measure
  * 需要ground truth
* Fowlkes-Mallows score
  * 需要ground truth
* Silhouette
  * 不需要ground truth
  * [輪廓係數](https://baike.baidu.com/item/%E8%BD%AE%E5%BB%93%E7%B3%BB%E6%95%B0?sefr=enterbtn&fbclid=IwAR1lvH9lK9mPaw8EqewrUf_X1ITGzMETN5mFiFjYxXaCzJ_pT_DtGsmCRO8)
  * 考慮了內聚度與分離度兩種因素，且圖形可以按照各個cluster展示histogram，考慮使用
  * 限制 : 該metric的假設是clustering為凸集合，月形聚類就會失準
* Calinski-Harabax Imdex
  * 不需要ground truth(方差比準則)
* Davies-Bouldin Index
  * 不需要ground truth(方差比準則)
* 

## IDEA ABOUT FEATURE ENGINEERIMG
* 為了讓分群更能區分各種臉型，眼型，鼻型，嘴形等
* 區域特徵 - 例如尖臉型
<img src='/images/face_cluster_3.png'></img>

## 資料噪聲
* 影響臉型分群因素列表
  * 平面旋轉角(下巴不是朝下)
  * 立體旋轉角 - 1 (左側臉，右側臉)
  * 立體旋轉角 - 2 (頭頂，下巴) - 較少出現的影響
  * 臉部表情