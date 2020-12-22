# CPU bounded

Wall Time : 經過總時間

CPU Time : 計算機的實際計算時間

中間的差異就是等待，或是架構上，硬體溝通上造成的時間差

## single thread

``` Python
import time

start = time.time()

delta_t = (time.time() - start) * 1000

print(f'your processing {delta_t:.2f}')
```

## multi thread

1. 為何單線程的測量方法多線程不能用?
2. 在多線程的程式中進行測量是可能的嗎?
