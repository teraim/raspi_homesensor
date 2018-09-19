#!/usr/bin/python

import os
import sys
from datetime import datetime
import HTU21DF

home_dir="/home/pi"
cam_name="raspcam01"

if not os.path.isdir("%s/sensor" % home_dir):
    os.mkdir("%s/sensor" % home_dir)

dt_now = datetime.now()
dt_str1 = dt_now.strftime("%Y/%m/%d %H:%M:%S")
dt_str2 = dt_now.strftime("%Y%m%d")

fn = "%s/sensor/%s_sensor_%s.csv" % (home_dir, cam_name, dt_str2)

f = open(fn, "a")

HTU21DF.htu_reset()
temp = HTU21DF.read_temperature()
humid = HTU21DF.read_humidity()

f.write("%s,%s,%s\n" % (dt_str1, temp, humid))

f.close()
