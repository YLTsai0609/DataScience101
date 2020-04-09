'''
pytest安裝之後會寫進環境變數中，所以可以在terminal中執行pytest
例如 : (py_37_ds) YuLong@wangyuxuandeAir:~/Desktop/Working_Area/DataScience_Note/demo/pytest_demo$ pytest
會遞迴搜尋~/Desktop/Working_Area/DataScience_Note/demo/pytest_demo
及路徑下的子目錄中所有以 test_ 開頭的測試檔，或者 pytest.ini 中指定的檔名或 func 名
可以加入folder argument
可以指定測試某檔案
可以指定不測試某檔案，其餘全部要測試
'''
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4


'''
我們將測試都寫在這裡，原本的func則寫在module_a.py
裡面的內容是
def just_do_it(text):
    return text.capitalize()
因此我們需要import該檔案的函數近來進行測試
函數名稱需要是test開頭，後面就接你想接的case名稱
'''

import module_a

def test_one_word():
    text = 'duck'
    result = module_a.just_do_it(text)
    assert result == 'Duck'
def test_multiple_words():
    '''
    這個case不會過，因為只會把第一個字的第一個字母大寫
    '''
    text = 'a veritable flock of ducks'
    result = module_a.just_do_it(text)
    assert result == 'A Veritable Flock Of Ducks'


