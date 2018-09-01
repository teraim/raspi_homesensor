# raspi homesensor (experimental)

## Preliminary

- sudo apt-get install awscli
- pip install smbus
- pip install retry
- pip install boto3

## AWS Preliminary

$ aws config

Please refer to the region name (e.g., ap-northeast-1) you use.
https://docs.aws.amazon.com/general/latest/gr/rande.html

## Usage

To routinely work this program, you can add a following line to the cron table in your environment.

*/10 * * * * /home/pi/raspi_homesensor/wrapper.sh
