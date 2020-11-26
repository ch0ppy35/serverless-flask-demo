# Serverless Flask Demo

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)

Flask in a serverless implementation

## Examples

```bash

(venv) [mmiller@Mikes-MacBook-Pro-13 serverless-flask (master ✗)]$ curl -XGET https://bvip0m9ua0.execute-api.us-west-2.amazonaws.com/dev/hi
{"message": "Hi stranger"}

(venv) [mmiller@Mikes-MacBook-Pro-13 serverless-flask (master ✗)]$ curl -XPOST -H "Content-Type: application/json" https://bvip0m9ua0.execute-api.us-west-2.amazonaws.com/dev/hi -d '{"name": "Mike"}'
{"message": "Hi Mike"}
```

## Deploying

First run

```bash
# Install serverless too
npm install serverless-wsgi
npm install serverless-python-requirements
```

Then you can deploy

```bash
(venv) [mmiller@Mikes-MacBook-Pro-13 serverless-flask (master ✗)]$ sls deploy
Serverless: Using Python specified in "pythonBin": python3
Serverless: Packaging Python WSGI handler...
Serverless: Generated requirements from /Users/mmiller/Projects/serverless-flask/requirements.txt in /Users/mmiller/Projects/serverless-flask/.serverless/requirements.txt...
Serverless: Installing requirements from /Users/mmiller/Library/Caches/serverless-python-requirements/6ed307820043b7faf3beb259bd2438f90f807003fc53f199203fc13cc09f09ce_slspyc/requirements.txt ...
Serverless: Docker Image: lambci/lambda:build-python3.8
Serverless: Using download cache directory /Users/mmiller/Library/Caches/serverless-python-requirements/downloadCacheslspyc
Serverless: Running docker run --rm -v /Users/mmiller/Library/Caches/serverless-python-requirements/6ed307820043b7faf3beb259bd2438f90f807003fc53f199203fc13cc09f09ce_slspyc\:/var/task\:z -v /Users/mmiller/Library/Caches/serverless-python-requirements/downloadCacheslspyc\:/var/useDownloadCache\:z -u 0 lambci/lambda\:build-python3.8 python3.8 -m pip install -t /var/task/ -r /var/task/requirements.txt --cache-dir /var/useDownloadCache...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Injecting required Python packages to package...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service flask-serverless-demo.zip file to S3 (10.03 MB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: flask-serverless-demo
stage: dev
region: us-west-2
stack: flask-serverless-demo-dev
resources: 12
api keys:
  None
endpoints:
  ANY - https://bvip0m9ua0.execute-api.us-west-2.amazonaws.com/dev
  ANY - https://bvip0m9ua0.execute-api.us-west-2.amazonaws.com/dev/{proxy+}
functions:
  app: flask-serverless-demo-dev-app
layers:
  None
```
