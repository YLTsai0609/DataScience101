# Pros and Cons
|Pros|Cons|
|----|----|
|1. 可解釋性(皆為正，且據統計解釋) <br> 2. 非線性但是可解釋ㄅ1. 可能跑很慢 <br> 2. 比起樹模型準確度還是蠻差的|

# Resource
[Interpretable Machine Learning 4-3 GAMs](https://christophm.github.io/interpretable-ml-book/extend-lm.html#gam)
[Python GAM -pyGAM, star 450+](https://github.com/dswah/pyGAM)
[Introduction Article 660+](https://codeburst.io/pygam-getting-started-with-generalized-additive-models-in-python-457df5b4705f?source=bookmarks---------0------------------)

# Hints
* 本質上是GLM的拓展，原本GLM，x只能是線性關係，GAM中x可以是非線性關係了
  * $GLM : y=\beta_{0} + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_p x_p + \epsilon$
  * $GAM : g(E_{Y}(y|x))= \beta_{0} + f_1 (x_1) + f_2 (x_2) + ... + f_p (x_p)$
* Additive model在解釋時都有很大的方便(像是Non-Negtive Matrix Factorization)
* 有各種統計量，是一個面對統計背景好解釋的模型
* 有Patial Dependence Plot with feature，面向麻瓜也能有好的解釋性
* GAM顯然無法用gradient descent優化，要用其他招數
* 以上，顯然具實用價值