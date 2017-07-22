# s3_to_dropbox

Cloud Formation template that sets up a S3 bucket which, when objects are placed in it,
will trigger a S3 Event, to execute a Lambda, which will copy the files to Dropbox.

## Prerequistes

* Python 2.7
* AWS CLI
* Tested on MacOS 10.12

## Deploy

### Create Bucket and Function

* Create a [Dropbox app and oauth token](https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/).

* Create Cloud Formation Stack from **cloud_formation_templates/lambda.json** and provide the 
token created above as the **DropboxTokenAccess** parameter.

### Deploy Updated Code To Lambda Function

* Setup your virutal env

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

* Deploy the code

```
bash scripts/deploy.sh us-west-2
```

You should now be able to place objects in the bucket and have them copied to Dropbox.
