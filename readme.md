# Descriptive Statistics Analyzer
### (Optimized for mobile devices experience)

## Author: M. MAD
### License: GPL3+

## Installation
It's simple for PCs, you need to have Python 3 installed on your system and
then installing `prettytable` library using `pip`:
```shell
python3 -m pip install -U prettytable
```
And then just running the main.py file with Python:
```shell
python3 main.py
```

For Android devices there are two ways to install and use this program, one is
[using the Termux app](docs/installation_on_android_(termux).md) (the
recommended way) and the other is
[using PyDroid3](docs/installation_on_android_(pydroid3).md).

## Usage
Just replace `data` variable's value and adjust the `data_type` and
`number_of_classes` variables accordingly and then run the script to get the
full statistic report.

In case of `Continuous` data_type, setting `precise_intervals` determines that
intervals between each class should be rounded (`False` value) or kept as
float (`True` value). Setting `calculate_q` and `calculate_d` values make the
program calculate and print Quartiles and Deciles of `Continuous` data.

## Acknowledges
This program was made possible by the work of [PrettyTable](https://github.com/jazzband/prettytable) contributors.