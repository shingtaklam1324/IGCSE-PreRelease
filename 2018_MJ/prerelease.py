# 2018 May/June CIE Comp Sci IGCSE Pre Release

if __name__ == "__main__":
    cows = {}

    num_cows = int(input("Num of Cows: "))

    for i in range(14):
        print("Day {} {}".format(int(i / 2) + 1, "Morning" if i %
                                 2 == 0 else "Afternoon"))
        for c in range(num_cows):
            # If cow is in dict, use current, otherwise insert new list
            cow_id = input("Cow ID: ")
            current = cows.setdefault(cow_id, [])

            volume = float(input("Volume of milk: "))

            current.append(volume)
            cows[cow_id] = current

    total_vol = 0.0
    for cow in cows.values():
        total_vol += sum(cow)

    print("Total Volume: {} l".format(round(total_vol)))
    # Average = total / num of cows
    print("Average Volume: {} l".format(round(total_vol / len(cows.keys()))))

    print("Cows with < 12 l for 4+ days")

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
        if days >= 4:
            print("Cow {}".format(cow_id))

    print("Cow with the most milk: Cow {}".format(max_vol_id))
