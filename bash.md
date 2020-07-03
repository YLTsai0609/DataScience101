# bash
> 紀錄工作中常用到的一些bash指令，以及使用場景
> 查看當前bash版本 `help`
* [TODO] 週一問問題
* 有沒有快捷鍵可以前選一個字? (已經查過網路了，可是不work)
* 怎麼看目前terminal的一些short cut

# NetWork
|命令|使用場景|備註|
|---|-------|---|
|`ifconfig`|查自己的這台的ip||
|`ipython` `import socket` `socket.gethostbyname('deviceName')`|從A主機經由同網域的連線查詢B主機的ip|ipython要pytho3.5以上才支援|
|`ping` ip adress|從A主機經由同網域的連線查詢B主機目前的連接狀況及速度(time out, or speed xx/ms)|ping = 戳，測自己網速可以搭配內部迴圈網路 127.0.0.1|
|`nmap` IP/DNS|查詢子網域內所有ip以及DNS，有ip, 如果該機台有ssh, 就能夠進入 掃描範例 : `nmap 192.169.0.*` 掃描此之下所有子網域, `nmap www.hinet.net` 透過DNS。掃描需要一段時間|`nmap`需要安裝，mac透過`brew`, ubuntu透過`apt`，DNS全名為Domain Name System|
|`scp userName@ip adress:filePath MyfilePath`|已知主機filePath，從主機抓檔案/資料夾到本地端||
|`scp MyfilePath userName@ip adress:filePath`|把本地端的檔案copy到主機端的目錄|
|`ssh userName@ip adress`|經由ssh連線到主機端，但主機端需要是一個ssh server，或是有給予ssh金鑰|mac需要打開"允許遠端登入" "系統偏好設定" --> "共享" --> "遠端登入"|
|`curl ifconfig.me`|查詢目前該機台的外部IP，多個機台可能是一樣的外部IP|

* [鳥哥一下 : [第11章、遠端連線伺服器 SSH/XDMCP/VNC/RDP]](http://linux.vbird.org/linux_server/0310telnetssh.php#scp)
* [scp 簡明使用守則](http://note.drx.tw/2008/03/ubuntuscp-part1.html)


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

## ifconfig/ipconfig
* (InterFace config) 提供檢測以及網路介面卡進行互動的指令

|名詞|解釋|備註|
|----|---|---|
|eth0|偵測到的介面名稱(Ethernet0的縮寫)|如果系統中有更多乙太網路介面，則會一一列出|
|EthernetHWaddr : `00:0c:29:ba:....`|網路介面卡位置，稱為MAC(media access control address)|
|inet addr|當前分配給網卡的IP位置(可能是固定IP或是浮動IP)|
|Bcast|broadcast address，廣播位置，用來發送給所有位於子網路內機台訊息的ip位置||
|Mask|網路遮罩，決定哪一部分是屬於網路或是主機||
|lo|loopback adress, localhost|連接到本地系統，測試用|
|wlan0|**無線網路介面卡**裝置||
|LAN|Local Area Network 區域網路||

* ipconfig是windows上的ifconfig

## iwconfig
* (Interface wireless config) 無線網卡的相關config
* Ubuntu上面有，但mac尚有編譯問題，沒辦法安裝

* ifconfig的潛能
* 修改本機IP位置(暫時的，永久修改要google)，變更網路遮罩，變更廣播位置，竄改MAC位置
* DHCP (Dynamic Host Configguration Protocol)能夠透過這個協定和基地台溝通，修正發送下來的IP，但在mac中需要google一下是用什麼指令，然後brew安裝它

## 操控DNS
* DNS : IP <--> www.google.com(人類看得懂的網域名稱)
* Hacker能夠從其中竊取許多關於入侵目標的重要資訊
* `dig`能夠搜尋有關目標域名的DNS資訊
* 改變DNS Server
  * 相關檔案在Unix-like的系統之下被放在/etc/resolv.conf的domain以及nameserver
  * 透過修改donmain以及nameserver就能夠自訂跳板服務([VPN - Virtual Private Network](https://zh.wikipedia.org/wiki/%E8%99%9B%E6%93%AC%E7%A7%81%E4%BA%BA%E7%B6%B2%E8%B7%AF))
* 自定義IP位置
* 相關檔案在Unix-like的系統之下被放在/etc/hosts
* 可以自訂一個IP，然後後面接一個DNS，該主機連線到該IP時就會被重定向到指定DNS，可以透過狹持TCP連線引導至惡意網站

## nmap
nmap <type of scan> <target IP> <optionally, target port>
* nmap 掃描自己區網內所有連網裝置IP,Port, 及開啟的服務
  * 先透過ifconfig, 如果屬於一個區網(LAN)，則取前三碼，例如192.168.0
  * nmap 192.168.0.* > scanlist.txt
* 可以搭配**封包監聽**，**封包攔截**，如果有人正在傳送密碼而且是明碼，就可以截取到密碼。
* 不局限於區網，只要有IP就可以實作任何的掃描
  * `echo Enter the starting IP adress`
  * `read FirstIP`
  * `nmap ${FirstIP}-${LastOctIP}...`

### More about SSH
pass

### 即時串流相關協定
* 動機 : 在樹莓派上利用TPU做Edge Computing，將結果及影片即時串流回主機Server，原本使用base64將 video image 壓縮成base64字串，在Client端再用based64 decode，但這個方法扔然會延遲。
* 概念 : 回想一下我們對影片的上傳下載，由於多媒體檔案通常都比較大，所需要的儲存容量也大，由於網路頻寬的限制，下載多媒體檔案都需要花費數分鐘甚至數小時，所以如果是這種下載方法來傳送多媒體檔案的延遲會非常大
* 串流(Streamming)的概念，只將開始部分存入記憶體，資料流隨時傳送隨時播放，只會在開始時有一些延遲，中間過程通常都會非常順暢，下列為網路串流發展的一些歷史 : 
 
|協定|解釋|
|---|----|
|RTP(Real-time Transport Protocol) 即時傳輸協議|串流協定剛開始發展的協定之一|
|RTMP：即時傳輸訊息協議(Real Time Messaging Protocol)|被Flash用於物件, 影片, 音訊傳輸, 這個協定建立在TCP或是HTTP之上，由於被包裹在TCP裏頭，實作出來畫質還可以，但延遲時間有2秒左右，對於Realtime的要求來說還是較長。|
|RTSP：即時串流協議(Real Time Streaming Protocol)|除了控制聲音或是影像外，還可以允許同時多個串流需求控制，並且可以自己選擇要用TCP或是UPD來進行串流內容，在這個Protocol中可以傳送播放、錄製、暫停等等控制協定、蠻像遙控錄影機的。|
* 上述中的RTSP也是我們採用的協定，[其Wiki在這裡](https://zh.wikipedia.org/wiki/%E5%8D%B3%E6%99%82%E4%B8%B2%E6%B5%81%E5%8D%94%E5%AE%9A)
* 套件實作 GStreamer, based on C，可以使用樹莓派硬體進行H.264編碼，串流品質優

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
## 執行方式 

|執行方式|效果|
|-------|---|
|sh xxxx.sh|該script會用一個新的bash環境來執行script中的指令，換句話說，裡面的變數並不會回傳到父程序中|
|source|在父程序中執行|

## 條件判斷
當你的條件很多時，就不會想用&&或是||了，會太多東西
1. if...then
```
read -p "Please input (Y/N):" yn

if ["${yn}"=="Y"]||["${yn}"=="y"]
  echo "OK, continue"
  exit 0
fi

if ["${yn}"=="N"]||["${yn}"=="n"]
  echo "Oh, interrupt"
  exit 0
fi

echo "I don't know what your choice is" && exit 0
```
2. 多重條件


[鳥哥一下 - 第12章、學習 Shell Scripts](http://linux.vbird.org/linux_basic/0340bashshell-scripts.php#script_why)



# 變數
* 動機 : 每次都被，環境變數/路徑 PATH搞得很煩，要來好好了解一下變數，進而提供可操作性
* 概念 : 當輸入`mail`這個指令時，如果你是root, 則會執行 `var/spool/mail/root`，當你是vbird，則會執行 `/var/spool/mail/vbird`
  如此一來，一個變數，通吃所有user，不用把執行路徑寫死，這樣的概念用在所有可被呼叫的指令中，像是`ls`, `cat`, ...等所有指令
  同樣的道理，不只可以用在系統預設上，進行開發時，也可以利用bash的變數，來處理每台電腦都不一樣的路徑問題!

* 變數取用 `echo $HOME` or `echo${HOME}`
* 變數賦值 
```
[dmtsai@study ~]$ echo ${myname}
       <==這裡並沒有任何資料～因為這個變數尚未被設定！是空的！
[dmtsai@study ~]$ myname=VBird
[dmtsai@study ~]$ echo ${myname}
VBird  <==出現了！因為這個變數已經被設定了！
```
* 變數給值規則
1. 有些shell中echo空的變數會是空的，有些則會噴error，要注意
2. 不能有空白字元 myname = VBird 會噴錯
3. 變數名稱只能是英文字母和數字，但**開頭不能是數字**，例如`2nyname=VBird`會噴錯
4. 變數內容需要空白字元，可以使用`"`或是`'`
   * **雙引號內的特殊字元，可以保有原本特性**，例如 `var="lang is $LANG"` -> `echo ${var}` 可以得到  lang is zh_TW.UTF-8
   * **單引號內的特殊字元，則僅為純文字**，例如 `var="lang is $LANG"` -> `echo ${var}` 可以得到  lang is $LANG
5. 可用跳脫字元`\`將特殊符號變成一般字元，例如 `myname=VBird\ Tsai` 
6. 一串指令中需要藉由其他指令提供的資訊，除了使用`$`還可以使用反向單引號，例如 `version=$(uname -r)` -> `echo $version` 可以得到 3.10.0-229.el7.x86_64
7. 如果想要累加變數(擴增變數內容)，可以這樣子，以PATH舉例 : `PATH=${PATH}:/home/bin`，再一個例子 : `version=${version}MacAir`
8. 若該變數需要在其他子程序執行，則需要`exoport`來使變數變成環境變數，例如 : `export PATH`
9. 通常大寫字元為系統預設變數，自行設定變數可以使用小寫，方便判斷(純粹依照使用者興趣)
10. 取消變數的方法 : `unset`，例如 `unset myname`
11. 遇到設定變數榮需要`'`，用雙引號包起來 : `name="VBird's name"`
12. 將自訂變數用在路徑上
```
d=pandas_101
echo ${d} # for check the variable
cd ~/Desktop/${d} # worked!
```

## 環境變數
變數當中，被linux系統預設能夠使用的，稱為環境變數，可以幫助我們完成**家目錄變換**，**提示字元顯示**，**執行檔搜尋的路徑**等等
* `env` 列出目前shell環境下的所有環境變數以及變數內容

|變數|值|
|---|--|
|HOSTNAME|study.centos.vbird|
|TERM|xterm|
|SHELL|/bin/bash|
|USER|dmtsai|
|HITSIZE|1000 指的是系統會記錄過去的1000個命令|
|PATH|執行黨的搜尋路徑，就是我們所謂的環境變數，目錄和目錄之間用冒號分隔，由於檔案的巡雲是依序由PATH目錄來查詢，所以目錄的順序也很重要喔|
|HOME|/Users/yltsai 也就是家目錄|
|LANG|語系資料，對我們來說通常是zh_TW.UTF-8或是 zh_TW.Big5|
|_|/usr/bin/env 上一次使用的指令的最後一個參數|

* `set` 列出所有變數，包含環境變數與自訂變數
例如我們自己設的變數

* 不論是否為環境變數，只要跟我們目前這個shell操作介面有關的變數，通常會被設成大寫

* 重要的 shell 變數
  * PS1(數字的1)，這個東西就是命令提示字元，每次按下[Enter]執行某個指令後，最後要再次出現提示字元時，就會主動讀取這個變數值，可以man bash查詢一下PS1的相關說明
  * 錢字號 關於本shell的PID，錢字號本身也是個變數，這個東東代表的是**目前這個shell的執行緒代號**
  * 可以透過 `$$`來顯示PID號碼
  * ? (關於上個執行指令的回傳值)，沒錯，問號也是一個特殊變數，這個變數指的是**上一個執行的指令所回傳的值**，上面這句話的重點是**上一個指令**和**回傳值**兩個地方，當指令執行成功時，指令代碼會回傳0，如果執行過程發生錯誤，會回傳錯誤代碼，一般來說就是非0的值
  ```
  echo $SHELL
  echo $? -> 0 # 沒問題，所以顯示0
  12name=VBird
  echo $? -> 127 # 因為有問題，回傳錯誤代碼
  echo $? -> 0 # 因為上一個指令 echo $?是正確指令，所以回傳0
  ```
* `export` 自訂變數轉成環境變數
  自訂變數與環境變數的差異在在於**該變數是否會被子程序繼續引用**
  <img src='/images/bash_variable_1.png'></img>
  * 我們在原本的bash底下執行另一個bash，那原本的bash就會睡著(父程序)，我們開啟的另一個bash則稱為子程序
  * **子程序僅會繼承父程序的環境變數，子程序不會繼承父成數的自訂變數!**
  * export可以將變數輸出，讓父程序可以使用!

### 加入環境變數
1. 先確認該檔案存在在你的系統中，這裡舉例mysql
`ls /usr/local/mysql/bin/mysql` - 確認執行檔存在
2. 進入.bashrc, .bash_profile
```
# MySQL path variable
mysql_path=/usr/local/mysql/bin/
export PATH=$PATH:mysql_path
```

3. source .bashrc, .bash_profile

4. echo $PATH - 確認路徑是否存在

5. 呼叫指令，應該要呼叫到該執行檔, 例如呼叫 mysql


# 變數鍵盤讀取、陣列和宣告 : read, array, declare
* `read`, `declare`, `typeset`, `array`
pass

# 檔案系統及程序的限制關係 
* `ulimit` : 限制Server上每個user的記憶體配額
pass

# 變數內容的刪除、取代和替換
pass

# 命令別名設定 : alias, unalias
* 動機 : 常常使用 `ls-al | more` 來看檔案，可是每次都要打這麼多字，覺得很煩
* `alias lm='ls -al | more'`，會立刻多出一個可執行的指令`lm`
* alias的定義與變數定義規則幾乎相同，所以要輸入指令時要以純文字，因此要加單引號，如果加雙引號，後面內容會是變數名稱喔
* 取代原本的rm `alias rm='rm -i'`，因為總會有手殘誤刪的時候
* 怎麼查現在有哪些alias? `alias`
```
alias

alias egrep='egrep --color'
alias fgrep='fgrep --color'
alias grep='grep --color'
alias ls='ls -F --show-control-chars --color=auto'
# 可以看到我們透過alias來設定一些顯示的顏色
```

# history 
歷史命令
透過history指令一次查看所有下過的命令
* 寫入時間 : 關掉terminal時，因此多個bash會有無法查到命令的情況
* 無法記錄時間 : 雖然history是按照時序紀錄，但是無法紀錄時間，或是修改 ~/.bash_logout來進行修改config
  
# 萬用字元與特殊符號

|符號|意義|備註|
|---|----|---|
|*|代表0個到無窮多個|從regax抄來的|
|?|代表一定有一個|從regax抄來的|
|[]|代表一定有一個在[]裡面，例如[abcd]代表一定有一在字元，可能是a,b,c,d任何一個|從regax抄來的|
|[-]|連續字元, 例如[0-9], [A-Z]|從regax抄來的|
|[^]|反向選擇，[^abc]找一個字元，非abc|從regax抄來的|
|#|註解符號，用在script中||
|\|跳脫符號，將特殊字元或萬用字元還原成一般字元||
|**|**|管線符號||
|;|連續下達指令 : 連續性命令，和管線符號並不相同||
|~|家目錄||
|$|取用變數的前置字元||
|&|將指令變成背景工作||
|!|not||
|>, >>|資料流重定向, 取代, 累加||
|<, <<|資料流重定向||
|''|單引號，不具有變數置換的功能，內容變成純文字||
|""|具有變數置換的功能，可保留相關功能||
|``|等同於$()，表示先做裡面的命令||
|()|子shell的起始和結束，先做的意思||
|{}|命令區塊的組合||

# pipe
* [鳥哥 第十章 10.6 管線命令, 6-1, 6-2](http://linux.vbird.org/linux_basic/0320bash.php)
* pipe是幹嘛的? bash命令執行的時候會有輸出資料出現，如果你要的資料需要經過幾道手續之後才會得到我們要的格式
  就要透過pipe來設定了，管令命令用的是 **|** 這個界定符號，另外，管線命令與 **連續下達命令**是不一樣的，下面會說明，不過我們先來舉個例子
> 我們想要知道 /etc/ 底下有多少檔案，那麼可以利用 ls / etc 來查閱，不過，因為 /etc底下的檔案太多，導致於一口氣就將螢幕塞滿了，不知道前面輸出的內容是啥，我們可以透過less指令來協助
`ls -al /etc | less`
這樣我們就能夠翻頁來查找剛剛吐出來的訊息了，同樣的道理，你也可以使用 `ls -al /etc | head -n 5`
### pipe做了什麼?
其實這個管線命令，**僅能處理經由前面一個指令傳來得正確資訊，也就是 standard output，對於 standard error並沒有直接處理的能力**

<img src = './images/bash_pipe_1.png'></img>

* 在每個管線後面接的第一個資料必定是**命令**才行，例如 `less` `more` `head` `tail` 等都是可以接受 standrar input，至於`ls`, `cp`, `mv`就不是管線命令了，因為後面這3個命令並不會接受 stdin的資料
* 管線命令僅會處理 standard output，對於 standard error output 會予以忽略
* 管線命令必須要能夠接受來自前一個指令的資料成為 standard input 繼續處理才行。

### 擷取命令 cut, grep
* cut : 切
`cut -d '分隔字元' -f fields <--- 用於有特定分隔字元`
`cut -c '字元區間' <--- 用於排列整齊的訊息`
```
E.g 1 將PATH取出，第5個路徑
echo ${PATH} <--- 叫出路徑
echo ${PATH} | cut -d ':' -f 5 <---  叫出路徑，然後切出第5個
E.g 2 將 export 輸出的訊息，取得第 12 字元以後的所有字串
export | cut -c 12-
```
cut這樣的功能在看log的時候特別實用
* grep : 剛剛的 cut 是將一行訊息當中，取出某部分我們想要的，而 grep 則是分析一行訊息， 若當中有我們所需要的資訊，就將該行拿出來～簡單的語法是這樣的：

```
grep -[acinv] [--color=auto] '搜尋字串' filename
-a ：將 binary 檔案以 text 檔案的方式搜尋資料
-c ：計算找到 '搜尋字串' 的次數
-i ：忽略大小寫的不同，所以大小寫視為相同
-n ：順便輸出行號
-v ：反向選擇，亦即顯示出沒有 '搜尋字串' 內容的那一行！
--color=auto ：可以將找到的關鍵字部分加上顏色的顯示喔！

E.g 1 : 將last當中，有出現root就取出來
last | grep 'root'
E.g 2 : pip list中，有tensorflow就取出來
pip list | grep 'tensorflow'
E.g 3 將last中，"沒有" root的取出來
last | grep -v 'root'
E.g 4 在last中，只要有root就取出，而且只取取第1欄
last | grep 'root' | cut -d '' -f1
E.g 5 取出 tec/man_db/conf 內含有MANPATH得那幾行
grep --corlor=auto 'MANPATH' /etc/man_db.conf
```
`grep`是個非常好用的命令，基本上就是一行的if-else, 用在正規表達式裡面更是一絕，值得學習

# 資料流重定向
* [鳥哥 第十章 10.5 資料流重定向](http://linux.vbird.org/linux_basic/0320bash.php)
* 什麼是資料流重定向? : 把資料傳導到其他地方去，也就是不從顯示在terminal, 可以傳到檔案裡面, 或是印表機, 等等

<img src = './images/bash_dataflow_redirection_1.png'></img>

## stdout, stderr
* 如上圖，我們執行一個指令時，這個指令會由檔案讀入資料，處理後，輸出到螢幕上，分別為**標準輸出(STDOUT)**，以及**標準錯誤輸出(STDERR)**
我們能不能透過某些機制將這兩股資料分開呢? 當然可以，這就是所謂資重定向


|概念|用法|
|---|----|
|標準輸入 (stdin )|代號 0, 使用 < 或是 <<|
|標準輸出 (stdout)| 代號 1, 使用 > 或是 >>|
|標準錯誤輸出(stderr)|代號 2, 使用 2> 或是 2>>|

例如 : `ls > test.txt`
資料就會盡到`test.txt`
* 注意 : 如果系統原本沒有該檔案，會新開出來寫，但是如果已經存在，就會覆寫
* 這時候要使用累加， `>>`
* 將正確資料與錯誤訊息分流 `ls ~/Desktop/aaa 1>> correct.txt 2>> error_log.txt`
* 黑洞裝置 : /dev/null 可以吃掉任何東西 `find /home -name .bashrc 2> /dev/null`

* 紀錄所有termial stdout到log檔案，寫一個bash script，每次開機就在背景執行
## stdin 
* <, << 將原本需要由鍵盤輸入的資料，改由檔案內容來取代
`echo 'ls ~/Desktop' > showDesktop.txt`

需要stdin, stdout, stderr的場景
1. 螢幕輸出訊息很重要，我們需要將它存下來時
2. 背景執行中的城市，不希望他干擾螢幕正常輸出結果時
3. 系統例行命令希望可以存下來時(例如crontab)
4. 一些執行命令可能已知錯誤訊息，想以 2>/dev/null丟掉時
5. 錯誤訊息和鄭瘸訊息需要分別輸出時

## example

安裝軟體時，你希望有log紀錄又有stdout

使用 tee

範例

`ls 2>&1 | tee file.tmp` 

super easy!

[How do I get both STDOUT and STDERR to go to the terminal and a log file?](https://stackoverflow.com/questions/363223/how-do-i-get-both-stdout-and-stderr-to-go-to-the-terminal-and-a-log-file)


## 命令執行的判斷依據 : ; && ||

|指令|舉例|說明|
|----|--|----|
|cmd1; cmd2; cmd3|sync; sync; shotdown -h now|先執行兩次sync同步寫入磁碟，然後關機，輸出的commend有前後依賴關係時|
|cmd1 && cmd2|ls /tmp/abbc && touch /tmp/abc/hehe| ls指令執行完畢而且正確執行($?=0)，則開始執行cm2，cmd1執行完畢且為錯誤($?!=0)，則cmd2不執行|
|cmd1 || cmd2|ls /tmp/abbc && touch /tmp/abc/hehe| 和上面一個反過來|

linux命令是由左至右的，所以`&&`和`||`的位置不要放反喔!



# Job Control 工作控制

|命令|使用場景|備註|
|---|-------|---|
|`nohup`|放到主機算，然後自己登出，搭配 `ctrl + z`, `bg` |nohup = no hang up|
|`bg`|把執行緒丟到後台，搭配nohup||
|`fg`|把執行緒拉回前台，佔住自己的terminal XD||
|`kill`|根據Job ID 把程式殺掉||
|`wait`|等待某Job跑完，或是並行處理完||

# file profiling  
|命令|使用場景|備註|
|---|-------|---|
|cat|檔案不大，覺得vi很難操作，複製程式碼時|cat會看整個檔案|
|less|一頁一頁看，而且可以往前翻頁|忘記less怎麼用的時候，less file 然後 h，基本操作 f - forward, b - backword, 可以設定一次看幾行|
|head|看個前幾行，意思一下，跟dataframe.head()一樣||
|tail|看個後面幾行，意思一下，跟dataframe.head()一樣||
|echo|叫一段文字、或是叫一個檔案、叫環境變數|怎麼叫環境變數? echo $PATH|
|tocuh|叫一個檔案，或是創建一個檔案||

# System profiling

|命令|使用場景|備註|
|---|-------|---|
|top|最簡易版的工作管理員，可以看CPU，跟thread還有ProcessID|10秒更新，都黑白，可以用htop|
|htop|豐富版，支援filter，自動提示，排序，比較美等等|Mac :brew install htop-osx|
|df - h|Dsik Free，顯示磁碟空間資訊||
|uname -a|顯示系統核心資訊||
|w|顯示上線使用者清單|可以在Server現在有誰連，有沒有怪人這樣|
|whoami|顯示目前使用者名稱||
|free|顯示記憶體與Swap區的用量||

[htop使用](https://blog.gtwang.org/linux/linux-htop-interactive-process-viewer-tutorial/)

* 什麼是`swap` : 硬體加速，當記憶體滿載時，會從硬碟中借一些容量拿充當記憶體，常用的話，很傷記憶體
# 檔案查找

|命令|使用場景|備註|
|---|-------|---|
|locate|找檔案|幾分鐘，幾個小時前的會找不到，located會找到很多，會搜尋整個檔案系統，搜尋的db一天更新一次|
|whereis|找二進位檔，回傳兩個結果，二進位檔以及操作手冊位置|不會回傳所有帶有關鍵字的檔案，不會很雜，但是重點是要知道你要找的是二進位檔|
|which|一樣找二進位檔，只是會在PATH variable中尋找||
|find|最萬用的進階搜尋|如果不知道搜尋根目錄的話，會挺慢的，要等一會|

`find search root -type f/d -name xxx.sh`, 支援萬用字元和正則表達式


# 軟體管理

|OS|中介軟體(下載軟體用的軟體)|備註|
|--|----------------------|---|
|macOS|brew, flnk||
|Ubuntu, Debian|apt, dpkg||
|?|curl|curl有Library的版本，程式可以利用curl當作HTTP Client使用，支援比較多網路協定，支援的作業系統比wget多|
|?|wget|最方便的一點，wget可以遞迴下載檔案，把子資料夾跟子子資料夾都下載，wget較為直覺|

* [fink mimic `apt`, `apt-get` on macOS](https://blog.csdn.net/camlot_/article/details/47424671)
* brew based on ruby(macOS自帶)
* apt(advance package tool) for debian-based linux kernel


# 檔案系統

<img src = './images/bash_file.png'></img>
* Mac也長得很相似

## GRUB
GRUB是諸多linux發行版採用的開機管理程式(bootloader)
雖然Ubuntu 9.10以後的版本開始採用 GRUB 2，但是追求穩定的人往往還是使用GRUB

## kernel管理

使用`ukuu`工具，能夠輕易管理及安裝Kernel

匯入外部鏡像
`sudo add-apt-repository -y ppa:teejee2008/ppa
`
更新鏡像源
`sudo apt-get update`

安裝ukuu
`sudo apt-get install ukuu`

[reference](https://peterli.website/%E5%A6%82%E4%BD%95%E5%9C%A8ubuntu-18-04%E4%B8%8A%E9%9D%A2%E5%AE%89%E8%A3%9D%E8%88%87%E7%AE%A1%E7%90%86kernel/)

# CPU, GPU, Memory

|命令|說明|
|---|---|
|lscpu|查看機台CPU狀態, 包含核心數, 執行緒數, 快取等|
|nvidia-smi|顯示當前GPU所有基礎資訊|
more about GPU info 
https://www.itread01.com/content/1541720962.html

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