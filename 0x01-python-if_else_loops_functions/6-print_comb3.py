#!/usr/bin/python3
for digits in range(0, 10):
    for digits2 in range(digits + 1, 10):
	if digits == 8 and digits2 == 9:
	   print("{}{}".format(digits, digits2))
	else:
	   print("{}{}".format(digits, digits2), end=", ")
