import csv
import os
import pandas as pd
import argparse

# init main with argparse to take in the csv file name


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", help="The name of the csv file")
    args = parser.parse_args()
    csv_file = args.csv_file

    # open the csv file using pandas
    df = pd.read_csv(csv_file)

    # create a new text file in the data folder
    with open("data/tweets.txt", "w", encoding="utf-8") as f:
        # write each tweet to the text file
        for tweet in df["tweet"]:
            f.write(tweet + "\n")


if __name__ == "__main__":
    main()
