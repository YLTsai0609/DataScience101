# Pros and Cons
|Pros|Cons|
|----|----|
|1. 可解釋性(皆為正，且據統計解釋) <br> 2. 非線性但是可解釋，表示準確度應該還不錯|可能跑很慢|

# Resource
[Dive into Deeper Math](https://multithreaded.stitchfix.com/blog/2015/07/30/gam/)
[Python GAM -pyGAM, star 450+](https://github.com/dswah/pyGAM)
[Introduction Article 660+](https://codeburst.io/pygam-getting-started-with-generalized-additive-models-in-python-457df5b4705f?source=bookmarks---------0------------------)

# Hints
* 基本上是GLM + feature interaction, constraint係數皆為正，形成Additive，Additive model在解釋時都有很大的方便(像是Non-Negtive Matrix Factorization)
* 有各種統計量，是一個面對統計背景好解釋的模型
* 有Patial Dependence Plot with feature，面向麻瓜也能有好的解釋性
* 以上，顯然具實用價值