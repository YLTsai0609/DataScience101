# 名詞們

| command  | what is it                 | note             |
|----------|----------------------------|------------------|
| `gsutil` | `google storage utils` | 用於管理gcs資源，例如建立bucket，列出bucket等    |
| `gcould` | `google could shell tools` | 用於操作gcp專案資源 |

[Google Cloud Shell 入門：gcloud & gsutil](https://titangene.github.io/article/getting-started-with-cloud-shell-gcloud-and-gsutil.html)

<<<<<<< HEAD
# gcould

## login
可以透過gcloud auth login 進行帳號登入，接著就可以設定project

## set project

```
(base) joetsai@thor:~$ gcloud config set project pixnet-gt
Updated property [core/project].
```
=======
# 常用指令

| command example | usage  | note |
|----------------|---------|------|
| gsutil ls -l   | list resource/files on google storage |     gcs     |
| gsutil cp local_file gs://yurenke-test/abc.json| upload resource to google cloud storage| gcs |
| gsutil mv gs://yurenke-test/abc.json gs://bcd/aaa.json |move bucket from a to b|gcs
| gsutil rm/rb gs://yurenke-test/abc.json  |remove thr bucket|gcs
| gsutil version  |show the version info about gsutil|gcs

# Google Cloud on Air 3/17

## GCP Introduction

<img src='./images/gcpair_13.png'></img>

<img src='./images/gcpair_14.png'></img>

<img src='./images/gcpair_15.png'></img>

app engine可以做到 auto-scaling

通常整理好準備分析的資料會放到bigquery

pubsub則是溝通工具，可以放到data lake

### gcs

上傳檔案不用錢，下載才要錢，可視為無限大的檔案空間

但實質上是key-value pair，所以其實你要rename folder，會比較麻煩

### network

google自己建置海底電纜，google有自家的網路，所以google自己的服務之間溝通速度會快很多

On-Premise - 地端機器

## Realtime BI Dashboard

有分成 batch 跟 streamming

<img src='./images/gcpair_1.png'></img>

其實上圖中最棘手的是左邊

多樣性(資料格式的不同，怎麼做整理和統一)，並且是大家比較不會注意到的

三張圖會對應到google的三個服務

## Pub/Sub(Reliable Realtime messaging)

event-based : message queue，有事件就上傳

<img src='./images/gcpair_2.png'></img>

<img src='./images/gcpair_3.png'></img>

1. 該服務會保證對方一定收的到(像是手機訊息進火車山洞)，對方還是收的到
2. Server服務 - 不用自己寫
3. 後面可以接收集資料的地方(資料湖)
4. message queue(可作為broker)，發送者不需要知道訂閱者
5. 對應open source工具 - Kafka, RabbitMQ(Sacaling服務時會用到)

<img src='./images/gcpair_4.png'></img>

## Cloud dataflow

### Pipeline

<img src='./images/gcpair_5.png'></img>

Apache Beam - 可以同時support batch/streamming

<img src='./images/gcpair_6.png'></img>

有各種template，只需實作商業邏輯即可

<img src='./images/gcpair_7.png'></img>

<img src='./images/gcpair_8.png'></img>

Apache Beam 只是一張設計圖，可以經由Spark，或是google dataflow的運算引擎來運算

<img src='./images/gcpair_9.png'></img>

以上是具體程式碼

同時支援batch / streamming?

<img src='./images/gcpair_10.png'></img>

1. 換Input / output
2. streamming要有一個window，來做groupby，其他幾乎一樣

<img src='./images/gcpair_11.png'></img>

Auto Scaling!
Monitorable!

### Runner

Dataflow - spark on gcp
<img src='./images/gcpair_12.png'></img>

## Visulization

Data Studio
>>>>>>> bdbbddab8c9524ed643fd6e881555a149cc7e9f7
