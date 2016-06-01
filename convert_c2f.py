#!/usr/bin/env python
# Convert celsius to fahrenheit
import sys

try:
    sys.argv[1]
    temp_c = float(sys.argv[1])
    temp_f = temp_c*(9.0/5.0) + 32
    print('Temperature in Fahrenheit: ', temp_f)

except:
    print('Incorrect input')

