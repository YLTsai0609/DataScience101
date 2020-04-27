# Infors
[Paper](https://arxiv.org/pdf/1904.11486.pdf)
citazion : 43
year : 2019

# Authors(Fly solo)

Richard Zhang 

# 摘要
Modern convolutional networks are not shiftinvariant, as small input shifts or translations
can cause drastic changes in the output. Commonly used downsampling methods, such as
max-pooling, strided-convolution, and averagepooling, ignore the sampling theorem. The wellknown signal processing fix is anti-aliasing by
low-pass filtering before downsampling. However, simply inserting this module into deep networks degrades performance; as a result, it is
seldomly used today. We show that when integrated correctly, it is compatible with existing architectural components, such as max-pooling and
strided-convolution. We observe increased accuracy in ImageNet classification, across several
commonly-used architectures, such as ResNet,
DenseNet, and MobileNet, indicating effective
regularization. Furthermore, we observe better
generalization, in terms of stability and robustness to input corruptions. Our results demonstrate
that this classical signal processing technique has
been undeservingly overlooked in modern deep
networks
# 導讀
[給CNN平移不變性，同時提升ImageNet成績，Adobe開源新方法｜ICML](https://kknews.cc/zh-tw/tech/klrvqjr.html)

# 註解

# Github
[Antialiasing cnns to improve stability and accuracy. In ICML 2019. star 1k+](https://github.com/adobe/antialiased-cnns)
