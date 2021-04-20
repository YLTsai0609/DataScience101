# Ref

Paper : 
[Hidden Technical Debt in Machine Learning Systems 2015, google 450+ citations](https://web.kaust.edu.sa/Faculty/MarcoCanini/classes/CS290E/F19/papers/tech-debt.pdf)


Best Practice : [Best practice for ml in google](files/rules_of_ml.pdf)

* The source actually comes from [google machine learning crash course](https://developers.google.com/machine-learning/guides/rules-of-ml)


# Notes

## Best Practives for ML Engineering

The best practice in machine learning from around Google.

Sections

0. Overview
1. Before ML
2. ML Phase I - Your First Pipeline
3. ML Phase II - Feature Engineering
4. ML Phase III - Slowed Growth, Optimization Refinement, and Complex Model

### Overview

Most of the problems you will face are, in fact, **engineering problems**. Even with all the resource of a great ML export, most od the gain come from great feature, not great ML algorithms.

So the approach is 

1. make sure your pipeline is solid end to end.
2. start with a reasonable objective.
3. add common-sense feature in a simple way.
4. make sure that your pipeline stats solid.

This approach will makes lots of money and make lot of people happy for a long peroid of time.

Diverge from this apporach only when there are no more simple tricks to get you any farther. Adding complexity slow future releases.

Once you've exhausted the simple tricks, cutting-edge ML might indeed be in your future.

### Before ML

#### **R1 Don't be afraid to launch a product without ML**

1. ML is cool, but it requires data.
2. If you think ML will give you a 100% boost, heuristic will grt you 50% of the way there.
3. **Example 1 :** Ranking apps in an app marketplaces.
   1. install rate
   2. number of installs
4. **Example 2 :** Detecting Spam 
   1. filter out publishers that have sent spam before.
5. (add) Use heuristic, think about where is the data at the same time. even hyberid two approach to achieve better performance.
6. (add) **Example 3 :** recommendation systems
   1. popularity recommendation
   2. popularity with category recommendation
   3. the newest content which your following

#### **R2 First, design and implement metrics.**

1. It's easier to gain pernission from the system's users.
2. If you think that something might be a concern in the future, it's better to get historical data now.
3. If you design your system with metric instrumentation in mind, things will go better for you in the future. Specifically, you don't want to find yourself grepping for strings in logs to instrument your metrics.
4. You will notice what things change and what stays the same. 
5. Google Plus team measures 
   1. expands per read
   2. reshares per read(轉貼)
   3. plus-one per read
   4. comments per read
   5. reshare per user
   6. comments per user
    Which they use in computing the goodness of a post at serving time.

6. **Example 1 :** Directly optimize one-day active users. However, during your early manipulations of the system, you may notice that dramatic alterations of the user experience don’t noticeably change this metric

Notice a problem? Add a metric to track it.

Excited about some quantitative change on the last release? Add a metric to track it.

#### **R3 Choose ML over a complex heuristic**

A simple heuristic can get your product out the door.

A complex heuristic is **unmaintainable**. 

Once you have data and a basic idea of what you are trying to accomplish. move on to machine learning!

As in most software engineering tasks, you will want to be contantly updating your approach, whether it is a heuristic or a machine-learned model, and you will find that the machine learned-model is easier to update and maintain(See Rule#16)

### ML Pahse I: Your First Pipeline

### Monitoring
In general, practice good alerting hygiene, such as making alerts actionable and having a dashboard page.

#### **R8 Know the freshness requirements of your system.**


How much does performance degrade if you have a model?

a day/week/quarter/year old?

This information can help you to understand the priorities of your monitoring. If you lose 10% of your revenue if the model is notupdated for a day. it makes sense to have an engineer watching it continuously.

**Most ad serving systems have new advertisements to handle every day, and must update daily.**

Example : if ML model for Google Play Search is not updated, it can have an impact on revenue in under a month.

Also notice that freshness can change over time. especially when feature columns are added or removed from your model.




### ML Pahse II: Feature Engineering

### ML Phase III: Slowed Growth, Optimization Refinement, and Complex Models

#### **R16 Plan to launch and iterate**

Don't expect that the model you are working on now will be the last one that you will launch, or even that you will ever stop launching models. Thus consider whether the complexity you are adding with this launch will slow down futher launches.

Many team have launched a model **per quarter or more for years**. There are 3 basic reseaons to launch new models :

1. you are coming up with new features
2. you are tuning regulization and combining old features in new ways.
3. you are tuning the objective.

So, as you build your model, think about 

1. how easy it is to add or remove or recombine features
2. how easy it is to create a fresh copy of the pipeline and verify its correctness.
3. wherther it is possible to have two or three copies running in parallel