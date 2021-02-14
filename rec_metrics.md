# Reference

[Recommender Playground from yltsai](https://github.com/YLTsai0609/recommender_playground)

[推薦系統實踐 - 項亮 2010](https://github.com/jzmq/book/blob/master/novel/%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F%E5%AE%9E%E8%B7%B5.pdf)

# Coverage

內容商應當最在意的指標 - 顯示了所有物品有多少被推薦出去，指標有很多種方式定義，以下是最簡單的一種定義(同時也被使用在`RecModel`中)

<img src='./images/recmetric_1.jpg'></img>

from : 推薦系統實踐

## different version coverage


# Recall & Precision

能夠被離線計算的指標，通常看Recall，來評估在訓練集所收集的時間區段中，平均每$a$個使用者點擊會有$b$個是系統推薦

這兩個指標是以**點擊數量**作為評估標準，容易失準的地方就是有的使用者很愛點擊東西，或是有機器人一直點擊，會把點擊數衝高

<img src='./images/recmetric_2.jpg'></img>

from : 推薦系統實踐


# Hit Ratio


$$
\frac{\#~hits}{\#~users}
$$

$\#~hits$ : 推薦列表N在確實有涵蓋使用者點擊
$\#~users$ : 使用者數量

同Recall，但以使用者數量作為評估基準，單個使用者就算有30個點擊且系統推薦出5個，hits不會是5，仍然是1

[slim 2011](http://glaros.dtc.umn.edu/gkhome/fetch/papers/SLIM2011icdm.pdf)