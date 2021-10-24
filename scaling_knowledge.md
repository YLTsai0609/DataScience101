# Why

團隊日益壯大，但分析總是重工(以前做過的就不要再做了)，某些分析步驟可被重用

1. 協作性(Data team and cross team)
2. insights 重用性
3. 教學性(觀察他人分析時使用的程式碼技巧)
4. 重現性(dataset and development env)

# Solutions

jupytext - `.ipynb` --> `.py` 可協作，可版本控制

file-server - 跨團隊 & 團隊內快速分享 insights

peer review - 確認分析結果正確性

search engine - search by code snippets / search by file name / search by tags(大量html, notebook中找以前有沒有人做過)

## Existing Solution

[knowledge repo](https://github.com/airbnb/knowledge-repo)

1. gitpython for trigger
2. gitpython for notebook versioning
3. MySQL and tags for search


https://github.com/YLTsai0609/knowledge_repo_cheatsheet


cons:

1. 顯示上不容易 : rendering尚有問題
2. 尚無法Getting start : docker image support
   * https://github.com/airbnb/knowledge-repo/issues/521 To be tested
   * 目前 docker 還有點問題，應該是要從docker image調整，或是等待官方docker image 釋出
   * `/Users/yulongtsai/Desktop/Working_Area/knowledge-repo-docker`
## Breakdown

1. [GitPython - github trigger](https://github.com/gitpython-developers/GitPython) - pull sutff to servering server when anyone push something.
2. [jypytext](https://github.com/mwouts/jupytext) - versioning and collobaration with team
3. [nbconvert - convert notebook to html,pdf, ...](https://github.com/jupyter/nbconvert)
4. [file-server (markdown and html)](https://github.com/YLTsai0609/ReadEm)
   1. `markdown` package for display markdown
   2. integreate static python http file server.
5. [search engine](https://github.com/quiltdata/t4)
   1. [medium post](https://blog.quiltdata.com/find-your-jupyter-notebooks-with-elasticsearch-1fe300c1cd0f)
   2. work every notebook as document and label
   3. elasticsearch for search engine
   4. rendering
   5. [similar thought](https://blog.ouseful.info/2018/05/22/more-thoughts-on-jupyter-notebook-search/)