def main():

    cows = [[0.0 for i in range(15)] for j in range(1000)]

    def convert(prompt, to, err_msg, validation):
        while 1:
            try:
                value = to(input("\x1b[1;93m{}\x1b[0m".format(prompt)))
                if not validation(value):
                    print(err_msg)
                    continue
                return value
            except ValueError:
                print(err_msg)
                continue

    num_cows = convert("Number of Cows: ", int,
                       "Invalid input", lambda x: 0 <= x <= 1000)

    for time in range(14):
        print("\x1b[1;97mDay {} {}\x1b[0m".format(int(time / 2), "Morning" if time %
                                 2 == 0 else "Afternoon"))
        for _ in range(num_cows):
            cow_id = convert("Cow ID: ", int, "Invalid input",
                             lambda x: 0 <= x < 1000)
            volume = convert("Volume: ", float,
                             "Invalid input", lambda x: x >= 0)
            cows[cow_id][time] = volume
            cows[cow_id][14] = 1

    total = sum(map(sum, cows))
    
    print("\n\n\x1b[1;97mResults")
    print("Total:\x1b[0m {} \x1b[1;97ml".format(round(total)))
    print("Average:\x1b[0m {} \x1b[1;97ml".format(round(total/num_cows)))

    print("\n\x1b[1;91mCows with < 12 l for 4+ days\x1b[0m")
    for cow_id, cow in enumerate(cows):
        days = [cow[2 * i] + cow[2 * i + 1] for i in range(7)]
        if len([i for i in filter(lambda x: x < 12, days)]) and cow[14] == 1:
            print("\x1b[31mCow {}{}\x1b[0m".format("0" * (3 - len(str(cow_id))), cow_id))

    idx = cows.index(max(cows, key=(lambda x: sum(x[:14]) * x[14])))
    
    print("\n\x1b[1;92mCow with the most milk\x1b[0m")
    print("\x1b[32mCow {}{}\x1b[0m".format("0" * (3 - len(str(idx))), idx))
main()
