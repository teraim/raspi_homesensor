# raspi homesensor (experimental)

## Preliminary

- sudo apt-get install awscli bc git
- sudo apt-get install python3 python3-pip
- sudo apt-get install python-numpy python-smbus i2c-tools
- sudo apt-get install pigpio

Before installation python modules, you should upgrade pip itself.

~~~
$ sudo pip3 install --upgrade pip
~~~

- sudo pip install scipy
- sudo pip install retry
- sudo pip install boto3
- sudo pip install picamera

## OpenCV Preliminary

### Quick Install (Raspberry Pi 3+)

~~~
$ sudo apt autoremove libopencv3 //if necessary

$ wget https://github.com/mt08xx/files/raw/master/opencv-rpi/libopencv3_3.4.2-20180709.1_armhf.deb
$ sudo apt install -y ./libopencv3_3.4.2-20180709.1_armhf.deb
$ sudo ldconfig
~~~

### Source Compiling Install (Raspberry Pi Zero)

~~~
$ sudo apt-get install build-essential cmake pkg-config
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev
$ sudo apt-get install libatlas-base-dev gfortran
~~~

Dowload an achived package from the following site.

https://github.com/opencv/opencv/releases

~~~
$ tar xzf 3.4.3.tar.gz
$ cd opencv-3.4.3
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/opt/opencv-3.4.3 -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON ..
$ make
$ sudo make install
$ ldconfig
~~~

## AWS Preliminary

$ aws config

Please refer to the exact region name (e.g., ap-northeast-1) you use.

https://docs.aws.amazon.com/general/latest/gr/rande.html

## Usage

To routinely work this program, you can add a following line to the cron table in your environment.

# sudo crontab -e

*/10 * * * * /home/pi/raspi_homesensor/wrapper.sh
