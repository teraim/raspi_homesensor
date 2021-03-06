#!/bin/bash -x
home_dir=/home/pi
cam_name="raspcam01"
mkdir -p ${home_dir}/sensor
dt=`date +'%y%m%d'`
fn=${cam_name}_sensor_temp_${dt}.csv

if [ ! -e ${home_dir}/sensor/${fn} ]; then
  echo "datetime,temp" > ${home_dir}/sensor/${fn}
fi

${home_dir}/raspi_homesensor/sensor_temp_AM2320.py >> ${home_dir}/sensor/${fn}
