# Face3D
## 背景
* 一但了解3D的face相關的研究以及應用，就有機會和3D動畫Team合作，協助量產重複性高的工作，提升產能
* 也能夠了解必逼真的臉部辨識，以及壹些活體檢測的知識
## Research Field
* [Apple FaceID的紅外線trick](https://pttnews.cc/32c4b26e80?fbclid=IwAR25EBWsRuwjuO3pdzx-0FdDKSbgUiJcP9T33ZoVZChcQofc-zvcf_g5NEg)
* [Face3D code and papers 1k+ stars](https://github.com/YadiraF/face3d)
* [Facenet 門禁系統 know how blog](https://blog.cavedu.com/2019/03/05/%E8%87%89%E9%83%A8%E8%AD%98%E5%88%A5%E6%89%93%E5%8D%A1%E9%90%98-%E6%A8%B9%E8%8E%93%E5%96%AE%E6%A9%9F%E7%89%88/
  * 雙camera - 確保不是平面假臉
  * Laplace threshold - 防止過於模糊的照片擾亂辨識結果
  * Server Side設計，IO密集 - 對樹莓派硬碟不好，容易壞