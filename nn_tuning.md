# 壹些務實的模型調整方法

* [你有哪些deep learning（rnn、cnn）调参的经验？ 贊同1k+](https://www.zhihu.com/question/41631631/answer/1129785528?fbclid=IwAR1m2xaWFpHVFgb_X6pelE-205IIl9A0dN53kiepS78H9*g60YXtpVqVVLGQ)
* 共18招
* 以下還有3個回答，都在1k+贊同

* [壹些常見的深度學習調參觀念](https://mp.weixin.qq.com/s/cD0IgS6BUq-DiOy2ltpYBg?fbclid=IwAR0UHqFDKrYQ2ROfu8h5_uNc8NLqfRahd32la6EllQ-QvZQwsYJKuWxqMrU)

## 關於Clone別人的code

0. 對於大多數任務，數據比模型重要，面對新任務的時候先充分分析數據，再根據數據設計模型，並決定參數，例如posenet的抖動產生的影響
1. 一開始不要用大的數據集，尤其是從別人的github clone的，可能在你的電腦上跑不起來，對code沒有信心之前不要做大規模實驗
2. 不要瞧不起條餐的論文/實驗報告，看論文時經常不看超參數設置的細節，在自己沒有太多資源實驗的情況下，實驗報告類的文章簡直是業界良心
3. 盡量不要自己搭架子(新手跟半新手)，找一個已經沒有明確bug能跑通其他任務的架子，在他的基礎上修改，否則debug過程非常艱難
4. 看論文的時候不要全信，能重現的話盡量重現一下，許多論文會把baseline做低，但實務上許多baseline其實還不錯

## 關於可重現性

1. 不管什麼模型，都先在一個小的訓練集上train, test，如果不能overfit，可能learning rate太大，或是code錯了

   1. 先調小learning rate
   2. 還不行，檢查code，看看dataloader資料格式對不對

2. train/val loss curve，正常的情況應該是train loss呈現log，逐漸下降趨於穩定，eval loss開始一直下降，到某一個epoch之後開始穩定或是開始上升，這時候用early stopping
3. 有些任務要注意gradient clipping，例如RNN系列
4. 要記錄每一次模型的動機，背景，參數，結果，以便復現，避免某一次引入了一個bug，發現時不知道怎麼評估影響範圍
5. 同一份code不應該因為hyperparameter改動一點點而有顯著差異，這表示資料太少或是基礎設置不當
6. 訓練時間很長時，要隨時可以將參數存擋，就跟打遊戲一樣
7. object detection可能遇到batch size沒辦法很大，因為網路參數太多了，這時候在框架允許的情況下，可以採用fp16來進行實驗

# Reference

[機器學習 2021 類神經網路訓練不起來怎麼辦 1~5](https://www.youtube.com/watch?v=QW6uINn7uGk)
* local minimum
* batch and momentum
* auto-learning rate
* loss functions
* natch normalization