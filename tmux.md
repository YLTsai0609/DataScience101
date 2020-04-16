# tmux
* [tmux 快速入門筆記](https://andyyou.github.io/2017/11/27/tmux-notes/)
* [終端機 session 管理神器 — tmux](https://larrylu.blog/tmux-33a24e595fbc)
* [tmux cheet sheet star 11k+](https://gist.github.com/MohamedAlaa/2961058)
* [How do I scroll in tmux? from `SuperUser`](https://superuser.com/questions/209437/how-do-i-scroll-in-tmux/209608#209608?newreg=8fc864abe3124c07a35ba213cd712b20)
* 一個console多個視窗，而且跨平台

# 觀念
```
原本我們打開一個 terminal 會和機器建立一個 session 當我們關掉視窗時 session 就會關閉，我們剛下的指令就會被中止。使用 tmux 意味著我們是通過 tmux server 來和機器建立 session，我們的操作視窗或視窗區塊則是跟 tmux server 溝通。

session 概略的說，指的是終端機和主機間建立的一個連線，在這個連線下的執行環境。後續文章將使用 session 。

```
|指令|快捷鍵|備註|
|---|-----|----|
|tmux|-|建立session|
|垂直分割|ctrl+b %||
|水平分割|ctrl+b "||
|視窗移動|crtl+b 方向鍵||
|切換佈局|ctrl+b space||
|關閉目前的pane| ctrl+b X|
|說明文件|ctrl+b ?|ctrl + c 離開|
|將session放到背景|ctrl + b + d||
|切回背景session|tmux at|at意思是`attach`|
|上滾、下滑|ctrl+b 進入scroll mode, 就可以用方向鍵/觸控板/滑鼠了|按q離開|
|zoom in pane|ctrl + b + z|回到多個pane也是ctrl + b+ z|

# why tmux
* 遠端連線保留session
* 跨平台 macOS, Linux, RaspberryPi, BeagleBones,...
* 客製化，可以自訂tmux設定

# 修改
* 預設讀取之conf - `/usr/local/etc/tmux.conf`，或者從man tmux -f的地方確認
* from [tmux ，不只是 terminal multiplexer 五顆紅寶石](https://5xruby.tw/posts/tmux/)
* prefix -> C+a
* 可複製文字用vi模式，並且貼上，有可能要再preference中的selection進行設定(和系統剪貼簿存在不同buffer)
  *  ctrl + V 進入vi 模式
  *  V for selection, shift + V for selection line, w for navigation
  *  y for yank
  *  q離開vi模式
  *  ctrl + p 貼上
*  在vi模式之下，複製就可以直接進到buffer中，依樣ctrl + p 貼上