# Advancing 3D Multi-Object Tracking: Evaluation Metrics and A Baseline
* 2019, July
* X Weng, K Kitani
* citation 9
* [github](https://github.com/xinshuoweng/AB3DMOT)
* [paper](https://arxiv.org/abs/1907.03961)

# 摘要
3D realtime 多物體追蹤在現實生活中是一個非常重要的應用，像是自動駕駛以及機器人輔助，近期的3D MOT研究中傾向發展更準確的系統，較少關注計算成本以及算法複雜性，所以我們提出了一個簡單且足夠準確的ream time 3D 多目標追蹤系統，我們使用3D資料 - LiDAR point cloud，使用**off-the-shelf 3D object detector**來獲得3D的bounding box，，接著再加上3D Kalman filter and Hungarian algorithm來進行物體追蹤，雖然我們的baseline系統只是把幾個標準模塊組合起來，但我們得到了當前最好的成果(state-of-the-art result)，為了評估我們的系統，我們把KITTI 2D MOT的評估方式延伸到了3D上，當然，我們加上了一些metrics，而我們的3D MOT系統在這樣的評估標準下也達到了當前最好的成果，還有一項令我們驚訝的地方，我們的系統並沒有使用任何2D data作為input，我們整個系統放到offical KITTI 2D MOT競賽中，我們還是得到了第2名，對了，我們的3D MOT method可以跑到214.7FPS，這是當前最快的3D MOT系統了。

# 作者
### First
Xinshuo Weng - 翁新碩
* [google scholar](https://scholar.google.com/citations?user=dthSEsoAAAAJ&hl=en)
* 發的期刊非常多，顯然Lab很大，大家互掛
* Carnegie Mellon University - 卡內基·梅隆大學
* Ph.D., Robotics Institute, School of Computer Science
* [github](https://github.com/xinshuoweng)
* 看github頭像，應該是個動漫宅
* [facebook](https://www.facebook.com/wengxinshuo)
* 確定是個中國人，之前在facebook app實習過，現在是PhD

### Second

