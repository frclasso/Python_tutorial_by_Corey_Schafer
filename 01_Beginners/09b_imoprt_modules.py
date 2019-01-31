#!/usr/bin/env python3

import sys

sys.path.append('/Users/fabio/Estudo/Prog/Python/Python_tutorial_by_Corey_Schafer')

from my_module import find_index, test

courses = ['History','Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')

print(index)
print(test)