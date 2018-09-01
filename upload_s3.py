#!/usr/bin/python
import os
import sys
import os.path
import boto3
from glob import glob

bucket_name = "raspz"
cam_name = "cam01"

homedir = os.environ['HOME']
print(homedir)

if not os.path.exists("%s/cam_images/" % homedir):
    print("error: cam_images dir does not exist.")
    exit()

fns = glob("%s/cam_images/*.jpg" % homedir)
print(fns)

#s3 = boto3.resource('s3')
s3 = boto3.client('s3')

for fn in fns:
    if os.path.isfile(fn):
        print(fn)
        #f = open(fn,"rb")
        basename = os.path.basename(fn)
        s3.upload_file(fn, bucket_name, "%s/%s" % (cam_name, basename))
        #f.close()
        os.remove(fn)

fns = glob("%s/room_env/*.log" % homedir)
print(fns)

for fn in fns:
    if os.path.isfile(fn):
        print(fn)
        basename = os.path.basename(fn)
        s3.upload_file(fn, bucket_name, "%s/%s" % (cam_name, basename))

