from iris_analysis.io import load, save
from iris_analysis import calculate
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path_to_file')
parser.add_argument('path_to_results')
args = parser.parse_args()


def run_analysis(path_to_file, path_to_results):
    print(path_to_file, path_to_results)
    df = load.load_df(path_to_file)
    df_results = calculate.calc(df)
    save.save_df(df_results, path=path_to_results)


if __name__ == "__main__":
    run_analysis(args.path_to_file, args.path_to_results)
