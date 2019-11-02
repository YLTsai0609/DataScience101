# bash
> 紀錄工作中常用到的一些bash指令，以及使用場景
> 查看當前bash版本 `help`

# NetWork
|命令|使用場景|備註|
|---|-------|---|
|`ifconfig`|查自己的這台的ip||
|`ipython` `import socket` `socket.gethostbyname('deviceName')`|從A主機經由同網域的連線查詢B主機的ip|ipython要pytho3.5以上才支援|
|`ping` ip adress|從A主機經由同網域的連線查詢B主機目前的連接狀況及速度(time out, or speed xx/ms)|ping = 戳，測自己網速可以搭配內部迴圈網路 127.0.0.1|
|`scp userName@ip adress:filePath MyfilePath`|已知主機filePath，從主機抓檔案/資料夾到本地端||
|`scp MyfilePath userName@ip adress:filePath`|把本地端的檔案copy到主機端的目錄|
|`ssh userName@ip adress`|經由ssh連線到主機端，但主機端需要是一個ssh server，或是有給予ssh金鑰|

* [鳥哥一下 : [第11章、遠端連線伺服器 SSH/XDMCP/VNC/RDP]](http://linux.vbird.org/linux_server/0310telnetssh.php#scp)


## 觀念
### 關於固定IP與浮動IP
真實IP, 實體IP, 虛IP, 假的IP, 其實沒有分沒有那麼多種，在IPv4裡面，只有兩種IP類別，其他你聽到的基本上是IP的取得方式
<br>
  * Public IP : 公共IP，經由INTERNIC所統一規劃的IP，有這種IP才能上Internet
  * Private IP : 私有IP或是保留IP，不能直接連上Internet的IP，主要用於區域網路內的主機連線規劃

IPv4規劃時就擔心IP會不足，而且為了應付某些企業內部的網路設定，於是有了私有IP的產生，私有IP也分別在A, B, C三個Class中個保留一段作為私有IP網段

  * Class A : 10.0.0.0 - 10.255.255.255
  * Class B : 172.16.0.0 - 172.31.255.255
  * Class C : 192.168.0.0 - 192.168.255.255

### 還有一個特殊網段 loopback IP

  * 127.0.0.1 : 內部迴圈網路 當你要測試你的TCP/IP封包與狀態是否正常時，就可以使用
* 所謂ip取得方式 

### 所以主機的IP是如何設定的?

  * 直接手動設定(static) 所謂的固定ip : 你可以直接向你的網管詢問可用的ip相關參數，然後直接編輯設定檔(或使用某些軟體功能來設定你的網路)。常見於校園網路環境、或是自架封閉區網、或是像ISP申請固定ip的連線環境
  
  * 撥接取得 : 向你的ISP註冊，取得帳號密碼後，直接撥接到ISP，你的ISP或透過他自己的設定，讓你的作業系統取得正確的網路參數。此時你**不用手動編輯與設定相關的網路參數**。目前台灣的ADSL，光纖到大樓、光纖到府，大部分都是使用撥接方式。為了因應客戶需求，某些ISP也提供很多不同的IP分配機制。包含hinet, seednet等都有提供ADSL撥接後取得固定ip的方式，詳情可以向自己的ISP洽詢XD。

  * 自動取得網路參數(DHCP - Dynamic Host Configguration Protocol) 所謂浮動ip : 在區域網路內會有一部主機負責管理所有電腦的網路參數，**你的網路啟動時，就會主動向伺服器要求IP參數**，若取得網路相關參數後，你的儲機就能夠自行設定好所有伺服器給你的網路參數。最常使用於企業內部、IP分享器後端、校園網路與宿舍環境、纜線寬頻等連線方式。

* [鳥哥一下 - 第二章、網路基礎概念 2.3.3 IP的種類與取得方式](http://linux.vbird.org/linux_server/0110network_basic.php#tcpip_network_type)

* [terminal 設定固定ip](https://blog.toright.com/posts/6293/ubuntu-18-04-%E9%80%8F%E9%81%8E-netplan-%E8%A8%AD%E5%AE%9A%E7%B6%B2%E8%B7%AF%E5%8D%A1-ip.html)

<br>

### 總結 : 

  > 只有公共IP和私有IP，固定IP及浮動IP指的是取得方式，手一揮，假的

# Permission

|命令|使用場景|備註|
|---|-------|---|
|`chmod`|更改檔案權限|需要惡補一下檔案權限的部分|

# Backup, packing, unpacking

|命令|使用場景|備註|
|---|-------|---|
|`dd`|備份磁碟、樹莓派microSD|可以調整寫入速度|
|`gzip`|壓縮、解壓縮||
|`zip` `unzip`|壓縮、解壓縮||
|`tar`|打包、解包| 打包/解包 實際上並沒有壓縮，檔名是.tar 即打包解包, 檔名是tar.gz 表示有壓縮|
|`tar xvf filePath -C dirpath`|解包, 解壓縮(加z)||


# Shell script
## 動機
編寫一個bash script
使用場景 : 其實跟python script一樣，當你的bash指令太長，或是一次要執行3個指令，就直接開一個 fileName.sh
例如 : 要定時備份、要定時check model performance然後retrain、每天的半夜retrain等等
效益 : 部署時常常使用的機器你也不知道哪哪個型號，但是是Unix like，基本上bash和vi這時候就會是你的武器，畢竟，你也不知道上面到底有沒有裝python
## 再多一點概念
基本上就是早期DOS年代的批次檔(.bat)，基本上就是把一堆指令堆在一起，
而且其實 shell script也提供陣列、迴圈、條件、邏輯判斷等，很多場景下寫起來會更快解決問題，同樣的，也不用編譯

vi example.sh
```
#!/bin/bash
echo "Start"

# 平行處理多個工作
sleep 3 && echo "Job 1 is done" &
sleep 2 && echo "Job 2 is done" &
sleep 1 && echo "Job 3 is done" &

# 等待所有工作完成
wait

echo "Done"
```

[鳥哥一下 - 第12章、學習 Shell Scripts](http://linux.vbird.org/linux_basic/0340bashshell-scripts.php#script_why)

# 環境變數/路徑 PATH

# pipe

# Job Control 工作控制

|命令|使用場景|備註|
|---|-------|---|
|`nohup`|放到主機算，然後自己登出，搭配 `ctrl + z`, `bg` |nohup = no hang up|
|`bg`|把執行緒丟到後台，搭配nohup||
|`fg`|把執行緒拉回前台，佔住自己的terminal XD||
|`kill`|根據Job ID 把程式殺掉||
|`wait`|等待某Job跑完，或是並行處理完||

# profiling 看一下
|命令|使用場景|備註|
|---|-------|---|
|cat|檔案不大，覺得vi很難操作，複製程式碼時|cat會看整個檔案|
|less|一頁一頁看，而且可以往前翻頁|忘記less怎麼用的時候，less file 然後 h，基本操作 f - forward, b - backword, 可以設定一次看幾行|
|head|看個前幾行，意思一下，跟dataframe.head()一樣||
|tail|看個後面幾行，意思一下，跟dataframe.head()一樣||
|echo|叫一段文字、或是叫一個檔案、叫環境變數|怎麼叫環境變數? echo $PATH|
|tocuh|叫一個檔案，或是創建一個檔案||

# 快捷鍵
**GNU bash，版本 4.4.23(1)-release (x86_64-apple-darwin16.7.0)**

|命令|說明|
|---|---|
|ctrl + A|移到行首|
|ctrl + Ｅ|移到行尾|
|ctrl + W|清空畫面|
|ctrl + U|從光標刪除到字首|
|ctrl + k|從光標刪除到字尾|
|ctrl + XX|在命令列首和光標之間移動|