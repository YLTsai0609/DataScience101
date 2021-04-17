
# [Data Augmentation in NLP Medium Post](https://towardsdatascience.com/data-augmentation-in-nlp-2801a34dfc28)


## 同義詞替換(Thesaurus)

找一個詞庫，或是字典，內容有記載詞以及替換詞，隨機將文本中的詞換成同義詞作為資料增強的手段

* 曾經有Paper採用過這種做法

## Word Embeddings & Contextulized Embedding

和同義詞替換同樣概念，不使用字典，使用訓練好的Word Embedding，讓模型找類似的字

* 曾經有Paper採用過這種做法

## Back Translation

用在翻譯任務上

假設要訓練的翻譯模型 語言是 English -> Cantonese(廣東話)

廣東話和英文之間的資料很少

可以找一大堆廣東話(Target Language) -> 翻譯成英文(Source Language)

就得到對應關係了!

可以標注很接近ground-truth，但不是ground-truth

* 曾經有論文採取過這種做法

## Text Generation

用於問答系統中

看起來效果沒很好

有論文使用過

# [《EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks》 for chinese](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)

2019, Aug, 200+ citations

## 同義詞替換

same idea with previous article.

(Synonmym Replacement-SR)
從句子中隨機選出$n$個不屬於停用詞集的單詞，並隨機替換他們

## 隨機插入

(Radom Insertion RI) 隨機找出句子某個不屬於停用詞集的詞，並從詞庫找出他們同義詞，插入句子中一個隨機位置，重複$n$次

## 隨機交換

(Random Swap, RS) : 隨機選擇句子中兩個單詞，並交換他們的位置，重複$n$次


## 隨機刪除

(Random Deletion, RD) : 以$p$的機率，隨機移除句子中的每個單詞

## 創新思路
以上方法，只有SR曾經被人研究過，其他三種方法都是本文作者首次提出

值得一提的是，常句子相對於短句子，存在一個特性，長句比短句有更多的單詞，因此長句子在保持原有類別標籤的情況下，可以吸更多噪聲

按照以上特性，作者提出一個方法，**基於句子長度來調整要改變的單詞數量**

$$n = \alpha l$$

$l$為句子長度，$\alpha$為一個句子要改變的單詞數量比例，對於每個句子來說，生成$n_{aug}$個增強句子

## 有效的原因

1. 生成類似原始資料的增強資料，有助於增加多樣性
2. 同義詞替換以及隨機插入，刪除，讓模型可以泛化倒不在訓練集中的單詞(詞庫中的詞)

## 風險

句子的增強版本，可能會改變原本的意思，但保留的原本的標籤，必須視應用場景來思考是否符合你的應用場景


# Lib

[nlpaug](https://github.com/makcedward/nlpaug)

[Chinese NLP Data Augmentation](https://github.com/InsaneLife/NLPDataAugmentation)

[《EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks》 for chinese](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)