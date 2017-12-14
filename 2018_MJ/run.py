import os

ITERATIONS = 1

for _ in range(ITERATIONS):
    os.system("python3 testing.py | python3 prerelease.py")
