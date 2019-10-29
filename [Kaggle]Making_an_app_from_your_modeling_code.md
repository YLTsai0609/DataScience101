# Making_an_app_from_your_modeling_code
Making_an_app_from_your_modeling_code | Kaggle 重點節錄
* [Kaggle NoteBook](https://www.kaggle.com/rtatman/careercon-making-an-app-from-your-modeling-code)
* [講者 - Rachael Tatman (Data Scientist at Kaggle)](https://www.kaggle.com/rtatman/kernels?sortBy=dateCreated&group=everyone&pageSize=20&userId=1162990)
# Quick Dive
* Make it work
* Make it pretty
* Make it portable
* A Flask App
# Make it work
* 要能夠重頭到尾能夠跑
# Make it pretty
* 把它寫得漂亮一點，用函數包起來，input, output 資料型態，註解寫好，整理的其他後端背景看得懂的樣子
# Make it portable
* Load your model and make predictions!
# A Flask App
    * serve.py
    * app.py
# Make it work, Make it pretty

你已經會了 =) 

# Make it portable
##  saving model
### Library-specific methods for saving models
* For Tensorflow and keras, using `model.save_weights()`, read using `model.load_weights`, by defult, your model will be saved as a **HDF5** file. [more info about tensorflow model](https://www.tensorflow.org/tutorials/keras/save_and_load#manually_save_weights), 
also you can searching about pytorch, XGBoost, lightGBM
### If there's no library-specific technique
* [pickle, serialized data format for python](https://docs.python.org/2/library/pickle.html)
* [your model built as one or more numpy array, using HDF5](https://www.christopherlovell.co.uk/blog/2016/04/27/h5py-intro.html)
* 記得, pickles可以處理更多的資料型態
* pickle的一些麻煩，python版本不同可能會無法載入, 如果真的遇到, 可以使用sklearn的joblib
* 最好記住python的版本，寫在requirements裡面
* pickle的其他麻煩，pickle檔案蠻容易被hack, 這點要找找解法, 如果需要的話
# A Flask App
`serve.py`
* 把model load近來
* 寫一個function, 叫做 get_api, return model function
```
from flashtext.keyword import KeywordProcessor
import pickle

# Function that takes loads in our pickled word processor
# and defines a function for using it. This makes it easy
# to do these steps together when serving our model.
def get_keywords_api():
    
    # read in pickled word processor. You could also load in
    # other models as this step.
    keyword_processor = pickle.load(open("processor.pkl", "rb"))
    
    # Function to apply our model & extract keywords from a 
    # provided bit of text
    def keywords_api(keywordProcessor, text, span_info=True): 
        keywords_found = keywordProcessor.extract_keywords(text, span_info=True)      
        return keywords_found
    
    # return the function we just defined
    return keywords_api

```
`app.py`

```
import json
from flask import Flask, request
from serve import get_keywords_api

# create an instance of Flask
app = Flask(__name__)

# load our pre-trained model & function
keywords_api = get_keywords_api()

# Define a post method for our API.
@app.route('/extractpackages', methods=['POST'])
def extractpackages():
    """ 
    Takes in a json file, extracts the keywords &
    their indices and then returns them as a json file.
    """
    # the data the user input, in json format
    input_data = request.json

    # use our API function to get the keywords
    output_data = keywords_api(input_data)

    # convert our dictionary into a .json file
    # (returning a dictionary wouldn't be very
    # helpful for someone querying our API from
    # java; JSON is more flexible/portable)
    response = json.dumps(output_data)

    # return our json file
    return response
```