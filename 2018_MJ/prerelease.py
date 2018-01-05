'''
    2018 May/June CIE Comp Sci IGCSE Pre Release
'''
import sys


def convert_input(
        prompt="",
        convert_to=float,
        err_msg="Error parsing input",
        validation=(lambda x: True)):
    '''
        Converts the input into a different type and performs the validation
        function on the result. Prints out the error if a ValueError occurs
        or the validation fails
    '''

    while 1:
        try:
            value = convert_to(input("" if (len(sys.argv) > 1) and (
                sys.argv[1] == "-s" or sys.argv[1] == "--suppressed") else ("\x1b[1;93m" + prompt + "\x1b[0m")))
            if validation(value):
                return value
            else:
                print(err_msg)
                continue
        except ValueError:
            print(err_msg)
            continue


def main(cows):
    ''' Main Function '''

    num_cows = convert_input(
        prompt="Number of cows: ",
        convert_to=int,
        validation=lambda x: x > 0,
        err_msg="Invalid number of cows"
    )

    for i in range(14):
        print("\x1b\n\nDay {} {}\n".format(int(i / 2) + 1, "Morning" if i %
                                           2 == 0 else "Afternoon"))
        for _ in range(num_cows):
            # If cow is in dict, use current, otherwise insert new list
            cow_id = convert_input(
                prompt="Cow ID: ",
                convert_to=int,
                validation=lambda x: (0 <= x < 1000),
                err_msg="Invalid Cow ID"
            )
            current = cows.setdefault(cow_id, [])

            volume = convert_input(
                prompt="Volume: ",
                convert_to=float,
                validation=lambda x: x >= 0,
                err_msg="Invalid Volume input"
            )

            current.append(volume)
            cows[cow_id] = current

    total_vol = 0.0
    for cow in cows.values():
        total_vol += sum(cow)

    print("\n\n===== Results =====")
    print("\nTotal Volume: {} l".format(round(total_vol)))
    print("Average Volume: {} l".format(round(total_vol / len(cows.keys()))))

    print("\nCows with < 12 l for 4+ days")

    # Placeholder values
    max_vol_id = ""
    max_vol = 0.0

    for cow_id, volumes in cows.items():
        # Check if current > highest
        if sum(volumes) > max_vol:
            max_vol_id, max_vol = cow_id, sum(volumes)

        # Count days where vol < 12
        days = 0
        for i in range(int(len(volumes) / 2)):
            try:
                days += int((volumes[2 * i] + volumes[2 * i + 1]) < 12)
            except IndexError:
                days += int((volumes[2 * i]) < 12)
        days += 7 - int(len(volumes) / 2)
        if days >= 4:
            print("\x1b[31mCow {}{}\x1b[0m".format(
                "0" * (3 - len(str(cow_id))), cow_id))

    print("\x1b[92m\nCow with the most milk: Cow {}{}\x1b[0m".format(
        "0" * (3 - len(str(max_vol_id))), max_vol_id))


main({})
