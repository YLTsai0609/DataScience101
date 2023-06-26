# Steps

1. 該程式碼要解決的問題為何
   1. stakeholder
   2. 場景
2. 方法論驗證
   1. 相關指標
   2. 復現方式
3. 工程實作
   1. 時間區間取樣是否合理 (vs 計算負擔)
   2. task --> simple responsibility principle
   3. outflow data schema, inflow data schema
   4. task, outflow - idempotency (reproducible result)
   5. 是否有冗余的 join
   6. 具有風險的寫法
      1. e.g. size(collect_set()) - memory intensive
      2. 大表 join 大表
      3. user defined function 的濫用
      4. 容易產生 exception 導致失敗
   7. 命名
      1. method : v_n
      2. variable : a_with_b
   8. 資料 gaurd
      1. 重要資料是否前面有掛 assert