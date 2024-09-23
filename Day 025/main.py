#!/usr/bin/env python
import os
# import csv

import pint
import pandas as pd
import numpy as np

CSV_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'weather_data.csv'
)


def main() -> None:
    # with builtin csv module
    # with open(CSV_PATH) as csvfile:
    #     data = csv.reader(csvfile)

    #     next(data)  # skip the csv header in iterator
    #     temperatures = [int(row[1]) for row in data]

    #     # for row in data:  # iterator already consumed by list comprehension
    #     #     print(row)

    #     print(temperatures)

    # with pandas
    data = pd.read_csv(CSV_PATH, header='infer')
    print(data)
    # print(data.dtypes)
    # print(data['temp'])

    data_dict = data.to_dict()
    print(data_dict)

    # avg_temp = data['temp'].mean()  # alternative
    temperatures = data['temp'].to_list()
    avg_temp = np.mean(temperatures)
    print(round(avg_temp, 2))

    print(data[data['temp'] == data['temp'].max()])

    print(convert_to_farenheit(data[data.day == 'Monday']['temp'][0]))


def convert_to_farenheit(temperature: float) -> float:
    ureg = pint.UnitRegistry()
    temperature_celsius = temperature * ureg.degC

    return round(temperature_celsius.to('degF'), 1)


if __name__ == '__main__':
    main()
