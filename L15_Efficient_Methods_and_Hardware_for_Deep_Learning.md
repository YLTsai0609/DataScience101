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

[TBC, 14.04](https://www.youtube.com/watch?v=eZdOkDtYMoo&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=15)****

# Other Resource
[Learning both Weights and Connections for Efficient
Neural Networks by Song Han 2015, 2336](http://papers.nips.cc/paper/5784-learning-both-weights-and-connections-for-efficient-neural-network.pdf)