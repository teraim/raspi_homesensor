#!/bin/bash
cam_name="raspcam01"
dt=`date +'%y%m%d%H%M'`
echo $dt
mkdir -p ${HOME}/cam_images
fn="${HOME}/cam_images/${cam_name}_${dt}.jpg"
raspistill -o ${fn} -w 640 -h 480
convert -pointsize 24 -fill white -font "Helvetica" -draw "text 50,50 '`date` ${cam_name}'" ${fn} ${fn}
