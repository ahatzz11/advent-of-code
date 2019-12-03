 #!/usr/bin/env python

# part one: 3402634
# part two: 5101069

import sys

def main(args):
    f = open("input.txt","r")
    instructions = f.read().split(",")

    i = 0
    for instruction in instructions:
        instructions[i] = int(instruction)
        i += 1


    current_index_offset = 0

    while(instructions[current_index_offset]):

        if(instructions[0 + current_index_offset] == 1):
            print('adding!')
            noun = instructions[instructions[1 + current_index_offset]]
            verb = instructions[instructions[2 + current_index_offset]]

            new_position = instructions[3 + current_index_offset]
            instructions[new_position] = noun + verb

        elif(instructions[0 + current_index_offset] == 2):
            print('multiplying!')
            noun = instructions[instructions[1 + current_index_offset]]
            verb = instructions[instructions[2 + current_index_offset]]

            new_position = instructions[3 + current_index_offset]
            instructions[new_position] = noun * verb

        elif(instructions[0 + current_index_offset] == 99):
            print('dead!')
            sys.exit(0)

        current_index_offset += 4
        print(instructions)

    print(instructions)



def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb


if __name__ == '__main__':
    main(sys.argv)
