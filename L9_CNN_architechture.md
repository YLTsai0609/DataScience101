# Reousrce
Stanford University 
https://www.youtube.com/watch?v=DAOcjicFr1Y

# Deep Learning Frameworks
<img src='./images/cnna_1.png'></img>
<img src='./images/cnna_2.png'></img>

# CNN architectures
<img src='./images/cnna_3.png'></img>

# LeNet

<img src='./images/cnna_4.png'></img>

# AlexNet - the first large cnn
* beat rest of non-deep learning based method on imagenet
<img src='./images/cnna_5.png'></img>

* first layer $55 \times 55 \times 96$
* parameters $11 \times 11 \times 3 \times 96$ = 35K
* TODO feature map height? depends on how many filters you have in the layer =)
* Pooling layer $3 \times 3$ stride 2 output : $27 \times 27 \ times 96$
* parameters : 0
* first ues of ReLU

<img src='./images/cnna_6.png'></img>
<img src='./images/cnna_7.png'></img>

* the second just because lack of GPU memory, then splits it into two parts
* 55 x 55 x 96 -> 55 x 55 x 48 x 2(two GPUS)

<img src='./images/cnna_8.png'></img>

* result

<img src='./images/cnna_9.png'></img>

* still be used in transfer learning task

<img src='./images/cnna_10.png'></img>  

* QA why CNN beat all of them? - no idea, but it is the first deep learning based approach

# ZFNet - 2013 imagenet
<img src='./images/cnna_11.png'></img>
* ZFNet basically tuning hyperparameter like strid, # of filters, and so on

# trands

<img src='./images/cnna_12.png'></img>
8 layer -> 19 layer(VGG) -> 22 layer(GoogleNet) -> 152 layer (insane!)

# VGG
* small filters, deepper networks, catching more details :p
* also fewer params - which is interesting
<img src='./images/cnna_13.png'></img>  
<img src='./images/cnna_14.png'></img>
<img src='./images/cnna_15.png'></img>
<img src='./images/cnna_16.png'></img>

* 4 bytes is float32 representation
* 100M / image when doing forward pass during whole training
* 138M parameters(VGG 19), 60M(AlexNet)
* QA depth of network / depth of img (channel)
* QA when people design network, deeper based on what?
  * basically more computational resource, better result
  * you could use pooling layer to decrease the params - maybe check 李弘毅(Why Deep)
  * abc
* QA we don't need params them all right? - true, but we also do BP to update weights, means update them in memory is more efficient

<img src='./images/cnna_16.png'></img>

* Some complexity analysis

<img src='./images/cnna_17.png'></img>
* standard graph representation like 3x3 conv, 64, conv1-1(3x3 filter, 64 kernels)

<img src='./images/cnna_18.png'></img>

* some details
* fc7 is a good feature representation(may uesd in transfer learning)
* QA - localization / detection difference? only one object / multiple objects

# GoogleLent

<img src='./images/cnna_19.png'></img>

* New design - inception module
* no FC layer
* only 5M params 12x less than AlexNet

## Inception module
* local network topology

<img src='./images/cnna_20.png'></img>

* concatenate all filter outputs together depth-wise
* QA if we want to do this - computational exprensive

<img src='./images/cnna_21.png'></img>

<img src='./images/cnna_22.png'></img>

* such a lot of computation - google use dimension reduction before doing conv ops
* $f \times f$ then padding with zero
* QA what is $1 \times 1$conv?

<!-- <img src='./images/cnna_23.png'></img> -->

* under proper usage, 1x1 conv reduce depth to lowe of dimension!

<img src='./images/cnna_24.png'></img>
<img src='./images/cnna_25.png'></img>

* check the result! google called that bottleneck layer

<img src='./images/cnna_26.png'></img>

* QA what will we loss by appling 1x1 conv?
  * basically no idea, but it helps model works well

<img src='./images/cnna_27.png'></img>

<img src='./images/cnna_28.png'></img>

<img src='./images/cnna_29.png'></img>

<img src='./images/cnna_30.png'></img>

<img src='./images/cnna_31.png'></img> 

<img src='./images/cnna_32.png'></img> 

* 3 place to train, whole network, 2 axuxiliary at lower layers
* The reason is that it is a deep network, inject at middle layer could give more gradient to earlier layer, intesteing :P
* 22 layers
* QAs : are the auxiliary outputs actually useful for final classification?
  * they do average all theses for losses coming out, but basically not sure, might check it the paper
* QAs : in the bottleneck layer, is it possible to use other dimension reduction techinique?
  * yes you could do that, but 1x1 conv si really convininent here
* QAs : why do we need to inject gradient to earlier layer?
  * basically they have a gradient vanish problem even they use a ??? activation func?

<img src='./images/cnna_33.png'></img> 

<img src='./images/cnna_34.png'></img> 

# ResNet

<img src='./images/cnna_35.png'></img> 

* this network basically won evertying, COCO, ILSVRC...
* what happens when we contibue stacking deepper layers on a "plain" cnn?

<img src='./images/cnna_36.png'></img> 

* deeper network do more worse
* and it is not about overfitting, because in training error, they are still bad
* **then the creator has a hypothesis!**

<img src='./images/cnna_37.png'></img>

* deep network should perform at least as shallow network, copy shallow and the rest are identify function

* ok, how could we design our model more easier

<img src='./images/cnna_38.png'></img>

* QAs : when you use the word residual, what are you talking about exactly?

* $F(x)$ a transfomation of $x$
* suppose $H(x)$ is transfomation + input, which is $H(x) = F(x) + x$
* we want to learning something like $H(x)$ which is hard to learning
* how about we learn it partially? we learning $F(x)$
* then plus x, we get $H(x)$
* so the residual means $F(x)$

* QAs : in practice, do we still learning a weight?
  * ????? can't tell
* QAs: why learning residual is more easiler?
  * just their hypothesis, and it worked well, it also imply the most layer is close to the identity$X$
  * it is not proving anything, just initution and hypothesis
* QAs : how people try other ways to combine input layer and output layer?
  * it's a active area, and basically she don't know

<img src='./images/cnna_39.png'></img>
<img src='./images/cnna_40.png'></img>
<img src='./images/cnna_41.png'></img>

* they also use 1x1 conv to control computational complexity
<img src='./images/cnna_42.png'></img>
<img src='./images/cnna_43.png'></img>
<img src='./images/cnna_44.png'></img>

* beat human, human metric came from 李飛飛lab的研究生，他花了一整週....

<img src='./images/cnna_45.png'></img>

* all right, they are main classfication network to use

# Compareing complexity

<img src='./images/cnna_46.png'></img>
<img src='./images/cnna_47.png'></img>
<img src='./images/cnna_48.png'></img>
<img src='./images/cnna_49.png'></img>

<img src='./images/cnna_50.png'></img>
* VGG is heavy!

* inference time

<img src='./images/cnna_51.png'></img>
<img src='./images/cnna_52.png'></img>

# Other architectures to konw

[TBC 36:01](https://www.youtube.com/watch?v=DAOcjicFr1Y)

# Other Resource
* [if gary still coming.... show him this](https://brohrer.mcknote.com/zh-Hant/how_machine_learning_works/how_convolutional_neural_networks_work.html)
* [Why we need top5 error and top1 error in imageclassfication error?](https://www.zhihu.com/question/36463511)
* [Deep Residual Learning for Image Recognition, 2016, 48669](http://openaccess.thecvf.com/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf)
* [AN ANALYSIS OF DEEP NEURAL NETWORK MODELS
FOR PRACTICAL APPLICATIONS, 2016, 543](https://arxiv.org/pdf/1605.07678.pdf)