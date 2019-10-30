# Key Concept
贝叶斯优化: 一种更好的超参数调优方式 | 知乎 重點節錄
* [講者 - tobe Vote : 758](https://zhuanlan.zhihu.com/p/29779000)

* 我們知道GridSearch是你給定的所有參數點(hyperparameter space)都跑一次，然後取最大的，這顯然有些參數不用搜尋
* Bayesian optimization就是利用先前所算過超參數以及model score，建立一個先驗機率分佈(prior)
  * 建立先驗機率分佈的方式採用的是高斯過程(Gaussian Process, GP)[1]
* 接著利用類似貝式定理的方式，找出下一個最有可能的超參數點，這裡必須要考慮兩件事
  * 考慮當前後驗機率分佈的mean，(預測機率最大的那個地方，表示者可能帶來最好的模型效果)
  * 考慮當前後驗機率分佈的variance，(預測機率分佈variance如果大，則表示不確定性很高，需要多採樣降低不確定性)
  * 綜合考慮這兩點的是Acquisition function(稱為獲取函數)，負責評估採樣質量，使用Expected Improvement(EI)來決定下個採樣點[2]
# Resource
1. 可以回想How_Bayesian_inference_works裡面對阿布體重先驗的分佈建立，現在把他自動化，會需要決定兩個值，一個是mean, 一個是variance, [知乎上有一則貼文可以看](https://zhuanlan.zhihu.com/p/24388992)
2. 可以從知乎的[這則貼文]((https://zhuanlan.zhihu.com/p/54030031))有個直覺式的了解
3. 論文的部分在[Bayesian op](https://github.com/fmfn/BayesianOptimization)最下面有提到
4. 實作，在標籤頁中的Hyperparameters
5. 對於超參數調整有一篇簡中的整理[Here](http://codewithzhangyi.com/2018/07/31/Auto%20Hyperparameter%20Tuning%20-%20Bayesian%20Optimization/)