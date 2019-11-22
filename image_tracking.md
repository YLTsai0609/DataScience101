# Image Tracking
## Naive approach
對於單點$(x,y)$來說，每個timestamp產生一個$(x,y)$，如此一來形成一個array，也可以說是函數$$C_{k}~~where~~k=1,2,3,...t$$
若
$$\frac{dc}{dt}<\epsilon$$
則為連續(即連續的定義)
Problem : 上述定義只能解決等速率時的情況，若單體具有加速度，就爆了，若每個出現在畫面中的單體，有不同的速率，同樣的爆了，因為不知道$\epsilon$怎麼定。

## kalman filtering
用於物件追蹤，雷達，軌道預測，kalman在196x年發表，用來解決火箭軌道預測的問題
核心思想主要加入了Bayesian inference，搭配物理學的運動公式，來推論下一個時間點可能的位置