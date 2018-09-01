#!/bin/bash
./cam.sh
./room_env_humid.sh
./room_env_temp.sh
./upload_s3.py
