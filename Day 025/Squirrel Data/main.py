#!/usr/bin/env python
import os

import pandas as pd

DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    '2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240926.csv'
)


def main() -> None:
    squirrel_data = pd.read_csv(DATA_PATH)

    fur_color = squirrel_data \
        .groupby('Primary Fur Color').size() \
        .reset_index(name='Count') \
        .rename(columns={'Primary Fur Color': 'Fur Color'})
    # print(fur_color)

    fur_color.to_csv(
        os.path.join(os.path.dirname(__file__), 'fur_color_data.csv'),
        index=False)


if __name__ == '__main__':
    main()
