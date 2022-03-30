
# 資料搜集(資料理解、資料可用性分析)

1. 該資料如何被產生的? 
   1. e.g. events - 觸發時機? - 有助於了解**資料解析度**，**如何訂定匯總層級**，**是否藏有 bias**，**該資料可分析的結論極限為何**
   2. 是否可重現? - 驗證、 double check 資料被產生的機制 - **避免錯誤的資料理解**
   3. 觸發頻率 - 每次符合條件就發生? 每 200 ms 觸發一次? ... - 有助於了解 **資料解析度**，**如何訂定匯總層級**，**是否藏有 bias**
2. 盤點對應資料
   1. DB / DW / DL(data lake) 是否相關的資料都已經被 review，可進行分析 - **資料是否可導出分析結論 ,該資料可分析的結論極限為何**


# 資料分佈(資料理解、資料可用性分析)
1. 資料解析度(顆粒度)
   1. 每一 row 代表的層級為何? 是一個 cookie, 還是一個 cookie, url, 還是一個 url, compain position, 還是一個 url?
   2. 數值欄位的單位 -  stay_time 的單位是 (s / ms / day ?)
   3. 有沒有重複值(特別是 cookie, url, ...)
2. 資料分布
   1. your best friend - [pandas profiling](https://github.com/ydataai/pandas-profiling) - **避開/探索 outlier，避免錯誤的 filter, 結論等**
   2. 交叉驗證 - 如果有 假設A ，其他資料集是否可以和目標資料集反映出 假設A 的事實 - **避免錯誤的資料理解**
   3. 資料合理性 - 中位數、平均數、是否反映了 一般 user / domain expert 對該產品的認知(e.g. 一個使用者一天不會進入一個網頁超過 N 次) - **避免錯誤的資料理解**


# 資料分析(驗證假設)

1. 資料理解是否正確無誤(顆粒度、單位、是否有重複資料列、每日資料列數是否合理)
2. 交叉驗證 - 類似的分析方法應當看到相似的結論 - **避免錯誤的結論、建立對結論的信心**
3. if 抽樣 
   1. boostraping 的 batch size 需要多大才能反應事實(透過 std in trials 來判斷) - **避免錯誤的結論、建立對結論的信心**
4. check 辛普森悖論
   1. 是否有重要的 dimension 沒有切分開來看過? 
      1. e.g. CTR Model A > CTR Model B, but CTR Model B / mobile, desktop both win