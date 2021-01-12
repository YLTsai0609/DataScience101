# 資料科學導入企業工作流程

1. 看資料、收集資料(沒資料什麼都是假的)
2. 最快能動的可行方案

   1. 收集專家知識、建Feature
   2. rule based, linear reg, decision tree, statistical regrssion(explainable)
   3. (optional) 模型評估，更多時候直接上線看成效

3. 進入優化循環 - 一邊實驗新模型、一邊收技術債

# 理想與現實 - 真正的Bottleneck在哪裡?

## 理想的分工

1. 收斂有價值的商業問題，轉化為資料科學問題(Business Understanding) - 溝通工作、亦可能需要一些政治力量
2. 資料收集(Data Collection) - 有人幫你收log或是爬蟲抓資料
3. 資料湖泊與資料倉庫(Data Lake / Data Warehouse) - 有人幫你弄好分散式儲存，管理所有資料庫
4. 資料流程(Data Pipelining) - 有人幫你管理、維護錯綜復雜的資料流
5. 資料清理(Data Cleaning) - 有人幫你清資料、進來的資料都可以直接用
6. 建模分析(Modeling/Analysis) - 你的最愛

## 殘酷的事實

小團隊全部自幹，5%時間在建模分析，95%時間都在搞工程

那些Bottle neck

| 類別                    | 項目                    | 備註                                                          |
|-------------------------|-------------------------|---------------------------------------------------------------|
| 資料清理(Data Cleaning)  | 非結構化、雜訊、被污染       |                                                               |
| 資料管理(Data Governance) | 隱私控管、上下游管理、知識管理 | 每個Team會進行自己的資料轉換，資料到下游就會亂成一團，花很多時間在工程整治 |

## 科學、工程

### 相同處

都需要管理、溝通、實驗

1. 貫穿全部的專案管理
2. 瞭解跟其他團隊的橫向需求/供給協調
3. 向上管理報告
4. 跑大地、考古挖資料
5. A/B 測試如何設計
6. 上線之後如何根據得到的結果修正、砍掉重練、嘗試新的模型

### 相異處

#### 解決的問題不同

商業問題(縱向) vs 一般化、讓類似問題可以快速解(橫向)

DS/DA/BA 注重商業應用

DE 處理平臺問題，維護平台穩定，讓下一個問題能夠得到快速解答

#### 思考模式不同

由於兩種工作的思維邏輯不同，常常在工程團隊造成大量的技術債，這會造成隱性的惡性循環

商業思維 : 以客戶為主要面向、強調產品價值、快速試錯、驗證最小可行方案，短期容易看見成果

工程思維 : 可靠性、穩定性、泛用性、可擴展性 - 短期內較難看見成效，但具有可規模化，可讓類似任務便容易等特性

## 案例分析

### 解決 X-Y 問題 (以團隊領導人或是產品經理的角度下去思考）

照著要求做很可能事倍功半

了解科學家的痛點則會事半功倍

### 建立合作關係

提供工程師能理解的急迫原因與作法

規劃償還技術債

提供一個藍圖來解決技術債，讓付出的勞力規模化，而不是僅提供一次性的產品

## 資料科學的工作不確定性

工程產品多數要解決的問題已有現成方案可以套用，而資料科學的產品很多時候找不到現成的資源，就算找到了，也會因為演算法不同而不一定套用於實際運用，以下四種情況也是資料科學工程中常見的。

1. 跨團隊合作經驗

一個人什麼都做不了，需要邀請PM或客服支援與協助資料搜集

小組織 和 大公司的合作模式也不同，合作會一直像是在做新的東西，也需要很多磨合。

2. 領域知識

ML 最重要的是找出 features，但如何定義要使用的 features，有些時候在該領域久了的同事，雖然不是資料科學家或工程師，但他們提出的 features 往往會更準確的達到目的。

3. 應用模型的實務經驗

工程問題會涉及很多的現實問題，例如因爲政治影響團隊之間的合作模式，這部分需要累積足夠的產業經驗來做實驗。

4. 客戶買不買單是另一回事，市場無法準確預測到所有的問題

探索的過程，時程難估

一開始：不知道問題是什麼、資料是什麼就要動工

常見問題：要試多少 feature/model？做到多好才算完成？Accuracy 100% 就算完工了嗎？

經驗是當有更緊急專案的出現，這個專案才有機會進入“維護模式”（笑）

2. Cold Start 成效差

持續搜集資料要多久才能收集足夠資料？Model 不夠好？要測試多久？

根據統計與檢定數值（x）上線測試直到客戶不抱怨為止（o）

3. Sprint 一次多長？

工程師在跑Sprint的流程是訂製一個時間衝刺，在時間內做得完的Tasks，但是資料科學家是一直在測試不同模型，實際上時間很難控制。

資料科學用「看板」更實際，不是用時間上的限制 ，而是用優先順序去規劃。

# Reference

[在日本，看見資料科學工程的趨勢 Connor(leafwind) | 資料工程師 ＠日本 SmartNews](https://medium.com/twdsmeetup/%E5%9C%A8%E6%97%A5%E6%9C%AC%E7%9C%8B%E8%A6%8B%E8%B3%87%E6%96%99%E7%A7%91%E5%AD%B8%E5%B7%A5%E7%A8%8B%E7%9A%84%E8%B6%A8%E5%8B%A2-b65540fa0426)