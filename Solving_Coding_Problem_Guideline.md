# How to Soling a Coding Problem?

**Stackoverflow Question Asking can be a lead !**
1. PreSolving
   * 有把錯誤訊息`去除掉自己電腦上的資訊`放到google搜尋欄中詢問過嗎?
   * E.g. 
   * Error message :  `File "C:\Users\WIN_10\PycharmProjects\yolo\....tensorflow\python\framework\common_shape.py" line 691, in _call_app_shape_fn_impl raise ValueError(err.message)`, `ValueError Dimension 0 in both shapes must be equal, but are 1 and 255, Shapes are [1,1,1024, 21] and [255, 1024, 1, 1] fpr Assign_360 (op:Assign)`
   * Searching with : `yolo tensorflow python framework common_shapes.py ValueError Dimension 0 in both shapes nust be equal`
   * Searching with (一定要出現yolo)`"yolo" tnesorflow......`
   * [google搜尋技巧](#google-%e6%90%9c%e5%b0%8b%e6%8a%80%e5%b7%a7)
   * 幾個常常網友問問題得地方
     * stackoverflow
     * github issue

2. Title : 精確的描述，例如`Is there an R function for finding the index of an element in a vector?`
3. Body
   1. 從你`想達成的結果`開始
   2. 描述`你做了什麼事情`
   3. 給出最小可以被實現的程式碼
   4. 再次說明以程式結果而言，你希望可以得到的結果是什麼
   5. 說明你再發問前，`有試過哪些方法，但是不work`

# 引導對方

1. 現在你在做的事情是什麼? 現在在哪個步驟?
2. 你試過了什麼方法?


# google 搜尋技巧
1. 精準比對  ""
    * 例如 ls -al 搜尋 "ls-al"
2. 排除指定條件的結果 -
    * 例如 國內旅遊 - "南投"
3. 未知字詞搜尋 * 
    * 例如 五*天，披星戴月的**
4. 站內搜尋 site:
    * 例如 pd.where using  site:stackoverflow.com
    * 應用點 "magiclen.org" -site:magiclen.org
        * 本站文章連結被分享到那些站外資源
5. 指定檔案類型 filetype:
    * 例如 numpy tutorial filetype:pdf
6. after: 某個日期之後
    * 例如 dataframe documentation after:2019-01-01
Reference
7. 覺得講得太少，自行google `google搜尋技巧`

## 預防勝於治療 - 找github source code的注意事項

1. 是否有官方，還是私人的?
2. 目前維護的情況如何? (github issue and commits)  