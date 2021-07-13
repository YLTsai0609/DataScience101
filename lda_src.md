# 目標

1. 理解LDA
2. 探索LDA是否可以透過tensorflow的系統來解(maximum likelihood by adam)
3. 探索如何結合Probabilistics Matrix Factorization，之後可作為Collabrative Topic Model的背景知識(Online learning Recommendation)

## Not found in ...

because the implementation is easy to understand.

[A collection of minimal and clean implementations of machine learning algorithms 8.3k+](https://github.com/rushter/MLAlgorithms)

[Python implementations of some of the fundamental Machine Learning models and algorithms from scratch 18.8k](https://github.com/eriklindernoren/ML-From-Scratch)


## dongwookim-ml / python-topic-model stars 350+

https://github.com/dongwookim-ml/python-topic-model

* pure python
* lda
  * Collapsed Gibbs sampling
  * Variational inference
* CollaborativeTopicModel - 2011
  * optimizer (nelder-mead) there are might be NaN
* **easy to understand**

## Scikit-Learn star 46.4k+

https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/decomposition/_lda.py

* pure python!
* sparse matrix supported.
* Online Latent Dirichlet Allocation with variational inference 2010
* optimizer : EM 
* **useful when we wanna implement our algo robust.**

## tensorflow / probability

https://github.com/scikit-learn/scikit-learn/blob/main/sklearn/decomposition/_lda.py


* high level probability layer
* use Adam optimizer
* might some exception, [check open issue, #774 2020, Feb](https://github.com/tensorflow/probability/issues/774)
* benifit by the auto-grad from tensorflow

## lda: Topic modeling with latent Dirichlet allocation star 1k+

https://github.com/lda-project/lda

* python 2.7
* replace computational expensive part into C
* collapsed gibbs sampling

## bmabey / pyLDAvis 1.5k+ 

https://github.com/bmabey/pyLDAvis

* visulization tool for LDA(scikit-learn and gensim)

# Study

dongwookim-ml / python-topic-model stars 350+

LDA 還分成 training / inference

Training - gibbs sampling and expectation maximization

1. training (使用Gibbs sampling 對於一個計算步驟做抽樣估計)
2. optimizer : Expectation Maximization(minimize negative log likehood)
3. 看起來沒有supoort sparse matrix, 數量大的時候可能會壞掉，對原理略有了解之後，可以嘗試scikit-learn的，也是更新的實作(2010 的 paper)

inference - Variational Bayes

1. 另一套用於推論的算法，要另外寫

CollaborativeTopicModel

1. notebook 沒有使用，不曉得實作的能不能用

