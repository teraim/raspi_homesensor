#!/bin/bash -x
home_dir=/home/pi
cam_name="raspcam01"
mkdir -p ${home_dir}/sensor

if [ ! -e ${home_dir}/sensor/${cam_name}_sensor_temp.csv ]; then
  echo "datetime,temp" > ${home_dir}/sensor/${cam_name}_sensor_temp.csv
fi

${home_dir}/raspi_homesensor/sensor_temp.py >> ${home_dir}/sensor/${cam_name}_sensor_temp.csv
