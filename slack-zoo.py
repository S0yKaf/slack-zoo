#! /bin/python3

import subprocess
import random

from config import TOKEN, WORKSPACE, DATA

endpoint = f"https://{WORKSPACE}.slack.com/api/users.profile.set"
status = random.choice(DATA)
subprocess.run(["curl", "-s",
                "-H", f"Authorization: Bearer {TOKEN}",
                "-H", "Content-type: application/x-www-form-urlencoded",
                "--data-urlencode", f"profile={status}", endpoint],
               stdout=subprocess.DEVNULL)
