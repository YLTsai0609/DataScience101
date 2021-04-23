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

`from kashgari.tasks.labeling import (BiLSTM_CRF_Model)`

Basically based on [bert4keras](https://github.com/bojone/bert4keras#%E5%8A%9F%E8%83%BD)

重點 : BertEmbedding_Model Tokenizer



Inference

重點 : TextProcessor


