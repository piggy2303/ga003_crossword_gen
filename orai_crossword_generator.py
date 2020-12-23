import subprocess
import numpy as np
import os
import argparse

if __name__ == '__main__':
    # parsing arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--word_list',
                        type=str,
                        default='word_list.txt',
                        help='path to word list txt file')

    parser.add_argument('--owner',
                        type=str,
                        default='Orai',
                        help='to set the name of owner')

    parser.add_argument('--grid_size',
                        type=int,
                        default="17",
                        help='grid_size of crossword.')

    parser.add_argument('--number',
                        type=int,
                        default="20",
                        help='Number of words to be used.')

    args = parser.parse_args()

    string_command_line = ["genxword",
                           args.word_list,
                           "n",
                           "-o",
                           args.owner,
                           "--grid_size",
                           str(args.grid_size),
                           "--number",
                           str(args.number)]

    string_command_line = " ".join(string_command_line)

    # os.system(string_command_line)
    output = subprocess.check_output(string_command_line, shell=True)
    output = output.decode()
    output = output.split("\n")
    print(output[1:args.grid_size+1])

    arr = []

    for line in output[1:args.grid_size+1]:
        line = line.split(" ")[:-1]
        arr.append(line)

    arr = np.array(arr)
    print(arr.shape, arr)
