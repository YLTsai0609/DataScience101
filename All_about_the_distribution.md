# All about the distribution
* Author : graykode/distribution-is-all-you-need
* Modified : YLTsai0609 / distribution, and applications
* spirit : Understanding first, mathematcs second.
<img src ='/images/distribution_1.png'></img>

2. Bernoulli distribtuion(discrete), [code](demo/bernoulli.py)
   * 成功是1, 失敗是0，成功機率為p
   * [Wiki](https://zh.wikipedia.org/wiki/%E4%BC%AF%E5%8A%AA%E5%88%A9%E5%88%86%E5%B8%83)
<img src ='/images/distribution_2.png'></img>
   * 白努力分佈不考慮先驗機率(prior probability $P(x)$)，如果我們最大化可能性(likelihood)，我們非常容易overfitting
   * 二元分類問題所使用的loss function : **ninary cross entropy**在數學上的形式即一個  $-logP_{bernoulli}(x)$


3. Binomial distribution(discrete), code
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

4. MultiBinomial distribution (discrete), [code](demo/categorical.py)
   * 白努力分佈的多重版本，這裡舉例有3個類別
   * TBD ... https://github.com/YLTsai0609/distribution-is-all-you-need