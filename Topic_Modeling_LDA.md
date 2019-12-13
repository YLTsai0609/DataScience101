# Topic Modeling
* 方法其實很多，透過matrix factorlization(PCA, SVD, NMF) / embedding(NN) / LDA 方法都可以得到
* 還缺一個評估的方式
* LDA主要透過設計兩個**話題機率分佈**來進行解釋
* 而且LDA與人類寫作的邏輯相近，換句話說在表達的時候有比較好的解釋性

# Understanding First
<img src = '/images/LDA_1.png'></img>
* 假設 
  * : 文章(文件)內中的詞彙，是來自某個Topic，所以左邊我們可以看到，黃色Topic中，有著各式各樣的詞彙，有著各自出現的機率
  * 每個文章(文件)都是由若干個主題，所組成的
  * 總共有兩層關係 
    * 原本 : 文件 -> 詞彙
    * 模型假設的生成機制 文件 ->(文件-主題分佈)-> 若干個主題 -> (主題-詞彙分佈) -> 詞彙
  * 思考點 : 舉兩個詞彙並非從話題產生的例子來反駁吧 =)

# Math Second
<img src = '/images/LDA_2.png'></img>
* 文件字數使用Possion分佈
  * Possion分佈常常用來描述發生次數:
    * 每個小時的來客數
    * 每天特定16:00-20:00進店客數
    * 在公車站等1小時，總共會停靠的公車數
    * 寫一篇文章，總共會寫多少字
* 對於每一個用字$w_{i,j}$，文件-主題分佈，主題-詞彙分佈採用Multinomial分佈
  * multinominal分佈被拿來描述多個cateogry時，各個category的出現機率，在主題很多，詞彙很多的假設下，每次選字可是為不變動的分佈。

# Prior distribution
* 上述是模型假設，並非先驗分配的假設
<img src = '/images/LDA_3.png'></img>
* 先驗分配這裡取 Dirichlet distribution，這裡事實上可以針對我們對文字資料的了解選用符合的先驗分佈，例如exponential distribution。
* [TODO 為什麼先驗使用Dirichlet?]
  * 猜測 : 這個分佈在數學上能夠變成任何其他常見的分佈，可塑型強
* 然後就跑Bayesian, 這裡是採用Gibbs sampling的方式，而非MCMC的sampling方式，scikit-learn的Model中也有多個變種，論文是2011, 2013年

# Result
* 就是兩個分佈的參數分佈，進入DataViz
* LDA的DataViz要說的事情稍微複雜
# DataViz
* Bar-plot 各Topic中有的LDA score
* bubble plot, LDA-viz
  * bubble plot 右邊扔然有bar-plot, 左邊則是Reduction的axis, 透過壓縮算法來計算各主兼之間的距離

# Evaluation