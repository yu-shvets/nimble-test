**s3_test.py** is a Python module to put and download a binary file
using **AMAZON S3** cloud storage service.

All dependencies are indicated in 'requirements.txt' and can be
installed with a command: _pip install -r requirements.txt_


**Functions:**

**_get_s3_client():_** - a function to establish connection to
    Amazon S3 creating S3 client. It requires Amazon credentials
    imported as variables - AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY.
    
**_put_file(bucket_name, file_name):_** - A function to put a binary 
    file to existing S3 bucket. It requires the names of existing bucket 
    and file as arguments. This function creates url with bucket name 
    and filename as a key in parameters. Then puts a file to a certain
    bucket using requests library.
    
**_get_file(bucket_name, file_name):_** - A function to download 
    file from existing S3 bucket, creating S3 client first. The names of 
    existing bucket and file are passed as arguments. It raises 
    exception if certain file does not exist.
      

