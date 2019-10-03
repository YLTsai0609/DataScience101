# Six Step to more professional data science code
6 Steps for More Professional Data Science Code | Kaggle 重點節錄
* [Youtube](https://www.youtube.com/watch?v=Trar7GZOPl8)
* [Kaggle NoteBook](https://www.kaggle.com/rtatman/six-steps-to-more-professional-data-science-code/)
* [講者 - Rachael Tatman (Data Scientist at Kaggle)](https://www.kaggle.com/rtatman/kernels?sortBy=dateCreated&group=everyone&pageSize=20&userId=1162990)

# 主要目標
* 可重複使用的
讓你的程式碼可以被重複使用，讓你不用再重寫，做事情能夠更有效率
我們可以透過6個方式來達成
1. 模組化(Modular) 把程式碼寫成function，讓他們可以被重複使用
2. 正確性(Correct) 要是正確的Code
3. 可讀性(Readable) 要讓人一目瞭然看懂程式碼，包含3個月後的你自己
4. 明確風格(Stylish) 程式碼維持良好的風格(像是PEP8 for python)
5. 通用性(Versatile) 解決那些會重複出現的任務，寫成function
6. 創造性(Creative) 解決那些還沒被解決的問題

#### Why fuctions?
或許你注意到我喜歡用functional programming而非 object oriented programming
主要是因為functional programming(FP)可以做到這件事
`data -> function 1 -> function 2 -> function 3 -> transformed data`
這會讓你的code非常容易理解
你可以透過`pyjanitor`來完成這件事，就像是
```
cleaned_df = (
    pd.read_excel('dirty_data.xlsx')
    .clean_names()
    .remove_empty()
    .rename_column("full_time_", "full_time")
    .convert_excel_date("hire_date")
)

cleaned_df

```

#### Correct 
為什麼這也要談? 一定要寫正確的才對啊！ 事實上我想說的是，如果可以加一些邊界條件的確認，或是簡單的test-case，這會讓你更好對function做debug，例如加入`assert`
```
import collections

def find_most_common(values):
    """"Return the value of the most common item in a list"""
    list_counts = collections.Counter(values)
    top_two_values = list_counts.most_common(2)

    # make sure we don't have a tie for most common
    assert top_two_values[0][1] != top_two_values[1][1]\
        ,"There's a tie for most common value"
    
    return(top_two_values[0][0])

```
我們可以看到，我們加入了一個assert的檢查，讓我們日後在這支function出錯時更能夠快速地了解問題出在哪裡，在這個函數中，有兩個most_commin值出現時，則會出現AssertionError

# Reference
* [pyjanitor](https://github.com/ericmjl/pyjanitor)
* [Kaggle Notebook](https://www.kaggle.com/rtatman/six-steps-to-more-professional-data-science-code/)