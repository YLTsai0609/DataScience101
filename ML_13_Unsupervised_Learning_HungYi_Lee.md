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
<img src='./images/un_7.png'></img>

<img src='./images/un_8.png'></img>

<img src='./images/un_9.png'></img>

[TBD 23:22](https://www.youtube.com/watch?v=iwh5o_M4BNU&list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49&index=22)