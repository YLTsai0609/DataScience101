# Resource
https://www.youtube.com/watch?v=eZdOkDtYMoo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=15

<img src='./images/effDL_1.png'></img>

<img src='./images/effDL_2.png'></img>

<img src='./images/effDL_3.png'></img>

<img src='./images/effDL_4.png'></img>

<img src='./images/effDL_5.png'></img>

<img src='./images/effDL_6.png'></img>

<img src='./images/effDL_7.png'></img>

* dive to 4 parts 

# Hardware 101
## Device
<img src='./images/effDL_8.png'></img>

* GPU weak memory
* CPU weak single thread

## Number Rrpresentation

<img src='./images/effDL_9.png'></img>

<img src='./images/effDL_10.png'></img>

## Algorithm for Efficient Inference

### Network Puring

<img src='./images/effDL_11.png'></img>

<img src='./images/effDL_12.png'></img>

* 1986年第一次發表，現在被從新拿出來探討
* AlexNet -> 10x less connection with 6m

<img src='./images/effDL_13.png'></img>

<img src='./images/effDL_14.png'></img>

<img src='./images/effDL_15.png'></img>

<img src='./images/effDL_16.png'></img>

* CNN, RNN, LSTM also works!

<img src='./images/effDL_17.png'></img>

<img src='./images/effDL_18.png'></img>

<img src='./images/effDL_19.png'></img>

* QA  how do we deal with zero connections? - force them(the output) to zero
* QA how do you decide which weight to drop?
  * so very simple, sort all weight, small weights, drop it - maybe not, the figure show not exactly
  * QA any threshold that I decide?

<img src='./images/effDL_20.png'></img>

### Weight Sharing
* similar weights -> get it into one!
* details weight leads big model, reduce them, and might slightly release overfitting

<img src='./images/effDL_21.png'></img>

* using simple clustering method to do it, or just rule based
<img src='./images/effDL_22.png'></img>
<img src='./images/effDL_23.png'></img>
16 times saving!

* How to train this? - when we do BP, they are binind together

* trained quantization if we have centroids, groupby the gradient -> sum it to get quantization gradient

* add graident to previous centroids
<img src='./images/effDL_25.png'></img>
<img src='./images/effDL_26.png'></img>

* result
<img src='./images/effDL_27.png'></img>
<img src='./images/effDL_28.png'></img>
only sixteeen discrete number, means we can use four bits to represent

<img src='./images/effDL_29.png'></img>

* more bits, more precision weight, when we decrease to 4 bits, accuracy drop very fast on **conv and fc layer**

<img src='./images/effDL_30.png'></img>

* combine them together
* note that, if we do not have much time, do the SVD!

# Huffman Coding

<img src='./images/effDL_30.png'></img>

in short,
In-frequent weights : use more,
Frequent weights : use less

<img src='./images/effDL_31.png'></img>

<img src='./images/effDL_32.png'></img>

compression ratio 10x ~ 40x without accuracy decrease

# Compact model - training our own small model

<img src='./images/effDL_33.png'></img>

<img src='./images/effDL_34.png'></img>

we can do that! SqueezeNet + Deep Compression

* TODO - how squeeze work?

[TBC, 20.12](https://www.youtube.com/watch?v=eZdOkDtYMoo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=15)****

# Other Resource
[Learning both Weights and Connections for Efficient Neural Networks by Song Han 2015, 2336](http://papers.nips.cc/paper/5784-learning-both-weights-and-connections-for-efficient-neural-network.pdf)

[Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding by Song Han 2016, 3462](https://arxiv.org/pdf/1510.00149.pdf)