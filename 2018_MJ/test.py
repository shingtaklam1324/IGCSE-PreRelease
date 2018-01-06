'''
    Pipes output of testing.py into prerelease.py
'''
import os
import sys

ITERATIONS = 1

for _ in range(ITERATIONS):
    file_name = sys.argv[1]
    num_cows = sys.argv[2]
    for test in sys.argv[3:]:
        print("\nTest: {}".format(test))
        os.system(
            "python3 testing.py {} {} | python3 {}".format(num_cows, test, file_name))
