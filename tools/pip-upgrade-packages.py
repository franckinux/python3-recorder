#!/usr/bin/env python3

import argparse
import os
# import sys

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-l", "--local", action="store_true")
group.add_argument("-u", "--user", action="store_true")

args = parser.parse_args()

if args.local:
    range = "local"
elif args.user:
    range = "user"
else:
    range = "local"

stream = os.popen(f"pip list --{range} --outdated --format=freeze")
output = stream.read()
if len(output) == 0:
    print("no package to upgrade")
else:
    for line in output.splitlines():
        try:
            package, _ = line.split("==")
        except Exception:
            continue
        os.system(f"pip install -U {package}")
