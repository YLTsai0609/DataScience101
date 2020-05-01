# Resource
* [[CS224W Machine Learning with Graphs] Properties of Networks and Random Graph Models
](https://www.youtube.com/watch?v=dD6LRgw_2mQ&list=PL1OaWjIc3zJ4xhom40qFY5jkZfyO5EDOZ&index=1)

# How can I describe a Graph?

<img src='./images/gn_1.png'></img>

# Degree Distribution
* Find the hub, and the outskirts!
* [degree - 一個頂點在圖中與相鄰鼎點連接的數目](https://zh.wikipedia.org/wiki/%E5%BA%A6_(%E5%9B%BE%E8%AE%BA))
* degree distribution - 度分佈，where is the hub, where is the outskirs, and something like that

<img src='./images/gn_2.png'></img>

* the plot - x axis degree $k$, y axis how many nodes / or normalized by total number of nodes
* only few hub, most have one or two degree - like exponential
* **two degree distribution if dierect graph**
  * in degree distribution
  * out degree distribution
* **indirected graph**
  * degree distribution

# Paths in a Graph
* A sequence of modes in which each node is linked to the next one!(no need must be shortest)

<img src='./images/gn_3.png'></img>

## Distance in a Graph
* Distance (shortest path, geodesic(測地線))
  * $h_{AX} = \infin$, $h_{BD}=2$
* 有向圖則需要跟著箭頭方向 - consequence distance
  * 不具有對稱性! $h_{BC} \neq h_{CB}$ 
  * 有時候我們僅僅只是把方向丟掉，因為我們不需要處理那麼複雜的有向網路
<img src='./images/gn_4.png'></img>

## Network Diameter
* Diameter = The max shortest path, which distance between any pair of nodes in a graph - the upper bound(it's ok but might too less information)
* Averafge path length - 
$$
\bar{h} = \frac{1}{2E_{max}}\sum_{i,~j \neq i}{h_{ij}}
$$

* $h_{ij}$ - is the distance from node $i$ to node $j$
* $E_{max}$ is the max number of edges(total number of node pairs) = $n(n-1)/2$
* 可忽略未被連結的點(如果這些點不是很多)
* 該測量和node connection有相依性
<img src='./images/gn_5.png'></img>

# Clustering Coefficient
* only defined in undirected graph

[TBD 0843](https://www.youtube.com/watch?v=dD6LRgw_2mQ&list=PL1OaWjIc3zJ4xhom40qFY5jkZfyO5EDOZ&index=1)