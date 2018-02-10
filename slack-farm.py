#! /bin/python3

import subprocess
import os
import random

import data as status

token = "YOUR_SLACK_AUTH_TOKEN"
endpoint = "https://YOUR_WORKSPACE.slack.com/api/users.profile.set"

data = random.choice(status.DATA)
subprocess.run(["curl", "-s",
                "-H", f"Authorization: Bearer {token}",
                "-H", "Content-type: application/x-www-form-urlencoded",
                "--data-urlencode", f"profile={data}", endpoint],
               stdout=subprocess.DEVNULL)
