# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import json


with open("foo.txt", "r") as f:
    contents = f.read()
my_list = json.loads(contents)



