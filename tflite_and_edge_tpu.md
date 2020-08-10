# tflite

* tnesorflow的瘦身版本 - 主要用於推論
* 基本上會在tensorflow.lite模組中，主要會使用到的有Interpreter以及TFLiteConverter
* 官方說明 - [ML for Mobile and Edge Devices - TensorFlow Lite](https://www.tensorflow.org/lite?hl=zh-cn)
  + 可以看到介紹，stackoverflow，以及usecase
  + [官方文件 Get started with TensorFlow Lite](https://www.tensorflow.org/lite/guide/get_started)
  + [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert) - 例子很少，加減看
  + [TensorFlow Lite and TensorFlow operator compatibility](https://www.tensorflow.org/lite/guide/ops_compatibility)
* [code-base basically C++](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite)
* [TensorFlow Lite概述：转换器、解释器、XLA和2019年路线图 贊同80+, 2019, July](https://zhuanlan.zhihu.com/p/74085789)

## tf-lite主要做了什麼事?

# edgetpu

* [開箱文](usb_accelator.md)

* 可以將 `tflite` 模型compile成edgetpu support的形式，那麼就可以使用edgetpu做推論，需要使用[edgetpu compiler](https://coral.ai/docs/edgetpu/compiler/)，[posenet](https://github.com/google-coral/project-posenet)中的BasicEngine有python接口
* can edge TPU run two model at the same time?
  + [Background] yes, but it might be slow, because edgetpu cache the model parameters in edgetpu memory, which enabling fast inference speed. when running a second model if we want, requires swapping the model parameter data in RAM，
    - check official doc [Run multiple models with multiple Edge TPUs](https://coral.ai/docs/edgetpu/multiple-edgetpu/#performance-considerations)
  + [Possible solution] co-compiling your models, which allows the Edge TPU to store the parameter data for multuple models in RAM together, which means it typically works well onlu for small models
    - [check official doc](https://coral.ai/docs/edgetpu/compiler/#parameter-data-caching)
    - [check stackoverflow discussion](https://stackoverflow.com/questions/58494469/edgetpu-compiler-how-to-combine-two-tflite-models)

# edge-tpu API flow

* 若API flow的推論速度或推論精確度不符合預期，那麼就需要考慮自己做model puring，distilling，**參考 README中的 Model Compression章節**

* `keras / tensorflow` (pb file) -> `tflite` (.tflite) -> `edgetpu_compiler` (.tflite)
  + example posenet_mobilenet_v1_edgetpu.tflite 1.3M
