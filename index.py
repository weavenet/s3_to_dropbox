#!/usr/bin/env python

import boto3
import dropbox
import json
import os
import time

def upload_data_to_dropbox(data, key):
    dropbox_access_token = os.environ['DROPBOX_ACCESS_TOKEN']
    file_name = "/" + key

    print "Uploading file to dropbox '%s'." % file_name
    dbx = dropbox.Dropbox(dropbox_access_token)
    dbx.files_upload(data, file_name)
    print "Upload complete"

def download_s3_object(region, bucket, key):
    client = boto3.client('s3', region_name=region)
    print "Dowloading object from s3."
    response = client.get_object(Bucket=bucket, Key=key)
    body = response['Body'].read()
    print "Download complete."
    return body

def process_record(record):
    key = record['s3']['object']['key']
    bucket = record['s3']['bucket']['name']
    region = record['awsRegion']

    print "Processing key '%s' in bucket '%s' in region '%s'." % (key, bucket, region)
    data = download_s3_object(region, bucket, key)
    upload_data_to_dropbox(data, key)

def process_event(event):
    for record in event['Records']:
      print "Processing record '%s'." % record
      process_record(record)

def handler(event, context):
    print "Processing event '%s'." % event
    process_event(event)
