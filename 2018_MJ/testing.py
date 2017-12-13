import random
import time

cow_ids = [123, 124, 125, 126, 127]

random.seed(time.time())

for i in range(14):
    for cow_id in range(len(cow_ids)):
        print(cow_ids[cow_id])
        print(random.random() * 12)
    random.shuffle(cow_ids)
