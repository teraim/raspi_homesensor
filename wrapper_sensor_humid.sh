#!/bin/bash -x
cam_name="raspcam01"
mkdir -p ${HOME}/sensor
${HOME}/raspi_homesensor/sensor_humid.py >> ${HOME}/sensor/${cam_name}_sensor_humid.log
