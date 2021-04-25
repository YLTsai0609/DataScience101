# kashgari

kashgari是一套將BERT模型推展到產品級的套件，特色是
簡單，容易使用，了解，修改，規模化，且能夠直接部署到雲端上

# Profiling BERT NER

# Code Analysis

[Kashgari github](https://github.com/BrikerMan/Kashgari)

有使用到的部分

QA : 

1. BERT的模型結構被藏在哪裡?
2. TextProcessor怎麼做的? - 是MultiProcessing嗎?
3. Tokenizer怎麼做的，怎麼自定義詞典

Training

`from kashgari.callbacks import EvalCallBack`

`from kashgari.embeddings.bert_embedding import BertEmbedding`

`from kashgari.tasks.labeling import (BiLSTM_CRF_Model)` - Model物件

Basically based on [bert4keras](https://github.com/bojone/bert4keras#%E5%8A%9F%E8%83%BD)

重點 : BertEmbedding_Model Tokenizer

Inference

重點 : TextProcessor

# BertEmbedding

![img](images/kashgari_1.png)

這裡的`BertEmbedding`繼承了`TransformerEmbedding`，看起來`BertEmbedding`中沒有比`TransformaerEMbedding`多太多東西，不過可以看到模型載入時會直接讀取相關的


`vocat.txt`

`bert_config.json`

`bert_model.ckpt`

![img](images/kashgari_2.png)

接著進入到`TrainformerEmbedding`物件來看，可以看到`TransformerEbmbedding`繼承了`ABCEmbedding`，並且會被`Seq2Seq`以及`ABCTadkModel`使用到，那麼這一層定義了哪些事情?

1. 可以看到`kashgari`的套件中很多物件都定義了`to_dict`，這使得將物件以dict的方式表達變得容易，若要以API傳送相關參數也會方便很多
2. `load_embed_vocab` - 載入embedding model的辭典並把它轉換為一個token字典
3. `build_embedding_model` - 載入模型參數，並以`bert4keras`這個套件把模型建立起來，接著把每一層bert encoding layer的參數freeze

![img](images/kashgari_3.png)

那麼`ABCEmbedding`物件中定義了哪些東西呢?

基本上的屬性有`embedding_size`, 以及`text_processor`，也是說當我們load bert model時，也可以傳入，text_processor

`ABCEmbedding`定義哪些行為呢?

1. `setup_text_processor` - 將text_prcessor中的一些屬性傳過來，例如`token2idx`
2. `build_embedding_model` - 宣告了繼承的物件要實作這個方法
3. `load_embed_vocab` - 宣高了繼承的物件要實作這個方法
4. `get_seq_length_from_corpus` - 了解文本中序列長度會使用到的method
5. `embed` - 把input sentecne 經過 text prcoessor處理，再經由embedding model predict，最後回傳embedding result(np.array)

![img](images/kashgari_5.png)

![img](images/kashgari_4.png)


# Text Processor

## Corpus Genrator

# ABCTask Model

# Tokenizer

# vocab.txt


# Reference
