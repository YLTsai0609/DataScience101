# Zero-Shot Object Detection
[《Zero-Shot Object Detection》笔记](https://zhuanlan.zhihu.com/p/47672456)
[Zero-Shot Object Detection](https://arxiv.org/pdf/1804.04340.pdf)
* year 2018
* citation 51
* Author
  * Ankan Bansal,  University of Maryland, College Park, MD
  * Karan Sikka, SRI International, Princeton, NJ
  * Gaurav Sharma, NEC Labs America, Cupertino, CA
  * Rama Chellappa, 
  * Ajay Divakaran 

# 摘要
作者們在本文中會介紹以及處理zero-shot object detection problem(ZSD)，ZSD指的是希望可以偵測到那些訓練網路時沒有被訓練到的data，並且，這次選用的資料及並非之前zero-shot classification的資料，使用了較為複雜的資料
本文中使用了先前被發表過的方法first adapting visual-semantic embeddings for ZSD，接著我們討論兩種在偵測場景中背景造成的影響，這激發了我們解決變動背景之下如何讓detector有更好的表現，其中一種模型僅使用了固定的背景，另一種的背景則會在幾種背景中變換(iterative latent assignment)，我們也列出了在訓練期間使用有限的類別數，但是預測時卻有非常多的類別時，所面臨到的挑戰為何，也提出了其中一個解決方案，稱作dense sampling，我們也提出了新的切分方式在MSCOCO以及VisualGenome上，以及展現了他們的實際成果，在傳統的Object dectection以及gemeralized zero-shot的比較，最後我們也提供了我們對次算法的insight以及總結目前所遇到的問題。

# 作者

