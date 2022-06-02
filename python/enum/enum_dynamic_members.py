# Dynamic member from struct data
# Can be used to create custom enum from env variables

import enum

data = ["xxx", "yyy"]
parsed_data={}

for elt in data:
    parsed_data[elt]=elt

A = enum.Enum('A', parsed_data)

# result:
# ipdb> A.xxx
# <A.xxx: 'xxx'>
# ipdb> A.xxx.value
# 'xxx'
