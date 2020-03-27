# Infors
citazion : 1
year : 2020, Feb
CVPR
[文](https://arxiv.org/abs/2002.10857?fbclid=IwAR3TQIQZk22FAkL7uSfx4ZEkQOq-mbQXgcXwE6r32HkTxRAUyUQZ9TOGlqo)

# Authors
Yifan Sun, Changmao Cheng, Yuhan Zhang, Chi Zhang, Liang Zheng, Zhongdao Wang, Yichen Wei

# 摘要
這篇文章在深度特徵學習上提供了一個成對相似度優化(pair simlarity optimization)的角度，針對組內相似度最大化$s_p$(within-class similarity)以及組間相似度最小化$s_n$(between-class similarity)，從這個觀點來看，我們發現大多數的loss function，包含了triplet loss 以及 softmax + cross-entropy loss都將$s_n$以及$s_p$嵌入到相似對中(similarity pair)並希望降低$s_n - s_p$
這樣的優化方法是死板的，因為對於每個相似度分數，懲罰強度都是相同的，我們的直覺則是，如果有一個相似度分數距離最佳值非常遠，該pair應該要被強化，在這樣思考下，我們針對每個相似對進行了權重上的重新配置，導出了Circle loss，會這樣命名是因為他有一個circular decision boundary，Circle loss對於上述題種的兩種優化方式有一個統一的公式，也就是在class level學習以及 pairwise labels，解析上來說，我們展示了Circle loss提供了一個更有彈性的最佳化方式讓收斂更加明確，並且在實驗上，我們展示出Circle loss在多個深度學習任務上都有優越的·表現，在人臉辨識，person re-identification，以及其他細顆粒的圖片資料及上，都達到了最新性能

# 導讀
[旷视研究院提出Circle Loss，革新深度特征学习范式 知乎50+](https://zhuanlan.zhihu.com/p/117716663)

* triplet loss 讓recognition task能夠有更好的表現，並在100k+的辨識任務上有著驚人的表現，然而在100k+以下的任務則是softmax會有更好的表現，這意味著兩個優化方法有各自的優勢，本篇文章Circle Loss就是把兩者統合了起來，並提出一個新的loss，在思想上有值得學習的地方

深度特征学习有两种基本范式，分别是使用类标签和使用正负样本对标签进行学习。使用类标签时，一般需要用分类损失函数（比如 softmax + cross entropy）优化样本和权重向量之间的相似度；使用样本对标签时，通常用度量损失函数（比如 triplet 损失）来优化样本之间的相似度。

这两种学习方法之间并无本质区别，其目标都是最大化类内相似度（s_p）和最小化类间相似度（s_n）。从这个角度看，很多常用的损失函数（如 triplet 损失、softmax 损失及其变体）有着相似的优化模式：

它们会将 s_n 和 s_p 组合成相似度对 (similarity pair)来优化，并试图减小（s_n-s_p）。在（s_n - s_p）中，增大 s_p 等效于降低 s_n。这种对称式的优化方法容易出现以下两个问题

# 註解
