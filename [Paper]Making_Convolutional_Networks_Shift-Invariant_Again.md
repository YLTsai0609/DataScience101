# Infors
[Paper](https://arxiv.org/pdf/1904.11486.pdf)
citazion : 43
year : 2019

# Authors(Fly solo)

Richard Zhang 

# 摘要
現代的卷積神經網路不具有平移不便性，圖片小小的平移之後就能夠造成劇烈的變動，特別是在downsampling的方法中，像是max-pooling, strided convolution, averagepooling, 在不考慮抽樣的理論的情況下，解決方式是反鋸齒濾波(anti-aliasing by low-pass filtering filtering before downsampling)，但是直接將這樣的濾波器掛載神經網路上並沒有好的結果，我們展示了正確將它們組合的方法，我們的方法可以和已經存在的結構組合在一起，像是max-pooling以及strided-convolution，我們觀察到在ImageNet中，幾個常見的模型撞購都有更好的表現，像是ResNet, DenseNet, 以及mobileNet，我們認為這是一種regularization，並且，我們還觀察到模型產生了更好的泛化(generalization)，就算輸入的圖片有些殘缺，穩定性以及魯棒性還是很好，我們的結果站釋出這項古典訊號處理方法在現代的網路結構中仍然不該被忽視


# 導讀
[給CNN平移不變性，同時提升ImageNet成績，Adobe開源新方法｜ICML](https://kknews.cc/zh-tw/tech/klrvqjr.html)

# 註解

# Github
[Antialiasing cnns to improve stability and accuracy. In ICML 2019. star 1k+](https://github.com/adobe/antialiased-cnns)

# Sample code(Pytorch)