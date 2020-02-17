# Transfer_learning
[李宏毅 ML 19 Transfer Learning](https://www.youtube.com/watch?v=qD6iD4TFsdQ&list=PLJV_el3uVTsPy9oCRY30oBPNLCo89yu49&index=28)

<img src='./images/tran_1.png'></img>

* 和現在要進行的task沒有直接相關的data
  * E.g. 手上有貓跟狗的data，有分辨cat, dog的model，但是你有另一組data是大象跟老虎，而你想要做一個classfier - input domain相似，但是task不同 **similar domain, different tasks**
  * E.g 手上有貓跟狗的data，有分辨cat, dog的model，但你有另一組data是高飛狗和招財貓，而你想要做一個classifer - input domain不同，但是task相同 **different domain, similar tasks**

* 我們能不能夠在現在有一些不相干data的情況下，來幫助我做現在的task?
  


舉幾個例子 : 
1. 語音辨識 - 台語，但是根本沒啥台語的data，你去youtube收集一堆中文跟英文的，transfer learning企圖用其他語言的辨識來improve 台語的語音辨識!
2. 影像辨識 - 醫學影像辨識，但是醫學影像很少，不過你可以在網路上爬到一大堆有的沒的的圖片!
3. 文件分析 - 法律文件分析，資料很少，但是有沒有其他網路文件有幫助??
4. 結構化資料 - 嫁接學習?
<img src='./images/tran_2.png'></img>

## Transfer Learning有可能嗎?
* 其實是合理的，例如你不知道研究生要怎樣過生活，你就搜尋漫畫家，他的主角就是研究生
* 或是你不知道怎麼打排球，你就搜尋排球少年，排球少年教你怎麼打排球

<img src='./images/tran_3.png'></img>

## Transfer Learning - Overview
* 有很多的方法，事實上Transfer Learning是很多很多方法的集合
* 有些名詞有人說是有人說不是，李教授覺得概念是，其實就是，所以整理再一起

<img src='./images/tran_4.png'></img>

* 暫且分成兩個部分，Target data以及Source Data

* Target Data指的是真正想要進行的任務
* Source Data則是我們手上現在有的，不那麼相關的Data
  * 注意，怎麼定義跟當前任務沒有直接的關係，這是一個比較模糊的地帶，目前有多個門派的說法
  * A門派 : 真實物體的image以及動畫版本的images，沒有直接關係
* 接著兩種Data簡單區分一下為有label以及沒有label，接著就產生4種可能

### labelled, labelled

<img src='./images/tran_5.png'></img>

<img src='./images/tran_6.png'></img>
 
#### Model Fine-tuning
看下圖，通常Target data非常少，而Source data有一大把，就像知乎中的嫁接學習

* 然而如果Target data非常之少，則稱之為One-shot Learning(一種特化出來，特別針對imblance ratio超大的情況所做的調整)
* 舉例 : 特定人員的語音辨識的特定語句辨識，Target data少，Source data多(其他不同人的背景)
* 直接用source data training，然後在target data上tuning model(like adversirial validation)，其實就想成source data traning出來的是initial value，然後在target data在train一發，然後就結束了，但是要很小心Overfitting，或許regularization要強一點，接下來就是介紹一下怎麼做到這件事
  
#### Conservative Training

<img src='./images/tran_7.png'></img>
* Regularization的方式可以選擇像是
  * output 的prediction在同樣的sample data不要差太多
  * model中的weight的L2 distance不要差太多
  * 或是其他你想得到的方法

#### Layer Transfer
<img src='./images/tran_8.png'></img>
* 同樣架一個新的Model，把某幾個layer直接copy到新的model裡面
* Target data只training新的layer
* 例如只有一層新的layer拿來train target data，如此一來只要考慮很少的參數，避免Overfitting
* Data夠多時，可以直接fine tune整個model
* `Layer Transfer`其實是個非常非常常見的小技巧
* 但是，哪些Layer應該要被transfer? - 不同任務有不同特性
<img src='./images/tran_9.png'></img>

* Speech : Copy最後幾層，重新train inputs 那層
  * why ? heuristic : 每個人講話，用同樣的發音方式，但是因為口腔結構，或是習慣不同，得到不同的頻譜，而NN是從聲音訊號來得知語者的發音方式，顯然input layer會和發音方式有關係
* Image : 通常Copy前面幾層，只train最後幾層
  * 如果把layer的weight畫出來，會發現說，前面幾層通常是學到一些直線橫線，簡單幾何圖形，越往後走越偏向高階特徵

<img src='./images/tran_10.png'></img>

* 所以就有人來做實驗了，NIPS, 2014 How transferable are features in deep neural networks? - citation : 3630
* ImageNet 有1000個class，其中500個當作Source，另外500個當作Target
* x軸是transfer learning時copy幾個layer，copy 0個layer就是沒有做tansfer learning，直接train，作為baseline，縱軸是Top1 accuracy
* n = 1，copy第一個layer，後面的layer全部re-train，...
* 如果copy太多layer，結果是會變差的，如果只copy了前面兩三個，結果是換變好的，各種顏色還要從原始論文了解一下定義
* 而這張圖解釋了，不同task上的Model，前面幾個layer是可以共用的，後面則不行
* 橙色線表示換過layer，而且做parameter optimization
* 但是需要注意，這個task的target data非常多
* 藍色線，是這篇論文的另一個發現，主要是想表示說，layer之間是要互相搭配的，沒辦法只train部分，這樣後面的layer和前面的layer無法互相搭配

TBD : 23:54

## Reference
[How transferable are features in deep neural
networks? NIPS 2014 citation 3630次](http://papers.nips.cc/paper/5347-how-transferable-are-features-in-deep-neural-networks.pdf)