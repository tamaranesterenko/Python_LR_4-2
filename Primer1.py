# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import json


my_list = ['foo', 'bar']


with open("foo.txt", "w", encoding="utf-8") as f:
    json.dump(my_list, f)

