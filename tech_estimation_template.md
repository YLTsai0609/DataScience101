# 常見考量

幾個常見考量點如下

1. 開發成本(時間 and 人)
2. 易用性(是否好維護，是否好建置，硬體相容度好不好)
3. 協作性(團隊使用這個技術是否容易協作，要補充什麼技術)

評估時的疑難雜症如下

1. 開發成本不太知道怎麼估 -> 自己用用看，考量團隊技術水平，考量社群大小
2. 若開發成本無法量化到幾個月/幾週，可以先估計尺度，是週，雙週，月，季的等級來完成
3. 不要說一定可以，要說有很大的機會可以做
4. 套件成熟度(看是否是大版號，怎麼問問題，slack / github issue的開發者回答問題的程度)

## 需求

大規模的物件辨識模型服務，例如廠商A需要20個client可以傳送照片給AI Server，並取得辨識結果

過往做法 : socket server / TCP連線 / 自訂封包格式

須滿足項目(多對多架構，可分散到不同機器或單台機器)

1. 單機上可以跑多模型，並接收多個client
2. (Optional)可分散式到多台機器

keyword : distributed development

### 需求細節化

一開始的需求可能是一個方向，對真正要做的事不會很明確，隨著時間的推移，所需要的東西會越來越明確，就可以寫在這裡

1. client丟出request之後就回應(blocking mode)同步式通訊協定

# 候選套件/框架

| 套件名稱 | 星星數 | 開發成本粗估 |社群大小| 優點 | 缺點 |
|--------|-------|------------|-------|-----|-----|
| celery  | 16.4k |       |     |     ||
| pyzmq  | 2.7k |       |     |     ||

Celery : Distributed Task Queue

[celery 架構](https://www.itread01.com/content/1550392027.html) - 無提供reponse回傳

ZeroMQ for python - pyzmq

ZeroMQ : distrbiuted, sync/async, cross machine/process/thread, flexiable, 
