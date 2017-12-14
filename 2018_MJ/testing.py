# python3 testing.py | python3 prerelease.py

import random
import time

NUM_COWS = 20
print(NUM_COWS)


def test_fixed_cow_ids():
    cow_ids = list(range(0, NUM_COWS))
    for cow_id in cow_ids:
        print(cow_id)
        print(random.random() * 12)
    random.shuffle(cow_ids)


def test_random_ids():
    for _ in range(NUM_COWS):
        print(random.randint(0, NUM_COWS))
        print(random.random() * 12)


def test_fixed_data():
    cow_ids = list(range(0, NUM_COWS))
    for cow_id in cow_ids:
        print(cow_id)
        print(cow_id)
    random.shuffle(cow_ids)


def test():
    random.seed(time.time())
    for _ in range(14):
        test_fixed_cow_ids()


test()
