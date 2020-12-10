# Case Study

# Overall Architecture

1. Candidate generation - $N$ models to guess what you will like, output a candidate list
2. Ranking model - filter the candidate from big number to small number
3. realtime picking - pick the most possible k(when you are using the app)

# Netflix, 2013

System Architectures for Personalization and Recommendation

[post](https://netflixtechblog.com/system-architectures-for-personalization-and-recommendation-e081aa94b5d8)

[post-translation](https://kknews.cc/zh-tw/code/g48e2o9.html)

Key takeaway - offline, nearline, online (use data avaiability and training time to build it)

    offline - hours / days to response
    nearline - minutes / seconds to response
    online - in 100ms  to response

# Integram, 2019

Powered by AI: Instagram’s Explore recommender system

[post](Powered by AI: Instagram’s Explore recommender system)

[post-trainslation]*https://yehjames.medium.com/instagram-%E6%8E%A8%E8%96%A6%E7%B3%BB%E7%B5%B1%E4%BB%8B%E7%B4%B9-%E5%88%86%E6%9E%90explore%E6%8E%A2%E7%B4%A2%E9%A0%81%E9%9D%A2%E7%9A%84%E5%80%8B%E4%BA%BA%E5%8C%96%E6%8E%A8%E8%96%A6%E7%AE%97%E6%B3%95-792d03fda228

Key takeaway - 

1. diversity and novelty is the goal of instegram explore recommender. use such a metric to evaluate the model.
2. 3 stage to break down the ranking, the model performance improved!

   1. 500 -> 150
   2. 150 -> 50
   3. 50 -> 25
