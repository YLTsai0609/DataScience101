# Ref

Best Practice : [Best practice for ml in google](files/rules_of_ml.pdf)

The source actually comes from [google machine learning crash course](https://developers.google.com/machine-learning/guides/rules-of-ml)


Total rules : 43


# Sections

0. Overview
1. Before ML
2. ML Phase I - Your First Pipeline
   1. Monitoring
   2. Your First Objective
3. ML Phase II - Feature Engineering
   1. Human Analysis of the system
   2. Training-Serving Skew
4. ML Phase III - Slowed Growth, Optimization Refinement, and Complex Model

# Overview

Most of the problems you will face are, in fact, **engineering problems**. Even with all the resource of a great ML export, most ad the gain come from great feature, not great ML algorithms.

So the approach is 

1. make sure your pipeline is solid end to end.
2. start with a reasonable objective.
3. add common-sense feature in a simple way.
4. make sure that your pipeline stats solid.

This approach will makes lots of money and make lot of people happy for a long peroid of time.

Diverge from this apporach only when there are no more simple tricks to get you any farther. Adding complexity slow future releases.

Once you've exhausted the simple tricks, cutting-edge ML might indeed be in your future.

# Before ML - 3 rules

## **R1 Don't be afraid to launch a product without ML**

1. ML is cool, but it requires data.
2. If you think ML will give you a 100% boost, heuristic will get you 50% of the way there.
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

## **R2 First, design and implement metrics.**

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

## **R3 Choose ML over a complex heuristic**

A simple heuristic can get your product out the door.

A complex heuristic is **unmaintainable**. 

Once you have data and a basic idea of what you are trying to accomplish. move on to machine learning!

As in most software engineering tasks, you will want to be contantly updating your approach, whether it is a heuristic or a machine-learned model, and you will find that the machine learned-model is easier to update and maintain(See Rule#16)

# ML Pahse I: Your First Pipeline - 4 rules

Focus on your infrastructure for your first pipeline.

While it's fun to think about all the imaginative ml you sre going to do, it will be hard to figure out what is happening if you don't first trust your pipeline.

## **R4 Keep the first model simple and get the infrastructre right**

The first model provides the biggest boost to your product, so it doesn't need to be fancy.

But you will run into many more infrastructure issues than you expect.

Before anyone can use your fancy new ML system. you have to determine:

1. How to get examples to your learning algorithm.
2. A first cut to what "good" and "bad" mean to your system.
3. How to integrate the model into your application. apply the model live or pre-compute the model on examples offline and store the result in a table.

E.g. Pre-classify web pages and store the result in a table, but classify chat messages live.

Choosing simple feature makes it easier to enusre that.

1. The feature reach your learning algo correctly.
2. The model learns researonable weights.
3. The features reach your model in the server correctly.

Onces you have a system that does these 3 things reliably, you have done most of the work.

Your simple model provides you with baseline metrics and a baseline behavior that you can use to test more complex models.


## **R5 Test the infra indenpendently from the machine learning**

Make sure the infra is testable, and that the learing parts of the system are encapsulated(封裝好的) so that you can test you can test everything around it.

Specifically,

1. Test getting data into algorithm.
2. Check the feature creation shcema is expected.
3. check your data match the data privacy permits.
4. Test getting models out of the training algorithm. Make sure that the model in your training environment gives the same score as the model in your sercing environment(kind of sanity check) - for deployment specifically.

ML has an element of unpredictabilty, so make sure that you have tests for the code for creating examples in training and serving, and that you can load and use a fix model during serving.

**R6 Be careful about dropped data when copying pipelines**

Often we careate pipeline by coping an existing pipeline(i.e. [cargo cult programming](https://zh.wikipedia.org/wiki/%E8%B4%A7%E7%89%A9%E5%B4%87%E6%8B%9C%E7%BC%96%E7%A8%8B)). **And the old pipeline drops data that we need for the new pipeline**

E.g. 

1. A hot article recommender - drop older post - because it is trying to rank fresh posts.

This pipeline was cpoied to use for Content-based item recommender, where all articles contents matter.

**R7 Turn heuristics into features, or handle them externally**

Usually the problems that ML is trying to solve are not completely new.

There is an existing system for ranking or classifying.

This means that there are a bunch of rules and heuristics.

**These same heuristics can give you a lift when tweaked with ML**

Your heuristics should be mined for whatever information they have, for 2 reseaons:

1. The trasnsition to a ML system will be smoother.
2. Usually theose rules contain a lot of the intution about the system you don't want to throw away.

There are 4 ways you can use an existing heuristic : 


1. Preprocess using heuristic : If the feature is incredibly awesome, then this is an option 
   * e.g. A sender has already been blacklisted in a spam filter(make sense in binary classification task)
2. Create a feature
   * e.g. you use a heuristic to compute a relevance score for a query result, you can include the score as the value of a feautre \. Later on you may wan to use ML techniques to massage the value(converting into distinct values, combing it with other features)
3. Mine the raw inputs of the heuristic
   * e.g. a hruristic for apps that combines the number of installs, the number of characters in the text, the day of the week. Then consider pulling these pieces apart, and feeding these inputs into the learning.
4. Modify the label(?) - This is an option when you feel that the heuristic captures information not currently contained in the label.
   * If you are trying to maximize the number of downloads, bbut you also want quality content, **then maybe the solution is to multiply the label by the average number of starts the app received**

# Monitoring - 4 rules
In general, practice good alerting hygiene, such as making alerts actionable and having a dashboard page.

## **R8 Know the freshness requirements of your system.**


How much does performance degrade if you have a model?

a day/week/quarter/year old?

This information can help you to understand the priorities of your monitoring. If you lose 10% of your revenue if the model is notupdated for a day. it makes sense to have an engineer watching it continuously.

**Most ad serving systems have new advertisements to handle every day, and must update daily.**

Example : if ML model for Google Play Search is not updated, it can have an impact on revenue in under a month.

Also notice that freshness can change over time. especially when feature columns are added or removed from your model.

## **R9 Detect problems before exporting models**

Many machine learning system have as stage where you export the model to serving.

If there is an issue with an exported model. It is a user-facing issue.

If there is an issue before, then it is a training issue. and user will not notice.

Do sanity checkes right before you export the model.

Specifically, make sure the model's performance is reasonable on held out data. Or, if you have lingering(揮之不去的) concerns with the data, don't export a model.

Many teams continoisly deploying models check the AUC value before exporting.

**Issue about models that haven't been exported require an e-mail alert, but issues on a user-facing model may require a page**

So better to wait and be sure before impacting users.

## **R10 Watch for silent failures**

This is a problem that occurs more for ML systems than for ther kinds of system.

e.g. : a particular table is being joined is no longer being updated. -> performance of ML system might decay!(due to the data freshness).

## **R11** Give feature column owners and documentation

If the system is large, and there are many feature columns, know who created or is maintaining each feature column.

If you find that the person who understands a feature column is leaving, make sure that someone has the information.

It's good to have a more detailed description of what the feature is, where it came from, and how it's expected to help.


# ML Pahse II: Feature Engineering - 1 rules

# ML Phase III: Slowed Growth, Optimization Refinement, and Complex Models

## **R16 Plan to launch and iterate**

Don't expect that the model you are working on now will be the last one that you will launch, or even that you will ever stop launching models. Thus consider whether the complexity you are adding with this launch will slow down futher launches.

Many team have launched a model **per quarter or more for years**. There are 3 basic reseaons to launch new models :

1. you are coming up with new features
2. you are tuning regulization and combining old features in new ways.
3. you are tuning the objective.

So, as you build your model, think about 

1. how easy it is to add or remove or recombine features
2. how easy it is to create a fresh copy of the pipeline and verify its correctness.
3. wherther it is possible to have two or three copies running in parallel