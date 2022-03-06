import argparse

# Usage: exercise_1.py [-h] [-i INPUT] [-n NUM] [-o OUTPUT]
#
# optional arguments:
# -h, --help            show this help message and exit
# -i INPUT, --input INPUT
# -n NUM, --num NUM
# -o OUTPUT, --output OUTPUT


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="file to be read")
parser.add_argument("-o", "--output", help="file to save result")
parser.add_argument(
    "-n", "--num", type=int, default=10,  help="integer number"
)

args = parser.parse_args()


def print_values(input, output, num):
    print(input, output, num)


if __name__ == "__main__":
    print_values(args.input, args.output, args.num)
