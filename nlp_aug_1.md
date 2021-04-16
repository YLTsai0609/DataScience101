# Ref

[Data Augmentation in NLP](https://towardsdatascience.com/data-augmentation-in-nlp-2801a34dfc28)

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

# Lib

[nlpaug](https://github.com/makcedward/nlpaug)

[Chinese NLP Data Augmentation](https://github.com/InsaneLife/NLPDataAugmentation)

[《EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks》 for chinese](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)