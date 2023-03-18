#!/usr/bin/env python3

import sys
import getopt
import gpt
import os

# defining a function to create the prompt from the system message and the messages


def main(argv):
    input_file = os.getenv('INPUT_TOPIC-FILE', "")
    output_dir = os.getenv('INPUT_OUTPUT-DIR', "")

    print(">>>>>>>>>>>>>>")
    print(os.getenv("OPENAI_API_BASE"))
    print(">>>>>>>>>>>>>>")

    opts, args = getopt.getopt(argv, "hi:o:", ["input_file=", "output_dir="])
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -i <input_file> -o <output_dir>')
            sys.exit()
        elif opt == '--help':
            print('main.py --input_file <input_file> --output_dir <output_dir>')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            input_file = arg
        elif opt in ("-o", "--output_dir"):
            output_dir = arg

    if (input_file == ""):
        print('Missing required Input file, please run -h or --help for more information')
        sys.exit()

    if (output_dir == ""):
        output_dir = ".out"

    gpt.generate_response(input_file, output_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
