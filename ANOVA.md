# ANOVA
ANOVA(Analysis of Variance) - 變異數分析
主要為探討連續型（Continuous）資料型態之應變數(Dependent variable）與類別型資料型態之自變數(Independent variable）的關係，當自變項的因子中包含等於或超過三個類別情況下，檢定其各類別間平均數是否相等的統計模式

Let's start from start from **t-test**
## T-test
* 白話文 : 兩組連續變數是否一致
* 更數學地說 : 兩組連續變數是否來自於同一個分佈?
* 關於Z-score以及 t-score
* Z score 知道母體平均的情況下
  $$
  Z_{i} = \frac{x_{i} - \mu}{\sigma}
  $$
  此時假設了隨機變數$x_{i}$符合高斯分佈，且為母體中的隨機變數，$\mu$為母體平均數，$\sigma$為母體標準差
* t score 不知道母體平均數的情況下，考慮從樣本來建立一個樣本分佈，且在樣本數夠多的情況下逼近母體分佈。
  $$
  t = \frac{\bar{x} - \mu}{\frac{S}{\sqrt{n}}}
  $$
  此時假設了$x_{i}$為取自常態分佈母體$(\mu, \sigma)$的隨機樣本，且樣本均值為$\bar{x}$，樣本標準差為$S=\frac{\sum(x_{i} - \bar{x})^{2}}{n-1}$用來推估母體標準差。
  樣本數為$n$，自由度為$n-1$，此時可以從一組抽樣樣本$x_{i}$得到一個t-score，t-score則會對應到一個t分佈，
  該分佈是一個t-score的函數 : 
  <img src='AVONA_1.png'></img>
[t test wiki](https://zh.wikipedia.org/wiki/%E5%AD%B8%E7%94%9Ft%E6%AA%A2%E9%A9%97)
## proportion test(Z test)
* target 是 0, 1
* 例如總統大選民調
* [Z test](https://www.statisticshowto.datasciencecentral.com/z-test/?fbclid=IwAR2fliMjso6O3zpaKyZH-2YqktHP1q1qEEt0-3uBnaVbQiVp32tGy2pHzSk)
### t-test的三種樣態
* 關於下列三種樣本類型，t-score的算法各有不同，也會對應到不同的樣本t分佈
### 單一樣本
* 單一樣本 t-test : 畫出分佈，查看分佈區間是否有涵蓋的猜測值(或稱為期望值)($\mu$)
* **e.g.所有的小費是不是平均值在2.5?**
* Null Hypothesis $H_{0}$ : 小費的平均值在2.5
* Alternative Hypothesis $H_{1}$ : 小費的平均值不是2.5
### 獨立雙樣本
* 男生vs女生(老人vs小孩) 小費是否有差異?
* Null Hypothesis $H_{0}$ : 男生vs女生所收到的小費**沒有差異**
* Alternative Hypothesis $H_{1}$ : 男生vs女生所收到的小費**有差異**
### 成對樣本
* 爸爸vs小孩 小費是否有差異 (樣本之間必須有某種關係)

* Null Hypothesis $H_{0}$ : 爸爸vs小孩所收到的小費**沒有差異**
* Alternative Hypothesis $H_{1}$ : 爸爸vs小孩所收到的小費**有差異**

###

Demo case

### 1 way ANOVA
* 獨立樣本的延伸版本，n組以上獨立樣本，$n \leq 3$
* 有三種房型，整棟，套房，共享房間
* H_{0} u_1 = u_2 = u_3 : 三種房型，選擇哪種房型並不影響價格
* H_{1} 至少有一個u不同 : 有任何一種房型的價格分佈與其他價格分佈有顯著差異
* F-value,
* df = dgree of freedom 
* resudials N of datapoint - df
* 組間平均差
* 穩定組內平均差SST，SSB，SSW
$$
SST = SSB + SSW = \sum_{i}^{K}\sum_{j}^{n_j}Y_{ij}^{2} - <Y>
$$
$$
SSB
$$
$$
F = \frac{MSB}{MSW} = \frac{SSB/df}{SSW/df}
$$
* within(組內)
* total(總共)
* between(B)
* 事後檢定 : 到底哪一組不一樣?
## Tukey HSD
* 類似t-test, 用於ANOVA之後的兩兩比較，找出獨立的那一項

## 2 way ANOVA
考慮interaction，例如考慮兩個變量 地區 + 房型 vs 價格
一樣$H_0$為all equal
事實上也可以放兩個特徵，target為price，metric為$R^{2}$
如果比$R^{2}$趨近於noise level，那麼就可以說兩個變量對target是沒有影響的，反之如果有差別，那麼就可以說哪個值是有影響的
