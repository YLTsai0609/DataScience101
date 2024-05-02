[【機器學習2021】Transformer (上)](https://www.youtube.com/watch?v=n9TlOhRjYoc&list=PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J&index=12&t=566s)

# Seq2Seq Model

* Input : sequence (a set of vector)
* Output : sequence (a set of vector)
* 語音辨識
  * In : 語音訊號
  * Out : 你好嗎? (長度無法確定)
* 機器翻譯
  * In : 某一國語言
  * Out : 另外一國語言，長度無法確定
* 語音翻譯
  * In : Machine Learning 的聲音訊號
  * Out : "機器學習"
  * 世界上有7000種語言不存在文字，且 end2end 可能計算得更快

<img src='./assets/tsf_1.png'></img>

# 台語語音轉繁體中文

母湯的聲音訊號 --> Model --> 不行

<img src='./assets/tsf_2.png'></img>

label : Youtube 上的台語影集，加上中文字幕

noisy

* 背景雜音?
* 不同人聲的口音?
* 台語音標?
* 如果都不管， Transformer baseline 還是表現得不錯

<img src='./assets/tsf_3.png'></img>

<img src='./assets/tsf_4.png'></img>

好與不好

好

* 多音節 --> 輸出音節數不同

不好

* 倒裝句
* 同樣聲音片段，容易聽成不同意思

# 中文文字 --> 台語聲音訊號
* Text to Speech (TTS) Synthesis

<img src='./assets/tsf_5.png'></img>


# NLP 使用上更加廣泛，理由是因為 seq2seq 幾乎是所有 Task 的母集合

<img src='./assets/tsf_6.png'></img>

Chat Bot (Question Answering) 幾乎是所有 NLP 問題的母集合

* QA - ok
* NER --> 給定一段文章，問他裡面的人是誰
* 文章摘要 --> 給定一段文章，問他總結
* 情緒辨識 --> 給定一段文章，問他正面還是負面
* QA 問題可以用 seq2seq 來解

<img src='./assets/tsf_7.png'></img>

* NLP 提供 Strong Baseline，但下游必須用其他不同的客製化模型，會做得更好

## Seq2seq 用於句法樹解析

Input : sequence
Output : parsing tree as a sequence (like programming language) - 2014, Dec


<img src='./assets/tsf_8.png'></img>



<img src='./assets/tsf_9.png'></img>

* 把 Grammar 當作一個語言，硬做，結果竟然是 SOTA
* 而且訓練時沒用什麼 tips，連 Adam 都沒有用， SGD 就 train 起來了
* 以文法來說，其實輸出類別非常之少

* 甚至圖片也可以轉換成 2D 文字


## Seq2seq for Multi-Label Classification

* 同個 Entity (Article) 屬於多個 class (例如多個 tags)
  * 如果用 Multi-class 解題，行不通的原因是，每一篇文章對應的 tags 數量可能是不同的

<img src='./assets/tsf_10.png'></img>

## Seq2Seq for Object Detection


<img src='./assets/tsf_11.png'></img>

* 輸出不知道是幾隻斑馬，就像是一個 Set of bounding box ， CV 也可以 end2end 用 transformer 解題

# Seq2seq


<img src='./assets/tsf_12.png'></img>

* 早期用的是 RNN， LSTM，現在用的是 Attention

# Encoder

<img src='./assets/tsf_13.png'></img>

* RNN, CNN, Self-attention 都可以作為 Encoder 的主要設計單元， Transformer 主要採用 Self-Attention

* 簡化版 - Transformer Encoder =  self-attention(含 positional encoder) + FeedForward Network (fc)
* 詳細版本 - self-attention + resudual + layer normalization + fc + resudual + layer normalization

<img src='./assets/tsf_14.png'></img>

<img src='./assets/tsf_15.png'></img>

* resudial 的意義 - 做過轉換的 vec 直接加上輸入的 vec，這樣優化的部分可以做少一點事情 --> 大量使用，意義為加速訓練收斂
* layer normalization
  * 輸入一個 vec，輸出一個 vec
  * 同一個 instance，不同 features 之間，做標準化, mean = 0, std = 1
* batch normalization
  * 考慮多個 samples, layer normalization 則更簡單一點

* 所以對應回去 paper 的圖， Add & Norm = residual + Layer Normalization

<img src='./assets/tsf_16.png'></img>

<img src='./assets/tsf_17.png'></img>

* 以上是 Transformer 預設架構，並非 optimal， layer normalization, residaul 的必要性，需要重複幾次等等，都是可以實驗的

# Decoder