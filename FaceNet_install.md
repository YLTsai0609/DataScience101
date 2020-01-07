# FaceNet_install
* 關於Google在2015年發表的論文，[其github上的code](https://github.com/davidsandberg/facenet)，安裝時所遇到的一些坑
1. 一定要記得開一個虛擬環境 conda activate XXX，避免安裝多個tensorflow, scipy環境，導致路徑混亂
2. facenet還沒被打包成package, git到自己的home目錄，手動加入PYTHONAPTH
3. requirement.txt寫得不好，scipy需要在1.1.0版，scipy.misc才會有imread的attribute
```
tensorflow==1.7
# scipy 1.1.0 for misc.imread attribute
scipy==1.1.0
# numpy==1.16.1 for less tensorflow logging shit
numpy==1.16.1
scikit-learn
opencv-python
h5py
matplotlib
Pillow
requests
psutil
```
* [其餘大致上參考這裡, 2018, 11, 10](https://www.itread01.com/yqifx.html?fbclid=IwAR0J7KuuJENV7yla8LYsGMPVblIOsX_cbFFBx4SSEkMSFDpHqFC-QeBUuEw)
* 已解 cannot import facenet - 把下載facenet資料夾的地方加入PYTHONPATH
* [scipy has no attribute `imread`](https://stackoverflow.com/questions/49685160/regarding-attributeerror-module-scipy-misc-has-no-attribute-imread?fbclid=IwAR0eCVlIdKlHfv938TT-UrSl0a60HPozWM1BuGb9By6hEqvRLmrGqqrCGBE)
* model 路徑問題 - 使用 file, abspath, dirpath, Pathlib.Path 建立基於執行檔案來計算的絕對路徑