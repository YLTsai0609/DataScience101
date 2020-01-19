# all_about_the_distance
* 背景 : 隨著使用到的距離函數越來越多，有必要做一個統整，更了解距離的本質
## personalized distance
[Reference](https://zh.wikipedia.org/wiki/%E8%B7%9D%E7%A6%BB)
一般度量
在數學中，集合$M$上的距離函數唯一函數$d : M \times M \rArr R$，$R$為實數集，且滿足:
* $d(x, y) \geq0$
* $d(x, y) = d(y, x)$
* $d(x, z) \leq d(x,y) + d(y,z)$
針對第三點特別說明，三角不等式 - 指出$x,z$的距離必須真的是所有路徑中的最短距離

## Text distance 
[Reference](https://towardsdatascience.com/3-text-distances-that-every-data-scientist-should-know-7fcdf850e510)