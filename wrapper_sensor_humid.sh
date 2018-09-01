#!/bin/bash -x
inst_dir=/home/pi/raspi_homesensor
cam_name="raspcam01"
mkdir -p ${inst_dir}/sensor
${inst_dir}/raspi_homesensor/sensor_humid.py >> ${inst_dir}/sensor/${cam_name}_sensor_humid.log
