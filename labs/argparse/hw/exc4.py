import argparse
import os
import configparser

# Usage: exercise_1.py [-h] [-i INPUT] [-n NUM] [-o OUTPUT]
#
# optional arguments:
# -h, --help            show this help message and exit
# -i INPUT, --input INPUT
# -n NUM, --num NUM
# -o OUTPUT, --output OUTPUT


dir_name = os.path.dirname(__file__)
parser = argparse.ArgumentParser()
parser.add_argument(
    "--config_file", help="config file", default='sample_config.ini')

args = parser.parse_args()

config = configparser.ConfigParser()
config.read(os.path.join(dir_name, f"../sample_code/{args.config_file}"))



parser.add_argument(
    "--input", help="file to be read", default=config["default"]["input_file"])
parser.add_argument(
    "--output", help="file to save result", default=config["default"]["result_file"])
parser.add_argument(
    "--num", type=int, default=config["default"]["count_lines"],  help="integer number")

args = parser.parse_args()


def print_values(input, output, num):
    print(input, output, num)


if __name__ == "__main__":
    print_values(args.input, args.output, args.num)


