# Proving the Lottery Ticket Hypothesis : Pruning is all you need
citazion : 25+
2019

# Authors

Rafael Müller

Simon Kornblith

Geoffrey E. Hinton

# 摘要
多目標網路模型的模型泛化，可以從使用`sort target`來得到明顯的準確度提升，labels smoothing是一種能夠避免網路overfitting的方法，而這樣的方法可以用在所有目前效能最好的網路上，像是圖片辨識，機器翻譯以及語音辨識，儘管它的用途很廣泛，但目前我們對這個方法的了解還不夠多，這裡我們秀出實際上他能改善的地方，label smoothing可以使模型在beam-search時獲得顯著提升，然而，五們發現如果有一個teacher network使用了label smoothing進行訓練，student model的知識蒸餾效果反而會變差，為了解釋這個現象，我們將label smoothing改變倒數第2層網路的現象視覺化，現象顯示，label smoothing使得同一類的訓練資料傾向於更緊密的聚合，這導致了不同類的資料相似性訊息丟失，但對模型的預測以及泛化程度影響不大

# 導讀
[Hinton等人最新研究：大幅提升模型准确率，标签平滑技术到底怎么用?](https://zhuanlan.zhihu.com/p/72685158?fbclid=IwAR1TtHlW_O3G5QjtUEZ8TlkCXE7NINTjM7v4RVU2l-NcWmvxQEvJUCl8CI0)



# 註解
