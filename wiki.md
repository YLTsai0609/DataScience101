# Wiki

1. [MediaWiki](https://www.mediawiki.org/wiki/MediaWiki) - Wiki 系統，容易更動、版本紀錄、簡易權限控管、檔案上傳、支援多國語系，
   [維基百科](https://en.wikipedia.org/wiki/Main_Page)，
   [台灣棒球維基館](http://twbsball.dils.tku.edu.tw/wiki/index.php?title=%E9%A6%96%E9%A0%81) 都是雞䱷 MediaWiki 發展而成的網站
   
2. MediaWiki 用 php 寫的，並且架設在 MySQL 上，而對於維基百科來說，他的 MySQL Database 是公開開放下載的, [credit](http://www.happystreet.com.tw/index.php/dynamic-teaching/host-websites-tips/159-mediawiki-installation-instruction)


# Database of wiki

[Manual:Database layout](mediawiki.org/wiki/Manual:Database_layout)

1. MediaWiki 1.35
2. most important tables - page, resion, text, user

[the schema of table in database - an overview](https://www.mediawiki.org/w/index.php?title=Manual:Database_layout/diagram&action=render)

# categorylinks table

1. table stores entries corresponding to links of the form [[Category:Title]] or [[Category:Title|sortkey]]
* [credit](https://www.mediawiki.org/wiki/Manual:Categorylinks_table)
* 從 `categorylinks` - 就可以透過分類表(`cl_to`, `cl_sortkey`) 來取得 edge 的關係，也可以直接對應到[頁面結果](https://zh.wikipedia.org/wiki/Category:%E7%81%AB%E9%8D%8B)