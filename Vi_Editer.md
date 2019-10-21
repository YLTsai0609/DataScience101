# Why vi 
* 所有Unix like系統都內建vi，其他文書編輯器則不一定存在 (重要)
* 很多個別軟體的編輯界面都會主動呼叫vi (重要)
* 有字體顏色辨識(好像很基本)
* 編輯速度快
# About vim
* vim 為 vi 的進階版本，會主動根據你開啟的檔案來確認你是什麼語言
* 支援正則表達式搜尋，多檔案編輯，區塊複製
## vi使用
* command mode 上下左右，刪除字元，刪除整列
* insert mode  (iI, oO, aA rR)，左下方會出現 `INSERT`, `REPLACE`，退出則是`Esc`
* command-line mode 輸入 `:`, `/`, `?` 游標移動到最底下，可以提供搜尋資料，讀取，存檔，大量取代字元，離開vi，顯示行號
### 使用範例
參見txt, 使用vi開啟
* 一般vi, 其實是vim
* 參見
  * [鳥哥Linux私房菜](http://linux.vbird.org/linux_basic/0310vi.php)
  * 鳥歌裡面蠻多指令都不work的，可以參見[大家來學vim](http://www.study-area.org/tips/vim/index.html)
  * [高見龍也分享了一些](https://kaochenlong.com/2011/12/28/vim-tips/)
* 
* 複製 y
* 複製該列n個詞 y {數字} w
* 複製多行 {數字} yy 成功時，下方會顯示 `x lines yanked`
* 貼上/貼上多行 p / shift + ctrl + v
* 註解
* 註解多行
* 上一步 u
* 下一步
* 自動縮排
* 執行外部指令 例如 : !ls
* 顯示行號 `set nu` <--> `set nonu`
* 觀看Options `set`