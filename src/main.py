#!/usr/bin/env python3

import sys
import getopt
import gpt
import os

# defining a function to create the prompt from the system message and the messages


def main(argv):
    input_files = os.getenv('INPUT_TOPIC-FILES', "").split(",")
    output_dir = os.getenv('INPUT_OUTPUT-DIR', "")
    remove_prefix = os.getenv('INPUT_REMOVE-PREFIX', "")

    opts, args = getopt.getopt(argv, "hi:o:", ["input_file=", "output_dir="])
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <input_file> -o <output_dir>')
            sys.exit()
        elif opt == '--help':
            print('main.py --input_file <input_file> --output_dir <output_dir>')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            if (len(arg.split(',')) > 1):
                input_files.extend(arg.split(','))
            else:
                input_files.append(arg)
        elif opt in ("-o", "--output_dir"):
            output_dir = arg
        elif opt in ("-rp", "--remove_prefix"):
            remove_prefix = arg

    input_files = list(filter(None, input_files))
    if (len(input_files) == 0):
        print('Missing required Input files, please run -h or --help for more information')
        sys.exit()

    if (output_dir == ""):
        output_dir = ".out"

    print(f"Files detected: {input_files}")

    for input_file in input_files:
        gpt.generate_response(input_file, output_dir, remove_prefix)


if __name__ == "__main__":
    main(sys.argv[1:])
