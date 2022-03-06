import argparse
import os

# Usage: exercise_1.py [-h] [-i INPUT] [-n NUM] [-o OUTPUT]
#
# optional arguments:
# -h, --help            show this help message and exit
# -i INPUT, --input INPUT
# -n NUM, --num NUM
# -o OUTPUT, --output OUTPUT


def checker(input_file):
        assert os.path.isfile(input_file), argparse.ArgumentTypeError


parser = argparse.ArgumentParser()
parser.add_argument("--input", help="file to be read", type=checker)
parser.add_argument("--output", help="file to save result")
parser.add_argument(
    "--num", type=int, default=10,  help="integer number"
)

args = parser.parse_args()


def print_values(input, output, num):
    print(input, output, num)


if __name__ == "__main__":
    print_values(args.input, args.output, args.num)


