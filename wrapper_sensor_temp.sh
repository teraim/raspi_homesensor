#!/bin/bash -x
inst_dir=/home/pi/raspi_homesensor
cam_name="raspcam01"
mkdir -p ${inst_dir}/sensor
${inst_dir}/raspi_homesensor/sensor_temp.py >> ${isnt_dir}/sensor/${cam_name}_sensor_temp.log
