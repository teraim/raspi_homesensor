#!/bin/bash -x
home_dir=/home/pi/raspi_homesensor
cam_name="raspcam01"
mkdir -p ${inst_dir}/sensor
${home_dir}/raspi_homesensor/sensor_temp.py >> ${home_dir}/sensor/${cam_name}_sensor_temp.log
