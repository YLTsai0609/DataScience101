# Google App Engine

[Third Party Introduction](https://medium.com/@dada8397/%E5%BE%9E%E9%9B%B6%E9%96%8B%E5%A7%8B%E7%9A%84gcp%E4%B9%8B%E6%97%8501-google-app-engine-2a7f375c2928)

[doc](https://cloud.google.com/appengine/docs/flexible/python/quickstart?hl=zh-tw)


1. Serveless
2. get configs in `app.yaml`
   1. handlers : a list of URL patterns and descriptions of how they should be handled

# Hello world

Check this [Third Party Introduction](https://medium.com/@dada8397/%E5%BE%9E%E9%9B%B6%E9%96%8B%E5%A7%8B%E7%9A%84gcp%E4%B9%8B%E6%97%8501-google-app-engine-2a7f375c2928)


`git clone https://github.com/dada8397/gae-demo`

the app.yaml

```
runtime: python27
api_version: 1
threadsafe: true

handlers:
- url: /
  static_files: www/index.html
  upload: www/index.html

- url: /(.*)
  static_files: www/\1
  upload: www/(.*)
```

check your own gcp projects

1. list project

```
(base) joetsai@thor:~/work/yulong/gae-demo$ gcloud config list
[core]
account = joetsai@pixnet.tw
disable_usage_reporting = True
project = pixnet-gt

Your active configuration is: [default]
```

1. deploy your gae by 

```
$ gcloud config set project helloworld-277717
$ gcloud app deploy
```

or 

```
gcloud app deploy --project=helloworld-277717
```

then you will get

```
(base) joetsai@thor:~/work/yulong/gae-demo$ gcloud app deploy --project=pixnet-research-lab
Services to deploy:

descriptor:      [/home/joetsai/work/yulong/gae-demo/app.yaml]
source:          [/home/joetsai/work/yulong/gae-demo]
target project:  [pixnet-research-lab]
target service:  [default]
target version:  [20210427t231206]
target url:      [https://pixnet-research-lab.df.r.appspot.com]

```

2. Done!

```
Beginning deployment of service [default]...
╔════════════════════════════════════════════════════════════╗
╠═ Uploading 3 files to Google Cloud Storage                ═╣
╚════════════════════════════════════════════════════════════╝
File upload done.
Updating service [default]...done.
Setting traffic split for service [default]...done.
Deployed service [default] to [https://pixnet-research-lab.df.r.appspot.com]

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse --project=pixnet-research-lab
```

3. You can check the service tab of `app engine` to monitor your services.

# Quickstart for Python in the App Engine Flexible Environment


[follow by the google app engine for python doc](https://cloud.google.com/appengine/docs/flexible/python/quickstart?hl=zh-tw)

[`app.yaml` documentation](https://cloud.google.com/appengine/docs/standard/python3/config/appref)
