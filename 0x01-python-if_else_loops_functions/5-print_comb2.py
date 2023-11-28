#!/usr/bin/python3
for num5 in range(0, 100):
    if num5 == 99:
        print("{}".format(num5))
    else:
        print("{:02}".format(num5), end=", ")
