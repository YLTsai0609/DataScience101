# facenet

[DeepFace: Closing the gap to human-level performance in face verification 2014]()

[FaceNet: A Unified Embedding for Face Recognition and Clustering 2015]()

[人臉辨識(Face recognition) 解析與實作](https://medium.com/life-is-fantistic/%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-face-recognition-cffcec53a544)

# Concept
在人臉辨識(Face Recognition)的應用場景中經常需要在預測時，只靠一張照片就辨識一個人，然而深度學習的演算法在只有一筆訓練資料的情況下效果會很差，所以人臉辨識中必須解決**One Shot Learning**(單樣本學習)的問題

# Similarity Function
為了達到**One Shot Learning**這樣的目標，我們希望讓NN去學習一個函數d
$$
d(img_{1}, img_{2})
$$
輸出兩張照片的相異程度

* 同一個人 : 輸出一個較小的數字
* 不同人 : 輸出一個較大的數字，我們需要定義一個Hyperparameter $\tau$
* 以$\tau$為threshold，小於則為同個人，大於則為不同一人

在這樣的設計中就能夠解決 1 : 1 match problem，而1 : K match problem也能夠使用這種方法來解決

# (Siamese network)孿生網路
2014
pass

# Triplet Loss
2015 
<img src='/images/facenet_1.png'></img>

2015年的論文中提出了一個能夠有效學習的Loss function

* 三種照片 Anchor, Positive, Negtive
* Positive <--> Anchor 為同個人
* Negtive  <--> Anchor 為不同人
* 我們需要比較 Anchor 分別與 Positive 及 Negtive 一組的兩對照片進行訓練
* 我們希望 Anchor 與 Positve的距離比較近，與Negtive的距離比較遠

<img src='/images/facenet_2.png'></img>

* trivial solutions : 如果 $f$ 為 0 函數時，output什麼都是0，沒用
* 要避免上述的情況，我們引進一個Hyperparameter $\alpha$ 稱為margin，如此一來，兩隊照片的差距不只要小於等於0，還要比零在小一些
* 舉例來說 $\alpha = 0.2$時，$d(A,P) = 0.5$的話，則d$(A, N)$至少要0.7才會被視為不同人，$d(A, N)$如果只有0.6的話則不符豪，因為兩組的差距不夠大

code 
```
def triplet_loss(y_true, y_pred, alpha = 0.3):

anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
 
 # Step 1: 計算anchor和positive的編碼(距離)
 pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
 # Step 2: 計算anchor和negative的編碼(距離)
 neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
 # Step 3: 將先前計算出的距離相減並加上邊距alpha
 basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
 # Step 4: 將上述計算出的損失與零取最大值，再將所有樣本加總起來
 loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
 
 return loss

```
Loss function就會長成這樣

$$
L(A, P, N) = max(|f(A)-f(P)|^{2} - |f(A)-f(N)|^{2} + \alpha, ~ 0 )
$$

上述Loss function意義為，若兩對照片距離小於$- \alpha$，則接受，但是如果大於0，就接受0。

Cost function就是所有Training data的總和，可以用任何Gradient descent-like的方法來最小化

$$
J = \sum_{i=1}^n L(A^{(i)}, P^{(i)}, N^{(i)})
$$

例如有10000張訓練圖片，分別來自1000個不同的人(每個人約10張圖片)，這樣才能夠成我們的資料集，如果每個人都只有一張照片會無法挑出Anchor及Positive，但是NN訓練完成之後，就能夠將系統用在One-shot Learning的問題。

Dig deeply...
Choosing the triplets A, P, N
* 在上述目標中，如果只按照要求，隨機的選擇同一個人的照片A, P以及不同人的照片A, N，兩隊照片的差距實際上很容易差異大，這使用我們的NN無法有效地學習參數
* 因此，我們如果能夠讓$d(A,P) ~ d(A, N)$，那NN學習時就必須花更大的力氣分割開這兩者，也就是說我們的模型會學得更好，FaceNet: A Unified Embedding for Face Recognition and Clustering》(2015)這篇論文有更詳細的說明。

# Harmonic Embedding
pass
## Harmonic Triplet Loss
pass
semi-hard negtives

# Network Architecture
L2 normolization (batch?)



# Source Code 功能解析
[FaceNet源码解读：史上最全的FaceNet源码使用方法和讲解（一）（附预训练模型下载](https://blog.csdn.net/u013044310/article/details/79556099)

1. `campare.py` 直接比對兩個人臉經過神經網路映射後的L2距離
2. `align\align_dataset_mtcnn` 使用mtcnn模型對人臉資料進行preprocessing
切邊到只剩人臉，且降低pixel，通常會設定為160
3. `train_tripletloss.py` 重新訓練自己的網路模型
   * `train_softmax.py` 作者對論文所做出的延伸，除了使用facenet裡提到的`train_tripletloss.py`來訓練，還實現了softmax，**在樣本數很小的情況下，用softmax會更容易收斂**，但是當訓練集中人臉個數超過約莫10萬時，最後一層的softmax輸出數量會變得非常大，該時候使用`train_tripletloss.py`能夠有更好的效果
4. `validate_on_lfw.py`驗證率FAR, 曲線下面積 AUC 等誤差率 EER 等性能指標
5. `classifier.py` 從一個已經訓練好的facenet模型，在街上一個    SVM分類器，進而分類每個人。cudnn和tensorflow的相容性可能有問題，建議使用tf 1.7 version

## Minor file
1. `cluster.py` 使用mtcnn進行人臉檢測，對齊以及裁切，進行embedding，最後output使用L2距離進行聚類
2. `predict.py` 使用mtcnn進行人臉檢測，對齊以及裁切，進行embedding，進行人臉識別(需要訓練好的svm模型)
3. `export_embeddings.py` 輸出embedding array


## 實作須知
[Reference 1 metrics](https://medium.com/@weilihmen/%E4%BA%BA%E8%87%89%E8%BE%A8%E8%AD%98-%E5%9F%BA%E6%9C%AC%E6%B5%81%E7%A8%8B-%E6%B8%AC%E8%A9%A6%E6%A8%99%E6%BA%96-8d4d7c66e8ff)

[Reference 2 landmark](https://makerpro.cc/2019/08/face-alignment-through-5-facial-landmarks/)

[Reference 3 face alignment details](https://chtseng.wordpress.com/2018/08/18/face-landmark-alignment/)
[Reference 4 臉部辨識技術的挑戰 知乎](https://www.zhihu.com/question/39032661)
check 回答 
1. 830+ overview
2. 70+ 應用場景, 1:1, 1:N, N:N
3. 145+ 實際場景落地, 配合型與非配合型
4. 8+ 實際場景落地, 非配合型的難點
<img src='/images/facenet_3.png'></img>

### 場景

#### 配合型人臉識別

#### 非配合型人臉識別

### 資料集
#### 人種造成的影響

### Metric
分兩種，偵測指標，辨識指標
#### 偵測指標
<img src='/images/facenet_4.png'></img>

#### 辨識指標
Precision, recall

誤識率(FAR)
拒識率(FRR)
分數閥值T

### Face alignment(face nomorlization)

#### landmarks

#### alignment
2D alignment and 3D alignment

### 立體角(angular size)