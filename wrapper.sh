#!/bin/bash -x

INST_DIR=/home/pi/raspi_homesensor

ret=`ps -el | grep pigpiod | wc -l`
if [ $ref -eq 0 ]; then
  sudo pigpiod
fi

${INST_DIR}/cam.py
${INST_DIR}/sensor_HTU21DF.py
${INST_DIR}/upload_s3.py
