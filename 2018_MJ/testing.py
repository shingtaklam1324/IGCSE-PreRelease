''' Generates the output to pipe into prerelease.py '''

import random
import time
import sys


NUM_COWS = int(sys.argv[1])
print(NUM_COWS)


def fixed_cow_ids(cow_ids):
    ''' Test with shuffled cow_ids and random volumes '''
    for cow_id in cow_ids:
        print(cow_id)
        print(random.random() * 14)
    random.shuffle(cow_ids)


def random_ids(_):
    ''' Test with random ids and volumes '''
    for _ in range(NUM_COWS):
        print(random.randint(0, NUM_COWS))
        print(random.random() * 14)


def fixed_data(cow_ids):
    ''' Test with shuffled ids and volume = id '''
    for cow_id in cow_ids:
        print(cow_id)
        print(cow_id)
    random.shuffle(cow_ids)


def invalid_volume(cow_ids):
    ''' Test with invalid volume input '''
    for cow_id in cow_ids:
        print(cow_id)
        if random.random() > 0.5:
            print('a')
        print(cow_id)
    random.shuffle(cow_ids)


def invalid_cow_id(cow_ids):
    ''' Test with invalid cow ID input '''
    for cow_id in cow_ids:
        if random.random() > 0.5:
            print('a')
        print(cow_id)
        print(cow_id)
    random.shuffle(cow_ids)


def test():
    ''' generate test input '''
    test_name = sys.argv[2]

    random.seed(time.time())
    cow_ids = list(range(NUM_COWS))
    for _ in range(14):
        globals()[test_name](cow_ids)


test()
