#!/usr/bin/env python
import os
import csv

import pandas as pd

CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'weather_data.csv'
)


def main() -> None:
    # with builtin csv module
    with open(CSV_PATH) as csvfile:
        data = csv.reader(csvfile)

        next(data)  # skip the csv header in iterator
        temperatures = [int(row[1]) for row in data]

        # for row in data:
        #     print(row)

        print(temperatures)

    # with pandas
    data = pd.read_csv(CSV_PATH, header='infer')
    print(data)
    print(data.dtypes)
    print(data['temp'])


if __name__ == '__main__':
    main()
