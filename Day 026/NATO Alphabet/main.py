#!/usr/bin/env python
import sys
from os.path import join, abspath, dirname

import pandas as pd

from utils import check_input

NATO_CSV = join(dirname(abspath(__file__)), 'utils/nato_phonetic_alphabet.csv')


def main() -> None:
    nato_df = pd.read_csv(NATO_CSV)
    phonetic_dict = {row.letter: row.code for _, row in nato_df.iterrows()}

    word = check_input("Insert a word: ", lambda x: x.isalpha()).upper()
    phonetic_word = [phonetic_dict.get(letter) for letter in word]

    print(f"The phonetic code is: {phonetic_word}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
