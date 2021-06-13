[Ref I](https://www.youtube.com/watch?v=utk3EnAUh-g)

[Ref II](https://www.youtube.com/watch?v=xrlbLPaq_Og&t=985s)

# Smaller Model

<img src='./images/mc_23.png'></img>

<img src='./images/mc_24.png'></img>

Lower lantency and Privacy.

## Neywork Pruning

Prune the useless parameters.

<img src='./images/mc_25.png'></img>

1. train a network.
2. measure the importance of a weights by
   1. absolute values
   2. life long?
3. measure the importance of a neuron
   1. mrsure the number of times it wasn't zero on a given dataset.
4. remove
5. fine-tune the network.
6. start from 2 --> 5 evaluate the importance

<img src='./images/mc_26.png'></img>

<img src='./images/mc_27.png'></img>




### what's the difference when we pruning the weights/neuron?

### Weights

<img src='./images/mc_27.png'></img>

<img src='./images/mc_28.png'></img>

Hard to implement, hard to speedup.

after experiment, 95% weights are useless, but the wired shape network is even slower!

<img src='./images/mc_29.png'></img>

### Neuron

<img src='./images/mc_30.png'></img>

QA : 
1. inefficency is the package impelemtation issue, not a algorithm issue.
   1. yes, it is.
2. instread of getting the network smaller, how about getting the network bigger and bigger?
   1. after experiemnt, answer is no. we'll check it out below.

## Why Prunning?

instread of getting the network smaller, how about getting the network bigger and bigger?

Why big network is easier to train?

Lottery Ticket Hypothesis.(Best paper award @2019 ICLR)

<img src='./images/mc_31.png'></img>

When we train a Large network, we are training a lot of sub-network.

Not all of the subnetwork trained successfully.

But large network success when only one subnetwork successed!

 
How to design the experiement?

<img src='./images/mc_32.png'></img>

Deconstructing Lottery Tickets:


<img src='./images/mc_33.png'></img>

we found that, it is possible a initilize parameter is good enough, we even don't need to train it.

So called Weight-Agnoise Network.


<img src='./images/mc_34.png'></img>

<img src='./images/mc_35.png'></img>

打臉大樂透假說

just run more epoch for smaller network.

Well, it's still a hypothesis.



# Knowledge Distillation

<img src='./images/mc_3.png'></img>

Original Network : Teacher Network

We want : Stdudent Network

Learning the trachers answer.

Minimize the cross entropy between student predcition and teacher's answer.

QA : 

1. When tracher goes wrong? 
   1. Learn it anyway.
2. Why not we just train a small network?
   1. learning toward teacher leads better result.
   2. tracher network provide addtional information(output a distribution (soft label))
   3. student network even can learn the unseen category by soft label prediction.

We even can learn a student complex ensemble network.

<img src='./images/mc_4.png'></img>

Temperature for softmax $y_i = \frac{e^{y_{i}/T}}{\sum_{j} e^{y_{j}/T}}$

<img src='./images/mc_5.png'></img>

when $T \rightarrow \infin$, student network learn nothing.

# Parameter Quantization

1. less bits
   
64 bits --> 32 bits --> 16 bits --> 8 bits --> binary !?

2. weight clustering --> only need 2 bits
   1. you can clustering when training or post-training.

3. represent frequent clutser by less bits, represent rare by more bits - Huffman encoding

<img src='./images/mc_6.png'></img>

4. Binary weight

<img src='./images/mc_7.png'></img>

Binary weights possible get good result...

<img src='./images/mc_8.png'></img>


# Architecture Design(Depthwise Separable Convolution)

Review Standard CNN, filter is a cube instead of retangle.

<img src='./images/mc_9.png'></img>

Depthwise - convolution by channel 

<img src='./images/mc_10.png'></img>

pointwise convulition - to capture cross channel correlation.

<img src='./images/mc_11.png'></img>

Parameters fraction : 

<img src='./images/mc_12.png'></img>

$O$ is big in general, like $O = 256$, however, if you are using kernel size $k=3, k=5$, you will get a $\frac{1}{9}$ or $\frac{1}{25}$ small network.

## Why it work? Low rank approximation

consider a dense layer.

<img src='./images/mc_13.png'></img>

we basically apply matrix factorization in NN.

tadeoff, $W$ will br limited.

$rank(W) \leq k$

<img src='./images/mc_14.png'></img>

<img src='./images/mc_15.png'></img>

<img src='./images/mc_16.png'></img>

They're very famous!

MobileNet, ShuffleNetm GhostNet

# Dynamic Computation

The network adjust the computation it need.

e.g. : 

1. different devices.
2. high/low battery.

Q : Why don't we prepare a set od models? (storage consuming.)

## Dynamic Depth

<img src='./images/mc_17.png'></img>

<img src='./images/mc_18.png'></img>

MSDNet

<img src='./images/mc_19.png'></img>

## Dynamic Width

<img src='./images/mc_20.png'></img>

## Computation based on Sample Difficultyu.

<img src='./images/mc_21.png'></img>


# Conclusion

You can use them all

<img src='./images/mc_22.png'></img>
