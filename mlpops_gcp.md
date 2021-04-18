# Ref

[An introduction to MLOps on Google Cloud](https://www.youtube.com/watch?v=6gdrwFMaEZ0)

# Content

## Tech Debt

[Hidden Technical Debt in Machine Learning Systems 2015, google 450+ citations](https://web.kaust.edu.sa/Faculty/MarcoCanini/classes/CS290E/F19/papers/tech-debt.pdf)

![img](./images/mlopsgcp_1.png)

## Challenges

![img](./images/mlopsgcp_2.png)

1. Time Consuming (EDA, feature, hyperparamter tuning)
2. Manual
3. Inflexible (Cannot adapte to another problem)
4. Not reusable

## ML Solution Lifecycle

![img](./images/mlopsgcp_3.png)

1. (Training) Experiments are critical to discovery and make sure data team deliver the best solution
3. (Serving) Model should be properly tested, evaluted and should be even versionable.
4. (Serving) monitoring - discovering better training data, making sure our model works well, debug when our model went wrong silently.
5. monitor as a feedback system.

![img](./images/mlopsgcp_4.png)

Source Repo - source code

Artifact Store - ml pipeline, artifacts

Model Resgistry - trained model

trained model should be linked the pipeline, articfacts and source code.

![img](./images/mlopsgcp_5.png)

![img](./images/mlopsgcp_6.png)

# MLOps on GCP


![img](./images/mlopsgcp_7.png)

![img](./images/mlopsgcp_8.png)

green part : open source tools

# Our needs

(Integrated in git hash) : model-versioning, data-versioning, src versioning(including pipeline code)