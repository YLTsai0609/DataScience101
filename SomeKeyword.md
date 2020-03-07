# Some Keyword

# Backbone
CNN Backbone往往是各種CNN模型的共享結構
而這些網路結構就是Object Detection, tracking, ...等等的用途，通常就是一個識別模型，但也有不適的時候，其實也可以說他是一個對raw iamge的**Feature Extractor**

[More about backbone](#more-about-backbone)

# Multi-Scale



pass


# More about Backbone

例如說，以下的backbone

```
AlexNet: https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
VGG: https://arxiv.org/pdf/1409.1556.pdf
GoogleNet: https://arxiv.org/pdf/1409.4842.pdf
Compact Bilinear: https://arxiv.org/pdf/1511.06062.pdf
Residual Network: https://arxiv.org/pdf/1512.03385.pdf
Inception: https://arxiv.org/pdf/1602.07261.pdf
Wide ResNet: https://arxiv.org/pdf/1605.07146.pdf
FractalNet: https://arxiv.org/pdf/1605.07648.pdf
DenseNet: https://arxiv.org/pdf/1608.06993.pdf
ResNeXt: https://arxiv.org/pdf/1611.05431.pdf
SORT: https://arxiv.org/pdf/1703.06993.pdf
```

這些共享結構除了調參之外(總深度，總寬度)以外，還反覆使用了多種技巧

```
Residual(残差): 直接elementwise加法。
Concat(特征拼接): 直接对特征深度作拼接。
Bottleneck(特征压缩): 通过Conv(1,1)对稀疏的或者臃肿的特征进行压缩
Grouping(分组): fc-softmax分类器从1个观察点把不同类靠空间球心角分离开，不同类放射状散开不符合高斯假设。分组改善了这一点。
Fractal(分形模式): 结构复用，可能带来好处
High-Order(高阶): 在非分组时，可能带来好处
Asymmetric(非对称): Conv(1,3),Conv(1,5),Conv(1,7)属于非对称结构，这个技巧在OCR处理长宽非1:1的字体有用
```

所以站在這個制高點，我們對於CNN結構有一個重新的審視

```
AlexNet/VGG: 普通
VGG: 加深
ResNet: 通过x+F(x)直接加法实现了Residual模块
Wide ResNet: 加宽
FractalNet: 结构复用，使用Concat
ResNeXt: ResNet基础上对Conv(3,3)使用了分组，但是如果Conv(1,1)也分组甚至精度不降
GoogleNet/Inception: 大量的非对称技巧
DenseNet: 大量使用压缩
SORT: 一个小trick使用elementwise x*F(x)实现高阶
Compact Bilinear: 通过学习矩阵A实现x’Ay实现制造新的特征

```