#!/bin/bash -x
INST_DIR=/home/pi/raspi_homesensor
{INST_DIR}/cam.sh
${INST_DIR}/wrapper_sensor_humid.sh
${INST_DIR}/wrapper_sensor_temp.sh
${INST_DIR}/upload_s3.py
