#!/bin/bash

region=$1
function_name=s3_to_dropbox

if [ "$region" == "" ]; then
    echo "Usage: $0 REGION"
    exit 1
fi

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Clean up old build file
file=$TMPDIR/build.zip
echo "Build file: '$file'."
\rm -f $file

# Build zip file to deploy
orig_dir=`pwd`
cd $DIR/../venv/lib/python2.7/site-packages/
zip -r -9 $file  *
cd $DIR/..
zip -q -r -9 $file *.py
cd $orig_dir

# Deploy code to existing lambda function
echo "Deploying to '$function_name'."
aws lambda update-function-code \
    --region $region \
    --function-name $function_name \
    --zip-file fileb://$file
echo "Deployment completed succesfully."
