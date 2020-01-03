# Selective Search
* a better way to help localization than sliding window approach 
* one of the most popular "Regional Proposal algorithm"
* [Ref 1](https://www.learnopencv.com/selective-search-for-object-detection-cpp-python/?fbclid=IwAR06cddw09dOkBNGWdFLhsytqnjDtFNISjmGfrZGtGR08OjEwXG7jK4lqb4)
* [Ref 2](https://github.com/AlpacaDB/selectivesearch)
* [TextBook 2004 International joural of computer vision 引用 6312次](http://cs.brown.edu/people/pfelzens/papers/seg-ijcv.pdf)
* [Ref 3 理解Selective Search](https://zhuanlan.zhihu.com/p/39927488)
* [Ref 4 目標檢測 (1) - Selective Search](https://zhuanlan.zhihu.com/p/27467369)

* 實作 : numpy, skimage, opencv

## 概念
sliding window很慢，考慮一個更聰明的搜尋方法，給一個base image，於是乎我們可以考慮顏色相似性，質地相似性，等等等等相似性，來選出與想要被辨識出來的image更有機會相似的候選image，可以表示成一個bounding box$(x, y, w, h)$
sub-regions 被稱為 patches
<img src='./images/selective_search_1.png'></img>

### Sliding window gif

### Region Proposal Algorithms
* 按照顏色相似性，質地相似性，等各種相似性來篩選，可以大幅減少搜尋次數
* 在亂選patches時，也容易有一些noise，例如框框大小都會不太一樣，也不知道框框要鎖多緊。
* 是否為正確的bounding box可以透過classification model來輸出confidence，這個clf可以是一個確定辨識A物體的SVM，或是一個Pattern Mathcher，例如單層CNN embeedding feature，或是PCA feature。
* 如果需要用訓練的方式來把bouding box**鎖緊**(tighten)，那麼就必須標記資料，做supervised learning，考量效能以及模型最簡原則的情況下，linear regression might be a great start。
* 不像是sliding window，從pixel level進行搜尋，region regional proposal algorithm通常把pixel groupby起來，例如類似顏色，類似質地，所以會比sliding window少更多次搜尋，不過在這樣的情況下，regional proposal algorithm通常會嘗試不同的長寬比
* regional proposal algorithm一個tricky的地方是，通常有很高的recall，因為通常很多框框都會包含到物體，而沒有被包含到的框框會被classifier拒絕。
<img src='./images/selective_search_2.png'></img>
* 幾種regional proposal algorithm方法已經被探討，以下舉出5種

1. Objectness
2. Constrained Parametric Min-Cuts for Automatic Object Segmentation
3. Category Independent Object Proposals
4. Randomized Prim
5. Selective Search
以上來說Selective Search非常常被使用，因為快，而且有高的recall

### Selective Search
* Selective Search的設計使用以下的圖片資訊
  * 顏色
  * 質地
  * 大小
  * 形狀

1. Start from over-segmenting the image based on intensity of the pixel
2. 在各個segmented parts加入bounding box
3. 如果相似性佳，就groupby成一個大的sement parts
4. 回到第2步

這種一步一步組合起segmentation的方式就是Selective Search的核心，也被稱為階層式的segmentation，下左圖可以看成初始條件，然後往上走，經過了一輪，再往上走，又經過了一輪，是一種bottom-up approach

#### Similarity
* break down成4塊，顏色，質地，大小，形狀

##### Color
1個pixel有三個顏色通道，每個通道的值以RGB色彩空間舉例，有0-255，切分成25個bins，如此一來一個pixel可以用25*3=75維的向量來表示目前的顏色
$$
C_i = \{c_{i}^{1},c_{i}^{2}, ..., c_{i}^{n}\}
$$
其中$i$為第$i$個pixel，$C_{i}$為第$i$個pixel的Color vector，上標$k=\{1, 2, ...n\}$表示第1~75個color dimension。
經過L1-norm標準化之後，使用下式計算區域間的色彩相似度
$$
s_{colour}(r_i, r_j) = \sum_{k=1}^{n}min(c_{i}^{k}, c_{i}^{k})
$$
E.g.pixel $i$的顏色為純紅(255, 0, 0), pixel $j$的顏色為暗紅(15, 0, 0)，after bins -> (25, 0, 0), (2, 0, 0) -> normolize -> (1, 0, 0), (2/25, 0, 0), 相似度 (2/25, 0, 0)
具有各顏色通道的獨立性

##### Texture

##### Size

##### Shape

##### All mash-up

##### Result