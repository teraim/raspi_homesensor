# raspi homesensor (experimental)

## Preliminary

- sudo apt-get install awscli
- pip install smbus
- pip install retry
- pip install boto3

## Usage

To routinely work this program, you can add a following line to the cron table in your environment.

# m h  dom mon dow   command
*/10 * * * * /home/pi/raspi_homesensor/wrapper.sh
