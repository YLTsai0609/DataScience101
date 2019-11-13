# All about the distribution
* Author : graykode/distribution-is-all-you-need
* Modified : YLTsai0609 / distribution, and applications
* spirit : Understanding first, mathematcs second.
<img src ='/images/distribution_1.png'></img>
* `conjugate`意思為共軛分佈
[TODO] https://read01.com/7K2am8.html#.Xcw5gpIzZE4

2. Bernoulli distribtuion(discrete), [code](demo/bernoulli.py)
   * 成功是1, 失敗是0，成功機率為p
   * [Wiki](https://zh.wikipedia.org/wiki/%E4%BC%AF%E5%8A%AA%E5%88%A9%E5%88%86%E5%B8%83)
<img src ='/images/distribution_2.png'></img>
   * 白努力分佈不考慮先驗機率(prior probability $P(x)$)，如果我們最大化可能性(likelihood)，我們非常容易overfitting
   * 二元分類問題所使用的loss function : **ninary cross entropy**在數學上的形式即一個  $-logP_{bernoulli}(x)$

<br>
3. Binomial distribution(discrete), [code](/demo/binomial.py)
   * n個**獨立**的是/非試驗中成功次數的離散機率分佈
   * 就是多次的Bernoulli試驗，有成功機率$p$，有試驗數$n$，因此就有mean, variance, 形成一個distribution
<img src ='/images/distribution_3.png'></img>
   * 隨機變數$X$服從參數為$n$和$p$的Binomial distribution，計為$X~～~b(n,p)$或$X~～~B(n,p)$
   * [wiki](https://zh.wikipedia.org/wiki/%E4%BA%8C%E9%A0%85%E5%88%86%E4%BD%88)
   * 想要知道正好得到$k$次成功的機率，$k=n$, $k=0$，在n足夠大的情況下(例如>10)，基本上很難出現，機率很小，其機率計為
    $$
 Pr(X=k) = \dbinom{n}{k} p^{k}(1-p)^{n-k}
$$
   * 參數: $n, p, k$
   * Binomial distribution is distribution considered prior probaility by specifying the number to be picked in advance.
   * 舉例 : 
     * 特定醫院特定一天中 : 出生的小孩有多少是女的
     * 特定教室，多少學生是綠色眼睛
     * 骰子共六面，摋出5,6算是成功，摋100次，成功73次的機率是多少
     * 在一個城市做市場調查，連續遇到7喜歡喝珍珠奶茶的人的機率
   * 應用場景 : 

1. Multi-Bernoulli distribution (discrete), [code](demo/categorical.py)
   * a.k.a categorical distribution
   * 白努力分佈的多重版本，這裡舉例有3個類別
   * 一個隨機變數$X$，有0.7的機率指向到A事件，0.2的機率指向到B事件，0.1的機率指向到C事件
<img src ='/images/distribution_4.png'></img>

5. Multinomial distribution(discrete) [code](/demo/graph/multinomial.png)
   * 關係和Bernoulli <--> Bonominal 一樣, a.k.a 多項分佈
   * 熱力學有用到，可以找一下公式
   * n個**獨立**的A/B/C試驗中成功次數的離散機率分佈
   * 一個骰子問題可以是4以上叫做成功，以下叫做失敗，則就會形成只有成功或失敗的形式，這個時候就是白努力試驗與二項分佈，當點數1~6的出現次數分別為(6,0,0,0,0,0)時的機率是多少，就是再說明一個多項分佈
   * 從隨機變數$X$將會擴張成隨機向量$X=(X_{1},...,X_{6})$
   * 可以得知一定是0~N項，而且每個事件發生的個數總和一定會是全部事件
     * $X_{i}~>0, X_{1}+X_{2}+...+X_{n}=N$
   * (6,0,0,0,0,0)的出現機率 : 
   $$
P(X_{1}=6, X_{2}=0,~...,X_{6}=0) = \frac{N!}{6!0!0!...0!} (p_{1})^{6}(p_{2})^{0}, ...(p_{6})^{0}
$$

   * 此例中，取了一個可能性相當低的事件，且$p_{i}$皆為$\frac{1}{6}$
   * General form
$$
P(X_{1}=m_{1}, X_{2}=m_{2},~...,X_{6}=m_{6}) = \frac{N!}{m_{1}!m_{2}!m_{3}!...m_{6}!} (p_{1})^{m_{1}}(p_{2})^{m_{2}}, ...(p_{6})^{m_{6}}
$$
Collect into  $\Pi$ : $$
P(X_{1}=m_{1}, X_{2}=m_{2},~...,X_{6}=m_{6}) = \frac{N!}{\Pi_{i=1}^{N}m_{i}}\Pi_{i}^{N}(p_{i})^{m_{i}}
$$
   * 上述中我們稱隨機向量$X$服從多項分佈$X~～~PN(N, p_{1}, p_{2},...p_{k}) $
   * 其中$X_{i}$
     * 期望值$E(X_{i}) = np_{i}$
     * 變異數$V(X_{i} = np_{i}(1-p_{i})$
     * 共變數 $Cov(x_{i}, x_{j}) = -np_{i}p_{j}$
<img src ='/images/distribution_5.png'></img> 
trial : 試驗總數, 即 n_experments
   * 可以透過組合個數，各category的出現機率，在合理的假設之下，推論接下來某個組合的出現機率，參考Reference
   * 舉例 : 
     * 一個骰子共六面，摋100次，出現$(X_{1} = 100, X_{2}=0,...X_{6}=0)$的機率是多少
     * 在城市中做市場調查，以年輕人為例，假設年輕人喜歡5種飲料店且沒有例外，遇到組合為A,A,A,B,D組合的機率是多少(注意假設) 
****
* [Multi-nomial distribution-1](https://baike.baidu.com/item/%E5%A4%9A%E9%A1%B9%E5%88%86%E5%B8%83)
* [Multi-nomial distribution-2](http://www.math.ncu.edu.tw/~yu/ps99/boards/lec41_ps_99.pdf)
* [Multi-nomial distribution-3](http://eschool.kuas.edu.tw/tsungo/Publish/05%20Discrete%20probability%20distribution.pdf)