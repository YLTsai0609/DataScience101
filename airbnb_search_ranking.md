# airbnb, 2018

[Real-time Personalization using Embeddings for Search Ranking at Airbnb, 2018 Best Paper](https://dl.acm.org/citation.cfm?id=3219885)

[translation](https://medium.com/life-of-small-data-engineer/embedding-recommendation-at-airbnb-2d68da7946d3)

Airbnb use embedding approach to increase 21% CTR.

# 產業特性

訂房網站

user - item interaction

1. user 行為更偏近於當下行為而非長期興趣(但user仍然會有長期旅遊偏好)
2. 和社群媒體不同，一個 user 不可能一天看 10+ 篇貼文
3. user 行為是 sparse 的，和旅遊淡旺季、各國連假時間有密切關聯


# User, Item 特性

* Item 數量 > User 數量
  * item 增長的數量 > user 增長的數量
  * 新 item > 新 user

* 對 user 所知 < 對 item 所知
  * item 房源認證通過後，屬性就幾乎不變了，改變的狀況可能是每年需要有審查房源的方式，確保提供的資源規格仍然和去年是一致的
  * user 對 item 的紀錄不多，反過來，item 對 user 的紀錄可能較多(也非常 skew 在熱門的 listing 上)
  * user 每次進入的意圖是不一定的，特別是在地區、人數、天數等都不一定有長期偏好

* user 變化 > item 變化
  * user 行為可能隨著假期長短、同團人數、自身經濟水平而改變
  * item 內容推出之後大多不在改變

* user cold start 嚴重性 >> item cold start 嚴重性
  * 新房源沒人看 --> 請他打廣告，降價、提供更完備的資訊等
  * 新使用者找不到自己想要訂的房間 --> 直接關係到營收

小結 : 

1. user 行為變化大，以當下需求的方式歸類並提供搜尋服務 (search) 會是較容易滿足使用者需求的方式
2. user 對 item 的點擊瀏覽資料較少、且幾乎不會對同雌個item有兩次訂閱行為，需要較多資料分析介入較容易幫 user / item 配對
3. u2i2i 會是長久有效的推薦方式

# How the service looks like?

https://www.airbnb.com.tw/s/homes?refinement_paths%5B%5D=%2Fhomes&date_picker_type=flexible_dates&search_mode=flex_destinations_search&search_type=filter_change&tab_id=home_tab&flexible_trip_lengths%5B%5D=seven_days_starting_long_weekend&location_search=MIN_MAP_BOUNDS&category_tag=Tag%3A8166

# listing embedding

1. 採用和 user embedding 相同長度的 vector，這樣 user 就可以和 listing 計算相似度 - 主要目標是房型、價位、地點...
2. for realtime search
3. TODO embedding and then?

# listing_type embedding 

1. 透過多個規則幫房間分類
2. for long-term user preference

# user_type embedding

1. 一般人一年旅行 1~2 次，針對個別使用者訓練 embedding 是不可行的
2. Many to one rule-based embedding mapping --> 相似的使用者使用同樣的 embedding
3. 分組規則?
4. for long-term user preference

# Training data

problem framing as : clf/reg/???

x, y : click session


## Positive samples

click session 

單一使用者在單次不中斷地瀏覽中，按照點擊的順序整理成一個序列，如果兩個點擊間隔超過30分鐘，則是為不同的 session 
其中又分為 exploratory session, booking session

data : 

```
[
    [click 1, click 2, click 3, ..., click m],
    [click 1, click 2, click 3, ..., click n],
    ...
]
```
## Negtive Samples

pass

# Model

word2vec --> Skip-gram 

給訂單個 item 得點擊，或預測前後 n 個點擊

# global context

如果該 session 中有物件最終有被下訂，那麼該點擊一定會參與計算，不論是否在前後 n 個 sliding window 中有物件最終有被下訂

# Congregated search

使用者通常單次搜尋只會找單一市場的物件、例如預計要停留的城市、因此 psotive 有很高機率是同個市場、隨機抽樣的 negtive 則是其他市場
但實驗表示，來自相同市場的的非 positivet. 抽樣為 negtive 效果更好


# item cold start

新的 item 沒有 embedding，根據方圓10英里內最相似的三個物件，embedding的平均就是新物件的 embedding

透過這個手法，可以讓 98% 以上的新物件都有 embedding


# Ref

[Is Word2vec a supervised/unsupervised learning algorithm?](https://www.quora.com/Is-Word2vec-a-supervised-unsupervised-learning-algorithm)

[Learn Word2Vec by implementing it in tensorflow](https://towardsdatascience.com/learn-word2vec-by-implementing-it-in-tensorflow-45641adaf2ac)