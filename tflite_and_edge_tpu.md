# tflite
* tnesorflow的瘦身版本 - 主要用於推論
* 基本上會在tensorflow.lite模組中，主要會使用到的有Interpreter以及TFLiteConverter
* 官方說明 - [ML for Mobile and Edge Devices - TensorFlow Lite](https://www.tensorflow.org/lite?hl=zh-cn)
  * 可以看到介紹，stackoverflow，以及usecase
  * [官方文件 Get started with TensorFlow Lite](https://www.tensorflow.org/lite/guide/get_started)
  * [TensorFlow Lite converter](https://www.tensorflow.org/lite/convert) - 例子很少，加減看
  * [TensorFlow Lite and TensorFlow operator compatibility](https://www.tensorflow.org/lite/guide/ops_compatibility)
* [code-base basically C++](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite)
* [TensorFlow Lite概述：转换器、解释器、XLA和2019年路线图 贊同80+, 2019, July](https://zhuanlan.zhihu.com/p/74085789)

# edgetpu
* 可以將`tflite`模型compile成edgetpu support的形式，那麼就可以使用edgetpu做推論，需要使用[edgetpu compiler](https://coral.ai/docs/edgetpu/compiler/)，[posenet](https://github.com/google-coral/project-posenet)中的BasicEngine有python接口