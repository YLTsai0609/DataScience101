# facenet
* matirial
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
