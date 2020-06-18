# Questions
* 有沒有一種資料增強方法，是把該物件去背剪下，然後random抽換背景?
* 有了這樣的方法，就能夠大幅加強物件在不同背景下被偵測出來的Precision，不會因為背景不同就找不到東西

* google
  * data augmentation randomly substitute object
  * data augmentation with different background

* connected papers
  * A survey on Image Data Augmentation for Deep Learning 

# Survey
* 關注在該論文解決了什麼問題? 與我們的問題是否相關?

* [A survey on Image Data Augmentation for Deep Learning 2019 161+](https://link.springer.com/article/10.1186/s40537-019-0197-0)
  * 近期的資料增強方法大補帖，YOLO v4有做的資料增強幾乎都涵蓋到了，但沒有我想要的

* [Data Augmentation using Random Image Cropping
and Patching for Deep CNNs 2019 22+](https://arxiv.org/pdf/1811.09030.pdf)

  * YOLOv4裡面有做到這種資料增強，基本概念是random擷取部分物件，拼接成新的照片，並用soft label來作為新的標記，這種做法的優點是讓圖片對於遮擋能夠更rostbuness
  * 圖1(隨機拼接)
  * 圖2(random bbox)
  * 圖3 (對於遮擋的robustness)

* [ViBe: A universal background subtraction algorithm
for video sequences 2010 1746+](https://orbi.uliege.be/bitstream/2268/145853/1/Barnich2011ViBe.pdf)
  * 一種去背方法，2010年提出，主要是用在影片裡面，影片的連續畫面中能夠透過frame by frame的pixel比對來認出背景，並比較了Bayesian histogram, Codebook, EGMM, GMM等去背方法，Vibe本身算是表現不錯的方法

* [Data-augmentation for reducing dataset bias in person re-identification 2015, 64](https://sci-hub.tw/10.1109/avss.2015.7301739)
  * 這篇文章是做行人重識別，在這個領域非常需要針對同個人在不同場景下能能夠有足夠的相似度，採取的資料增強方法就是我要的，去背然後換到不同背景上，**論文的方法中有略為提到他的做法，值得在細讀一次**
  * 同樣的，有圖(剪下人)貼上背景

* [Perspective Transformation Data Augmentation for Object Detection 2019, 0+](https://ieeexplore.ieee.org/document/8943416)
  * 主要是轉換viewpoint的資料增強方法，基本上用Afiine transform，並不是什麼新技巧，一種水論文的感覺?
  * 基本上機過兩個步驟，affine transform，然後annotation alignment
  * viewpoint可以涵括到相機拍不到的地方，但是也不是全部都可以，要細看一下，如果有viewpoint上的需要，可以看，在空拍機上的資料增強會很有用

* [Style Augmentation: Data Augmentation via Style
Randomization 2018, 13](https://arxiv.org/pdf/1809.05375.pdf)
    * 透過GAN做style上的資料增強，內文也有圖，但比較不是現實世界中會出現的場景，可能在漫畫/卡通上有用?