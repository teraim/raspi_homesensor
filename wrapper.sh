#!/bin/bash -x
./cam.sh
./wrapper_sensor_humid.sh
./wrapper_sensor_temp.sh
./upload_s3.py
