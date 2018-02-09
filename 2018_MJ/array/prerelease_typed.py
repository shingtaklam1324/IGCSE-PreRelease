#!/usr/local/bin/python3.7
'''
    2018 May/June CIE Comp Sci IGCSE Pre Release
'''

from typing import List, TypeVar, Callable
import sys
import signal
import gc

def c_c(_signal, _frame):
    '''
    Handler for SIGINT
    '''
    print("\n\x1b[91;1mSIGINT\nCleaning Up\x1b[0m")
    gc.collect()
    sys.exit(1)


signal.signal(signal.SIGINT, c_c)

# Generic Number Type
N = TypeVar('N')


def main():
    '''
    Main
    '''

    cows: List[List[int]] = [[0.0 for i in range(15)] for j in range(1000)]

    def convert(prompt: str, convert_to: Callable[[str], N], err_msg: str, validation: Callable[[N], bool] = lambda _: True) -> N:
        '''
        Converts the input into a different type and performs the validation
        function on the result. Prints out the error if a ValueError occurs
        or the validation fails
        '''

        while 1:
            try:
                value: N = convert_to(
                    input("\x1b[1;93m{}\x1b[0m".format(prompt)))
                if not validation(value):
                    raise ValueError
                return value
            except ValueError:
                print("\x1b[1;91m{}\x1b[0m".format(err_msg))
                continue

    num_cows: int = convert("Number of Cows: ", int,
                            "Invalid input", lambda x: 0 <= x <= 1000)

    for time in range(14):
        # (7 days * twice per day)
        print("\n\x1b[1;97mDay {} {}\x1b[0m".format(int(time / 2) + 1, "Morning" if time %
                                                    2 == 0 else "Afternoon"))
        for _ in range(num_cows):
            cow_id: int = convert("Cow ID: ", int, "Invalid input",
                                  lambda x: 0 <= x < 1000)
            volume: float = convert("Volume: ", float,
                                    "Invalid input", lambda x: x >= 0)
            cows[cow_id][time] = volume
            # Set [14] to 1, so there is an input
            cows[cow_id][14] = 1

    # Only first 14 are wanted, [14] is the 'has input bit'
    total: float = sum(map(lambda x: sum(x[:14]), cows))

    print("\n\n\x1b[1;97mResults")
    print("Total:\x1b[0m {} \x1b[1;97ml".format(round(total)))
    print("Averages:\x1b[0m")
    for cow_id, cow in enumerate(cows):
        if cow[14]:
            print(round(sum(cow[:14]) / 14))

    print("\n\x1b[1;91mCows with < 12 l for 4+ days\x1b[0m")
    # Get a tuple of (cow_id, volumes)
    for cow_id, cow in enumerate(cows):
        # Work out the number of days where vol < 12 ([2i] + [2i+1] < 12)
        days: List[float] = [cow[2 * i] + cow[2 * i + 1] for i in range(7)]
        # Filter only the days where volume < 12, if length is > 4 and has input
        if len([i for i in filter(lambda x: x < 12, days)]) >= 4 and cow[14] == 1:
            print("\x1b[31mCow {}{}\x1b[0m".format(
                "0" * (3 - len(str(cow_id))), cow_id))

    # Find the maximum index (cow_id)
    idx: int = cows.index(max(cows, key=(lambda x: sum(x[:14]))))

    print("\n\x1b[1;92mCow with the most milk\x1b[0m")
    print("\x1b[32mCow {}{}\x1b[0m".format("0" * (3 - len(str(idx))), idx))


main()
