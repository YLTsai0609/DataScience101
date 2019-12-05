# NLP_Model_evaluation
## Introduction
評價語言模型的一種方式
將語句視為一個詞語序列
$$
S=W_{1},W_{2},...,W_{k}
$$
這個句子出現的機率可以按照條件機率表示法
$$
P(S) = P(W_{1},W_{2},...,W_{k}) = P(W_{1})P(W_{2}|W_{1})..P(W_{k}|W_{1},W_{2},...,W_{k-1})
$$
也就是說在給定一句話的前$k$個詞，我們希望語言模型可以預測第$k+1$個詞是什麼，即給了第$k$個詞，出現的機率分佈$P(W_{k+1}|W_{1},W_{2},...,W_{k})$，可以想像會有好多個字/詞，分別有對應的機率，形成一個機率分佈
## What is a good model?
* 將模型應用到具體的問題中，例如翻譯，拼字檢查，然後觀察這個模型的表現，但是耗時，也可難以操作，但卻是我們要的終極目標
## perplexity
