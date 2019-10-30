# Introduction 
* 關鍵字萃取不只有TFIDF, 還有RAKE以及TextRank，以下會介紹關鍵字共現、圖模型、RAKE、以及TextRank
* TODO 使用時機
NLP task pipeline
<img src = '/images/keywordExtraction_1.png'></img>
# 基本觀念
* Bag of Word / One Hot Encoding
* 差異在於 BOW會計算字數
<img src = '/images/keywordExtraction_2.png'></img>
<img src = '/images/keywordExtraction_3.png'></img>
# TFIDF 
### TFIDF 使用情境
# 共現
<img src = '/images/keywordExtraction_4.png'></img>
* 我們可以看到對角線的部分就是個關鍵字出總共出現在幾個文本中
  * 這個範例總共有1個文件，5個文本
  * 例如你出現在第2, 4, 5 3個文本中(同個文本出現了兩次你，仍然只算一次)，依序填完對角線
  * 共現的部分，我們就考慮，你和我總共一起出現在哪些文本，總共一起出現在第4,5個文本，所以為2
  * 整個矩陣是對稱矩陣，且為正值，為一個半正定(semi-postive matrix)
  * 這樣的矩陣基本上會隨著文本中友的字詞迅速膨脹，而且是一個dense matrix，有$O(N^{2})$的空間複雜度, $N$為文字數
# 詞彙圖(Graph / Network)
<img src = '/images/keywordExtraction_5.png'></img>
* 填好矩陣之後，我們就有所謂**共現次數**(等同於共現強度、共現分數等)以及網路關係(可以用在text rank中)
* 例如"你"和其他5個詞彙都有共現，但和"珍珠"沒有，這一點就可以反映在網路中(可以用在RAKE中)
* 有了這樣的網路之後，我們就可以應用在找關鍵字上了
# 詞頻 + 連結 = RAKE
* [詞頻]詞頻出現的越多，具有越高的普遍性，是關鍵字的可能性下降
* [連結]一個字時常跟其他常用字一起出現，是關鍵字的可能性上升
$$
TF = count~of~the~word~in~documents
$$
$$
Degree = Rank(word) - 1
$$
<img src = '/images/keywordExtraction_6.png'></img>
<img src = '/images/keywordExtraction_7.png'></img>
* 透過RAKE算法萃取出了關鍵字 : 珍珠、紅茶、拿鐵
* RAKE(rapid automatic keyword extraction)
### RAKE 使用情境
# Text Rank 
<img src = '/images/keywordExtraction_8.png'></img>
* 和Google搜尋引擎使用的PageRank基本上是相同原理，只是把text換成page
* 一個詞彙到底是不是一個關鍵字? 透過和這個詞彙共同ㄉ的其他詞彙來表達(某種embedding)
* Ex 拿鐵這個字的重要性，由紅茶，我，愛，你，奶茶來決定，該重要性稱為Weight Score $WS(word)$
$$
WS(拿鐵) = (1-d) + d*相鄰結點分數
$$
$$
d~~~ smoothing parameter
$$
d越小，相鄰節點的影響越小
<img src = '/images/keywordExtraction_9.png'></img>
* 先考慮紅茶，紅茶與3個關鍵字相連，其中一個是拿鐵，因此乘上1/3，再乘上$WS(紅茶)$，實際上就是 $ WS(紅茶) \frac{1}{Degree(紅茶)}$
<img src = '/images/keywordExtraction_10.png'></img>
* 在考慮我，我和很多詞彙都相連，使得我和拿鐵的關聯性沒那麼高，因此weight就比較小
### 小結 : 
* 從上推論來看，如果有一組字只和拿鐵一起出現，這會使得對於$WS(拿鐵)$的貢獻度在權重的部分是 1，充分展現了共現
<img src = '/images/keywordExtraction_11.png'></img>
* 雞生蛋，蛋生雞問題，給一個初始值，用遞迴跑破解，可以得到收斂的Weighted Score
### 公式與收斂展示
<img src = '/images/keywordExtraction_12.png'></img>
### TextRank 使用情境
* 我們可以看到，"愛"有最高的weighted score，這是因為"愛"常常是連接主詞和受詞之間的橋樑，使得"愛"的分數較高，TextRank被用來找出辭彙語詞彙之間的橋樑作為一種關鍵字萃取方式