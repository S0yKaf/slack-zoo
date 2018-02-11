# slack-zoo
Set your slack status to a random animal.

## Requirements
* curl
* python3.6.x
* a deep love for animals

## Setup
1. add your slack auth token and the desired workspace in `config.py`
```bash
$ sed -i 's/YOUR_SLACK_AUTH_TOKEN/your_token/' config.py
$ sed -i 's/YOUR_WORKSPACE/your_workspace/' config.py
```
2. have fun!

## Usage
`$ ./slack_zoo.py` or `$ python slack_zoo.py`

### cron
This script is best used alongside a cron-job for added lulz.
```bash
# make sure to run this on the root of the repo.
$ (crontab -l; echo "*/5 * * * * python3.6 $(pwd)/slack-zoo.py") | crontab
```
