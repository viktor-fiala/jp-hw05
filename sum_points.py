import argparse
import pathlib
import json
from data.dataframe import DataFrame

# Načtení argumentů ze vstupu
parser = argparse.ArgumentParser()

parser.add_argument("--output", required=True)
args = parser.parse_args()

# Výpočet počtu studentů, kteří splnili zadaný úkol
result = {}


def dictionary_add(dic, key, val):
    """adds val to the existing value if key exists, otherwise adds new key and value to the dictionary"""
    try:
        dic[key] += val
    except KeyError:
        dic[key] = val


files = pathlib.Path("results").rglob("*.csv")

for file in files:
    if file.is_file():
        df = DataFrame.from_csv(file)

        for idx, val in df.items():
            if idx == "Splněno":
                continue
            # přetypování bodů na int
            new_val = val.apply(lambda x: 0 if x == "" else int(x))

            # sečtení bodů
            new_sum = new_val.sum()
            dictionary_add(result, idx, new_sum)

# Zapsání do výstupního souboru ve formátu JSON
path = pathlib.Path(args.output)
with path.open(mode="w", encoding="utf-8") as file:
    json.dump(result, file)

print(result)
