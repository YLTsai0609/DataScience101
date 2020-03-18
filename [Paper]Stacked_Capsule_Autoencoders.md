# Infors
citazion : 11
year : 2019

# Authors
Adam R. Kosiorek
Sara Sabour
Yee Whye Teh
Geoffrey E. Hinton
# 摘要

# 導讀
[AAAI Conference 知乎導讀](https://zhuanlan.zhihu.com/p/106305139?fbclid=IwAR2HvU3dZKbETUazn4vRfYOLEiOJD2hqkGz4QgSWyx6Z405rU5NM9sU20tA)

物件偵測上主要基於兩種方法:
* 傳統手工特徵，例如HOG, LP等等，通常涉及很多手動操作，這樣深層次的結構很難被發現
* CNN，使用end to end learning，透過所有圖像使用相同的知識，這種方法獲得巨大的成功，但是他們在很多方面與人類感知不同

CNN存在的問題:
* CNN雖然對於區域特徵的描述能力很好，但是他們對以下的情況實質上處理得非常差
  * 視角轉換    
  * 旋轉
  * 剪切(放大伸縮)
  * 光照
  * 對抗性

膠囊網路，通過可查看所有部件的autoencoder，進而推斷物體膠囊的位置與姿勢

# 註解
