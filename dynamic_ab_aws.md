# Growth Analytics Bootcamp

* Starup - 錢燒完之前找到 product market fit.
  * which means user acuqsition (new user traffic is important)
* 15% A/B Testing win and beat the hypoethsis

# Dynamic A/B Testing

* Tino - Houzz A/B
* Growth Analytics - 酷朋 A/B

# Causal Model in Practice

A/B --> 就是想要做 Causal Inference

[Lyft](https://eng.lyft.com/causal-forecasting-at-lyft-part-1-14cca6ff3d6d)

[Netflix](https://netflixtechblog.com/a-survey-of-causal-inference-applications-at-netflix-b62d25175e6f)

* 為何大公司最後都會設計自己的實驗平台?
  * A/B win rate 過低， traffic 浪費， product win 需要很多次成功的 hypothesis --> means we need causal inference

* 偷看實驗 --> 就像偷看骰子什麼時候摋到 1 (Sequential Testing)

[Notifications: why less is more — how Facebook has been increasing both user satisfaction and app usage by sending only a few notifications Analytics at Meta](https://medium.com/@AnalyticsAtMeta/notifications-why-less-is-more-how-facebook-has-been-increasing-both-user-satisfaction-and-app-9463f7325e7d)


[How Meta tests products with strong network effects](https://medium.com/@AnalyticsAtMeta/how-meta-tests-products-with-strong-network-effects-96003a056c2c)

* A/B --> A組被影響，B組連帶影響 (buyer funnel vs seller funnel) 會受到 network effect 影響
  * 例如 A 組發優惠券，瘋狂叫車，會使得叫車價格上升，而 B 組的需求就會下降

[Beyond A/B Test : Speeding up Airbnb Search Ranking Experimentation through Interleaving](https://medium.com/airbnb-engineering/beyond-a-b-test-speeding-up-airbnb-search-ranking-experimentation-through-interleaving-7087afa09c8e)

* Interleaving experimentation framework
  * offline 先 win
  * pick most potential target audience
  * A/B 之前

[MAB Use Case at Uber](https://www.uber.com/en-TW/blog/xp/)

[How to Use Quasi-experiments and Counterfactuals to Build Great Products - Shopify](https://shopify.engineering/using-quasi-experiments-counterfactuals)

[Evaluating the helpfulness of AI-enhanced catalogue data](https://www.amazon.science/blog/evaluating-the-helpfulness-of-ai-enhanced-catalogue-data)


[Trustworthy experiments - books - Ron Kohavi](TODO)

[Awesome Causal Inference](https://github.com/matteocourthoud/awesome-causal-inference)

# Amazon A/B Testing Platform

Product win --> 15% A/B wins --> faster A/B help product

* how to make it fast?
* 運費是不是購買的阻礙

![alt text](images/ab-aws-image.png)

* A/B 能不能夠變成非技術人員可以 self-service? - WEBLAB deparment
* 早期來說就人工安排實驗
* 中期 --> build up A/B Testing Platform
* 後期 --> 連 Review 的過程都變成 ML Scan document
* 要降低漫無目的的亂測 - 定義關鍵元素要填表格

![alt text](images/ab-aws-image-1.png)

![alt text](images/ab-aws-image-2.png)

* Peeking - Sample size 還不夠，不能提早結束
* Cherry Picking - 不是你的 target metric improve, 不是你的功

![alt text](images/ab-aws-image-3.png)

* 隨著你的實驗跑越來越多次，需要多少 traffic 可以用 ML 自動決策給實驗需求者

![alt text](images/ab-aws-image-4.png)


![alt text](images/ab-aws-image-5.png)

# Coupang A/B Testing Platform

![alt text](images/ab-aws-image-6.png)

* 成效

![alt text](images/ab-aws-image-8.png)

![alt text](images/ab-aws-image-7.png)

![alt text](images/ab-aws-image-9.png)

![alt text](images/ab-aws-image-10.png)

![alt text](images/ab-aws-image-11.png)

![alt text](images/ab-aws-image-12.png)

* CI 檢測會不會整個 Failed (講白了就是把人工 Review 工具化)

![alt text](images/ab-aws-image-13.png)

* config / application 解耦合

![alt text](images/ab-aws-image-14.png)

![alt text](images/ab-aws-image-15.png)

# 自動停止不良實驗 --> faster iterations

![alt text](images/ab-aws-image-16.png)

![alt text](images/ab-aws-image-17.png)

![alt text](images/ab-aws-image-18.png)

# 實驗報告的即時性 & 準確性

![alt text](images/ab-aws-image-19.png)

![alt text](images/ab-aws-image-20.png)

![alt text](images/ab-aws-image-21.png)

* 從新功能 / impact 小的地方開始引入實驗平台
* 實驗平台沒有辦法改變實驗文化 XD

# Houzz use case

* Houzz - two-side market, b2c platform
* Tino

## Geo-based experiments

![alt text](images/ab-aws-image-24.png)

* A/B 的假設是 AB 互不影響，但是 Lyft 的優位券發送，會打破這個假設(network effect)，所以變更 randomization unit ， 有助於假設不被打破

![alt text](images/ab-aws-image-25.png)

* Geo 相比 user 的 network effect 更小
  * 相似 market --> LA/NY

![alt text](images/ab-aws-image-27.png)


* disadvantage

# Design Geo-Exp

1. Geo-Feanularity
   1. granularity - zip --> State

![alt text](images/ab-aws-image-28.png)

* spillovers --> 一個設計師會同時面對 control and treament, 打破假設 (Sub metro)
* DMA --> 不會打破假設(設計師是有地域性的)
* DMA --> randomization unit 變得很少

# How to randomize the Geo unit

![alt text](images/ab-aws-image-31.png)

* Houzz --> clustering + Repeated randomization

![alt text](images/ab-aws-image-32.png)


![alt text](images/ab-aws-image-33.png)

* 以上都有做 PoC
* 但 Houzz 最終使用的
  * East to understand, transparent, and let stakeholder buy in.
  * Matching and statified randomization

![alt text](images/ab-aws-image-34.png)

![alt text](images/ab-aws-image-35.png)


# Validation two groups


![alt text](images/ab-aws-image-36.png)

* need to pick all metrics we cared about
* robust check

![alt text](images/ab-aws-image-37.png)


# 實驗開跑

![alt text](images/ab-aws-image-38.png)

* Time-based regression

![alt text](images/ab-aws-image-40.png)

* Difference in Differences
* pre-test
  * common trend 其實很難 identify 
  * treament effect 比 common trend 小太多
* analysis plan --> 避免 cherrypick

# DataDI

![alt text](images/ab-aws-image-41.png)

* 金融、零售

![alt text](images/ab-aws-image-42.png)

![alt text](images/ab-aws-image-43.png)

![alt text](images/ab-aws-image-44.png)

![alt text](images/ab-aws-image-45.png)

![alt text](images/ab-aws-image-46.png)

* Build up Experiment platform & Detailed Event-tracking system

![alt text](images/ab-aws-image-47.png)

![alt text](images/ab-aws-image-48.png)

## Landing Conversion Funnel

user acqusition - 1500元/人，但是驗證碼按鈕真的很爛 --> 流失率從50% --> 9%

## User Engagement

![alt text](images/ab-aws-image-49.png)

* 線上開戶，有拿開戶禮，轉換率是16倍，但是只有20%的人收到

## EDM

![alt text](images/ab-aws-image-50.png)

* 不只降低成本，還可以提升轉換率(把平常不開信的人過濾掉就好)

![alt text](images/ab-aws-image-51.png)

## 遊戲課金

![alt text](images/ab-aws-image-52.png)

## 化妝品商品頁測試

![alt text](images/ab-aws-image-53.png)

## 行銷文案測試(話術測試)

![alt text](images/ab-aws-image-54.png)

通常最有效的文案 - 限制、獨家、你有他沒有 --> 未必要給定時間地點的 CallToAction

## 沈睡客戶召回

![alt text](images/ab-aws-image-55.png)

* 台灣的自有產品實驗不多，但是行銷或是業務場景非常多，可以做實驗，磨練文案和話術

# DataDI

![alt text](images/ab-aws-image-56.png)

![alt text](images/ab-aws-image-57.png)

![alt text](images/ab-aws-image-58.png)

* 流量正交 -- 不同實驗不同組 test/control

![alt text](images/ab-aws-image-59.png)


![alt text](images/ab-aws-image-60.png)

![alt text](images/ab-aws-image-61.png)

![alt text](images/ab-aws-image-62.png)

* Aug - LINE/OCard - 講 Retension

# A/B Testing --> MAB Testing

* 兩大 A/B Testing 的痛點
* Control group - 一定要走完實驗嗎? 能不能早點結束 (Bayesian) - 可能的話7天之內
* Control group - 降低 experiment impact
* long term metrics is decreasing <---> short term metrics is increasing
  * short-term experiment --> long-term experiment
  * e.g. 不用錢! CTR 噴高， Revenue 歸零
  * 

* 大部分廣告系統實驗都是 MAB Testing
* Random / Eplison / UCB / Thompson sampling
* A/B Routing --> MAB Rounting (AWS 幫你 build 好了)