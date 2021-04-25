# Reousrce
Stanford University 
https://www.youtube.com/watch?v=6SlgtELqOWc&list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv&index=8

[all the slides](http://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture8.pdf)


<img src='./images/dls_1.png'></img>
<img src='./images/dls_2.png'></img>
<img src='./images/dls_3.png'></img>
<img src='./images/dls_4.png'></img>
<img src='./images/dls_5.png'></img>

# GPU
Graphics Processing Uint, Graphics card, originally render computer graphics, especially around games

<img src='./images/dls_6.png'></img>

* almost NVIDIA in deep learning XD
* good solution when training...

<img src='./images/dls_7.png'></img> 

* CPU sharing memory with system
* GPU have their own memory(their own caching system)
* convolution is a matrix dot problem

<img src='./images/dls_8.png'></img>

* actually really hard to using write cuda, then they are higher-level APIs
* cudnn - almost all the operation in deep learning
* OpenCL
* in fact, never write any cuda code in your project, so. 

<img src='./images/dls_9.png'></img>

* commonly, 60x - 70x
* benchmark like that basically unfair, he might not tuning good performance on CPU, this is just a out-of-box benchmark like, tensorflow cpu vs tensorflow gpu, torch cpu vs torch gpu


<img src='./images/dls_10.png'></img>

* cudnn boost about 2x ~ 3x, make sure you're using cudnn!

<img src='./images/dls_11.png'></img>

<img src='./images/dls_12.png'></img>

* **might be a bottleneck when reading data and tranferring to GPU**

* most general solution is multi-processing data io
  * basically like reading data into quene
  * feed queue into gpu for train

* 2016...
<img src='./images/dls_13.png'></img>

* 2017...

<img src='./images/dls_14.png'></img>

* intesting things is, new generation library badically come from industry

<img src='./images/dls_15.png'></img>

# hello world about computational graph

<img src='./images/dls_16.png'></img>

# high level of tensorflow wrapper

<img src='./images/dls_17.png'></img>

<img src='./images/dls_18.png'></img>

<img src='./images/dls_19.png'></img>

# Pytorch

<img src='./images/dls_20.png'></img>

<img src='./images/dls_21.png'></img>

<img src='./images/dls_22.png'></img>

# high level wrapper pytorch nn
<img src='./images/dls_23.png'></img>

# Custom
<img src='./images/dls_24.png'></img>

# DataLoaders!

<img src='./images/dls_25.png'></img>

# Pretrained MODELS

<img src='./images/dls_26.png'></img>

# Visualization

<img src='./images/dls_27.png'></img>

# Static vs Dynamic Graph

<img src='./images/dls_28.png'></img>

<img src='./images/dls_29.png'></img>

<img src='./images/dls_30.png'></img>

## Conditional
<img src='./images/dls_31.png'></img>

## Loops

<img src='./images/dls_32.png'></img>

#  Caffe

<img src='./images/dls_33.png'></img> 

<img src='./images/dls_34.png'></img> 

# advice

<img src='./images/dls_35.png'></img> 

<img src='./images/dls_36.png'></img> 


