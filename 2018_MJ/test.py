'''
    Pipes output of testing.py into prerelease.py
'''
import os
import sys

ITERATIONS = 1

for _ in range(ITERATIONS):
    num_cows = sys.argv[1]
    for test in sys.argv[2:]:
        print("\nTest: {}".format(test))
        os.system(
            "python3 testing.py {} {} | python3 prerelease.py -s".format(num_cows, test))
