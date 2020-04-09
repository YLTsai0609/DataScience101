# 目的
* 了解別人的程式碼怎麼運作，如果給定某個input，會不會有預期output?
* 了解自己即將要設計的函數(物件)會怎麼運作，在給定個input下，會不會有預期的output?
* 能夠對自設計的函數有信心，因為不是憑空想像怎麼操作，而是實際有testcase跑，而且通過

# 主流框架
框架|說明|備註
-----|-----|-----
unittest|python原生，需繼承物件，要寫較多程式碼，有setup和teardown，分別是所有程式測試前以及測試完之後跑，可以較全面的測試|使用過Java, .Net, C/C++的開發者們會比較熟悉他
pytest|第三方套件，語法簡潔，兼容unittest程式碼，豐富擴展plugin(例如django)，平行化測試(pytest-xdist)|
nose|第三方套件，更注重自動化測試，可以產生自動化測試報告(html)||

# 當前選用
* 目前使用pytest - 撰寫測試程式碼時速度快，無複雜需求
* 若要用unittest, nose還要再survet一下
* 使用pytest的demo可參考[demo case](/demo/pytest_demo/test_sample.py)
# 參考
* [Python 的檢查及測試工具箱](https://medium.com/pyladies-taiwan/python-%E7%9A%84%E6%AA%A2%E6%9F%A5%E5%8F%8A%E6%B8%AC%E8%A9%A6%E5%B7%A5%E5%85%B7%E7%AE%B1-eda71af68c19)
* Python 專家實踐指南
* Effective Python 寫出良好python程式的59個具體作法
* [Python備忘錄](https://jinsenglin.gitbooks.io/memo-of-python/content/part1/doctest-unitest-nose-pytest-tox.html)
* [詳解Python nose單元測試框架的安裝與使用](https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/361874/)