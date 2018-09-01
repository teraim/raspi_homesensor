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

def upload_images(s3):
    if not os.path.exists("%s/cam_images/" % homedir):
        print("error: cam_images dir does not exist.")
        exit()

    fns = glob("%s/cam_images/*.jpg" % homedir)
    print(fns)

    for fn in fns:
        if os.path.isfile(fn):
            print(fn)
            #f = open(fn,"rb")
            basename = os.path.basename(fn)
            s3.upload_file(fn, bucket_name, "%s/%s" % (cam_name, basename))
            #f.close()
            os.remove(fn)

def upload_sensor(s3):
    if not os.path.exists("%s/sensor/" % homedir):
        print("error: sensor dir does not exist.")
        exit()

    fns = glob("%s/sensor/*.log" % homedir)
    print(fns)

    for fn in fns:
        if os.path.isfile(fn):
            print(fn)
            basename = os.path.basename(fn)
            s3.upload_file(fn, bucket_name, "%s/%s" % (cam_name, basename))

if __name__ == '__main__':
    #s3 = boto3.resource('s3')
    s3 = boto3.client('s3')
    upload_images(s3)
    upload_sensor(s3)
