# Tmp
## collections
[如何用简单易懂的例子解释隐马尔可夫模型](https://www.zhihu.com/question/20962240) 5.7k
[HMM和RNN是什么关系？功效上两者有冲突重叠？](https://www.zhihu.com/question/57396443)
[《白话深度学习与Tensorflow》学习笔记（3）HMM RNN LSTM](https://www.jianshu.com/p/a2755179be5b)
[從Baive Bayes -> HMM -> CRF](https://www.zhihu.com/question/53458773) 68
[機率圖模型 -> HMM -> MEMM -> CRF](https://www.zhihu.com/question/53458773) 180 順位2
[自然語言處理 -- Hidden Markov Model](http://cpmarkchang.logdown.com/posts/192352-natural-language-processing-hidden-markov-models) 

## Markov Model
以自然語言處理來舉例，語料庫中，各種字串的機率分佈，可以看成是一個
Random variavle的sequence, $X = (X_{1}, X_{2}, ..., X_{T})$, 其中，$X$的值是alphabet(字)的集合$S = \{s_{1}, s_{2}, ...s_{n} \}$

如果想要知道一個字串出現的機率，則可以把字串拆解成Bigram, 逐一用錢一個字，來推估下一個字出現的機率是多少

但是要先假設以下的 *Markov Assumoption*

> Limitted Horizon :
> > $P(X_{t+1} = s_{k}|)X_{1}, ...,X_{t} = P(X_{t+1} = s_{k}|X_{t})$

> Time Invariant : 
> >$P(X_{t+1} = s_{k}|X_{t} = P(X_{2} = s_{k}|X_{1})$

Limitted Horizon的意思是，每個$X_{t+1}$是什麼字($s_{i}$)的機率，只會受到上一個字$X_{t}$的影響
Time Invariant的意思是
每個$X_{t+1}是什麼字($s_{i}$)$的機率，和前一個字$X_{t}$的機率關係，不會因為在字串中的位置不同，而有所改變

> 註 : 事實上，這兩種假設是為了簡化計算，在真實的自然語言中，以上兩種假設都不成立

有以賞兩個假設之後，上一個字$s_{i}$必成這個字$s_{j}$的機率，就能夠建立*Tansition Matrix : A*，其中*A*的元素可以寫成:
$$
a_{i, j} = P(X_{t+1}= s_{j}|X_{t}=s_{i})
$$
也可以用*Transition Diagram*來表示 : 
<img src='./images/HMM_1.png'></img>
如果想要計算字串($s_1,s_2, ...,s_T$)在Model中出現的機率，可以從第一個字開始，用Transition Matrix逐字推算下去，假設第一個字(*Initial State*)的機率, $P(X_1 = s_1) = \pi_{s1}$，則Random sequence$(X_1, X_2, ..., X_T)$的機率為:
$$
P(X_1 = s_1, X_2 = s2, ... , X_T = s_T)\\\\
 = P(X_1 = s_1)P(X_2 = s_2)...P(X_T = s_T)
$$
即
$$
\pi_{s1}\Pi_{t=2}^{T}P(X_t = s_t|X_{t-1}=s_{t-1}) = \pi_{s1}\Pi_{t=2}^{T}a_{X_T, X_{T+1}}
$$

舉個例子，假設有個*Markov Model*, 
*alphabet*的集合$S=\{0, 1 \}$
*Initial State*的機率$\pi_{0} = 0.2, \pi_{1}=0.8$
*Transition Matrix為*

<img src='./images/HMM_2.png'></img>

用*Transition Diagram*表示成:

<img src='./images/HMM_3.png'></img>

則在此Model中，出現字串1011的機率為
$$P(X_1=1, X_2=0, X_3=1, X_4=1)\\\\
=\pi \times P(X_2=0|X_1=1) \times P(X_3=1|X_2=0) \times P(X_4=1|X_3=1)\\\\
=0.8 \times 0,6 \times 0.7 \times 0.4 \\\\
= 0.1344$$

## Hidden Markov Model
所謂的Hidden Markov Model, 就是從表面上看不到state是什麼，又多了一層推斷，例如狀態的表示是下雨以及晴天(Hidden state)，但能夠觀察到的狀態(observable state)是前一天晚上的氣象預報，由想要透過observable state去觀察hidden state
其中, observable為一個集合$O=\{o_1, o_2, ...o_n\}$
hidden state為一個集合:$Q = \{q_1, q_2, ...q_n\}$
