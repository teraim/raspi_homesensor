#!/bin/bash -x
inst_dir=/home/pi/raspi_homesensor
cam_name="raspcam01"
dt=`date +'%y%m%d%H%M'`
mkdir -p ${isnt_dir}/cam_images
fn="${isnt_dir}/cam_images/${cam_name}_${dt}.jpg"
echo ${fn}

##
#if [ ! -e /sys/class/gpio/gpio21 ]; then
#  sudo sh -c "echo 21 > /sys/class/gpio/export"
#  sudo sh -c "echo out > /sys/class/gpio/gpio21/direction"
#fi

#sudo sh -c "echo 1 > /sys/class/gpio/gpio21/value"

raspistill -o ${fn} -w 640 -h 480 -rot 180
#raspistill -o ${fn} -rot 180

#sudo sh -c "echo 0 > /sys/class/gpio/gpio21/value"

#if [ -e /sys/class/gpio/gpio21 ]; then
#  sudo sh -c "echo 21 > /sys/class/gpio/unexport"
#fi

##
convert -pointsize 24 -fill white -font "Helvetica" -draw "text 50,50 '`date` ${cam_name}'" ${fn} ${fn}
