 #!/usr/bin/env python

# part one: 3402634
# part two: 5101069

import sys

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier



def caluclate_fuel(mass):
    first = int(mass) / 3
    second = truncate(first)
    needed_fuel = second - 2
    return needed_fuel


def main(args):
    f = open("input.txt","r")
    lines = f.readlines()

    fuel_for_fuel = 0

    # initial
    for line in lines:

        line_fuel = caluclate_fuel(int(line))
        current_fuel = caluclate_fuel(int(line))

        while (current_fuel > 0):
            if(caluclate_fuel(current_fuel) > 0):
                line_fuel = line_fuel + caluclate_fuel(current_fuel)

            current_fuel = caluclate_fuel(current_fuel)

        fuel_for_fuel = fuel_for_fuel + line_fuel

    print(fuel_for_fuel)

if __name__ == '__main__':
    main(sys.argv)
