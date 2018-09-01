#!/bin/bash -x
cam_name="raspcam01"
mkdir -p ${HOME}/sensor
${HOME}/raspi_homesensor/sensor_temp.py >> ${HOME}/sensor/${cam_name}_sensor_temp.log
