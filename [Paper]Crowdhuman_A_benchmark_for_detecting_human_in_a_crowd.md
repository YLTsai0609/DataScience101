# Infors

[here](https://arxiv.org/pdf/1805.00123.pdf)
citazion : 43
year : 2018

# Authors

S Shao, Z Zhao, B Li, T Xiao, G Yu, X Zhang, J Sun

# 摘要

人體檢測近些年來取得了非常大的進展。但是，高度擁擠的環境中人體檢測的遮擋問題還遠未解決。問題更大的是，目前的人體檢測基準測試中，擁擠的情況仍然沒有受到重視。本文中，我們給出了一個新的數據集，稱為CrowdHuman，可以更好的評估擁擠情況下的檢測器。 CrowdHuman數據集規模很大，標註豐富，變化多樣。訓練集和驗證集中總計有47萬個人體實例，每幅圖像中平均有22.6個人體，在數據集中有各種各樣的遮擋情況。每個人體實例都進行了三種標註，即頭部邊界框，人體可見區域邊界框和人體完整身體邊界框。目前最好的檢測框架在CrowdHuman上的檢測基准在文中相應給出。 CrowdHuman數據集的跨數據集泛化結果展示了在之前的數據集，包括Caltech-USA，CityPersons和Brainwash上的結果是目前最好的結果。我們希望我們的數據集會成為一個堅實的基準，幫助推進人體檢測任務的將來研究。

# 導讀

[【論文筆記】：CrowdHuman: A Benchmark for Detecting Human in a Crowd](https://www.twblogs.net/a/5d4e3650bd9eee5327fc72af?fbclid=IwAR2cGI4bInS5qmoewfHRrgKXxPZKCoemd3ftt_T_6hdy3PiJppOpRGo4rPk)

CrowdHuman的訓練集、驗證集和測試集分別包括15000，4370和5000幅圖像。圖片上的人體實例包含了三種標註，包括人體可見區域邊界框標註、頭部區域邊界框標註和人體整體邊界框標註。其設計是爲了解決人羣問題, 可以更好的評估擁擠情況下的檢測器。

第一，與現有的人體檢測基準測試比較，給出的數據集更大、人羣密度高的多。
第二，對每個人體實例都進行了整體人體邊界框、可見邊界框和頭部邊界框標註。這些豐富的標註使得很多潛在的視覺算法和應用成爲可能。
最後，作者提出的CrowdHuman數據集可以作爲一個有效的預訓練數據集。在行人檢測的基準測試中已經給出了最好結果，如Caltech和CityPersons，還有頭部檢測的基準如Brainwash。

# 註解
