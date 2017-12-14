# python3 testing.py | python3 prerelease.py

import random
import time

NUM_COWS = 1000
print(NUM_COWS)

# Test with a 
def test_with_cow_ids():
    cow_ids = list(range(0, NUM_COWS))
    for _, cow_id in enumerate(cow_ids):
        print(cow_id)
        print(random.random() * 12)
    random.shuffle(cow_ids)


def test_with_random_ids():
    for _ in range(NUM_COWS):
        print(random.randint(0, NUM_COWS))
        print(random.random() * 12)


def test():
    random.seed(time.time())
    for i in range(14):
        test_with_cow_ids()

test()
