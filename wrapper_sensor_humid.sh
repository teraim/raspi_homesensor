#!/bin/bash -x
home_dir=/home/pi
cam_name="raspcam01"
mkdir -p ${home_dir}/sensor

if [ ! -e ${home_dir}/sensor/${cam_name}_sensor_humid.csv ]; then
  echo "datetime,humidity" > ${home_dir}/sensor/${cam_name}_sensor_humid.csv
fi

${home_dir}/raspi_homesensor/sensor_humid.py >> ${home_dir}/sensor/${cam_name}_sensor_humid.csv
