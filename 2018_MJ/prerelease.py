# 2018 May/June CIE Comp Sci IGCSE Pre Release


def convert_input(prompt="", to=float, err_msg="Error parsing input", validation=None):
    while 1:
        try:
            value = to(input(prompt))
            if validation is not None:
                if validation(value):
                    return value
                else:
                    print(err_msg)
                    continue
            else:
                return value
        except ValueError:
            print(err_msg)
            continue

def is_gt_zero(num):
    return num > 0

if __name__ == "__main__":
    cows = {}

    num_cows = convert_input(
        prompt="Number of cows: ",
        to=int,
        validation=is_gt_zero,
        err_msg="Invalid number of cows"
    )

    for i in range(14):
        print("\n\nDay {} {}\n".format(int(i / 2) + 1, "Morning" if i %
                                 2 == 0 else "Afternoon"))
        
        for c in range(num_cows):
            # If cow is in dict, use current, otherwise insert new list
            cow_id = input("Cow ID: ")
            current = cows.setdefault(cow_id, [])

            volume = convert_input(
                prompt="Volume: ",
                to=float,
                validation=is_gt_zero,
                err_msg="Invalid Volume input"
            )

            current.append(volume)
            cows[cow_id] = current

    total_vol = 0.0
    for cow in cows.values():
        total_vol += sum(cow)

    print("\n\n===== Results =====")
    print("\nTotal Volume: {} l".format(round(total_vol)))
    # Average = total / num of cows
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
            print("Cow {}".format(cow_id))

    print("\nCow with the most milk: Cow {}".format(max_vol_id))

    # print(cows)
