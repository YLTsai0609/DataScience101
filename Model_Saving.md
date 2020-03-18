# Keras
## 簡易版 : [看Keras老中的翻譯](https://keras.io/zh/models/about-keras-models/?fbclid=IwAR158EDBV0UpPWeYlVQH6S-OLWAYnvLm8Dftm6e8v4sVE8QzxZ96-j-2ejE)
重點Highlight
* Keras提供兩種模型，Sequential以及Coustom
* `model.get_config()`，model config會給出dict，可以呼叫`from_config`來衝新建立模型
* `get_weights(), ser_weights()` : 從numpy數組中建立權重
* `to_json(), model_from_json`:返回模型結構的json，**注意，沒有包含權重**
* 同樣道理我們有`to_yaml(), model_from_yaml()`
* `save_weights(), load_weights()`整個儲存為HDF5文件(某種序列化)

## [詳細版 Keras FAQ](https://keras.io/getting-started/faq/?fbclid=IwAR0HEHKuCEAvzAiUCcldLBV3gNe0BLTjAJDpZZc6TDecH3UPK2Q10IiPe7o)

* 全部存(結構+權重+優化器狀態)
* 只存模型結構
* 只存權重
* 處理客製化模型
 
重點Highlight
* 不推薦用pickle或是cPickle

### whole models(結構+權重+優化器狀態)
* 儲存為`HDF5`
* 模型架構，並且允許重建模型
* 模型權重
* 訓練時資料(loss以及optimizer)
* optimizer狀態(讓你可以繼續train)

```
from keras.models import load_model

model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')
```

### 只存架構

```
# save as JSON
json_string = model.to_json()

# save as YAML
yaml_string = model.to_yaml()
```

```
# model reconstruction from JSON:
from keras.models import model_from_json
model = model_from_json(json_string)

# model reconstruction from YAML:
from keras.models import model_from_yaml
model = model_from_yaml(yaml_string)

```

### 只存權重
```
model.save_weights('my_model_weights.h5')
model.load_weights('my_model_weights.h5')

# 如果要load進不同的結構
model.load_weights('my_model_weights.h5', by_name=True)

```

例如說你增加了新的層

```
"""
Assuming the original model looks like this:
    model = Sequential()
    model.add(Dense(2, input_dim=3, name='dense_1'))
    model.add(Dense(3, name='dense_2'))
    ...
    model.save_weights(fname)
"""

# new model
model = Sequential()
model.add(Dense(2, input_dim=3, name='dense_1'))  # will be loaded
model.add(Dense(10, name='new_dense'))  # will not be loaded

# load weights from first model; will only affect the first layer, dense_1.
model.load_weights(fname, by_name=True)

```

### 處理客製化模型

* 如果你定義了一些特殊的層或是class或是funciton，那你可以要加上一些參數

```
from keras.models import load_model
# Assuming your model includes instance of an "AttentionLayer" class
model = load_model('my_model.h5', custom_objects={'AttentionLayer': AttentionLayer})

```

或是這種方式

```
from keras.utils import CustomObjectScope

with CustomObjectScope({'AttentionLayer': AttentionLayer}):
    model = load_model('my_model.h5')

```

特殊的結構也可以這樣來載入

```
from keras.models import model_from_json
model = model_from_json(json_string, custom_objects={'AttentionLayer': AttentionLayer})

```

# Tensorflow
[參考官網](https://www.tensorflow.org/tutorials/keras/save_and_load)

### checkpoints during training
* Train太久，存起來改天train就會用到，會有一個callback物件叫做`tf.keras.callbacks.ModelCheckpoint`，callback是一個可以傳進model fit 的物件

```
checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

# Create a callback that saves the model's weights
cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

# Train the model with the new callback
model.fit(train_images, 
          train_labels,  
          epochs=10,
          validation_data=(test_images,test_labels),
          callbacks=[cp_callback])  # Pass callback to training

# This may generate warnings related to saving the state of the optimizer.
# These warnings (and similar warnings throughout this notebook)
# are in place to discourage outdated usage, and can be ignored.
```

剛剛的行為會產生ckpt集合

```
checkpoint           cp.ckpt.data-00001-of-00002
cp.ckpt.data-00000-of-00002  cp.ckpt.index
```

### 整個model存

* 序列化，然後存起來，會存成一個pb檔
```
# Create and train a new model instance.
model = create_model()
model.fit(train_images, train_labels, epochs=5)

# Save the entire model as a SavedModel.
!mkdir -p saved_model
model.save('saved_model/my_model') 
```

!ls saved_model/my_model

```
my_model
assets  saved_model.pb  variables
```

* 或是存成HDF5檔案(也是一種標準序列化)

```
# Create and train a new model instance.
model = create_model()
model.fit(train_images, train_labels, epochs=5)

# Save the entire model to a HDF5 file.
# The '.h5' extension indicates that the model should be saved to HDF5.
model.save('my_model.h5') 

```
# Pytorch

# Other