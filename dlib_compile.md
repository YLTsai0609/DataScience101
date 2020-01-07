# dlib_compile
# 背景
因為使用conda install，似乎與[Speed up Dlib's Facial Landmark Detector](https://www.learnopencv.com/speeding-up-dlib-facial-landmark-detector/)中說明到的，該實作在Paper中能夠達到1ms的速度有巨大的落差
因此考慮自己編譯，並驗證是否有SSE2的config加速下有所差別，搭配[這篇](https://www.learnopencv.com/install-dlib-on-ubuntu/?fbclid=IwAR35ZGCeVf2DGX_TBlUWH7MCVnAaT3Yr5OGsSyK8rWBqZccjtTxlz1t-Lnc)
來使用cmake .. -DUSE_SSE4_INSTRUCTIONS=ON使CPU加速
`SSE4 is the next fastest and is supported by most current machines.`
其中還安裝了 `sudo apt-get install libopenblas-dev liblapack-dev`
然後沒辦法繼續  
make install了
因為沒有make的target
* 目標 - create a shared library for dlib
* [check create a shared library for dlib](https://stackoverflow.com/questions/33996361/create-a-shared-library-for-dlib/33997825?fbclid=IwAR1OBaS8uaf8c-I-D3BQDWQO044rXXBkyvLye9sYfRoTlUBUoAAKTWP8ixs#33997825)
# After Compile C++ library
# Compile python module
