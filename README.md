# final_project_wanyingli 

![](https://github.com/wanyinglixx/final_project_wanyingli/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/wanyinglixx/final_project_wanyingli/branch/main/graph/badge.svg)](https://codecov.io/gh/wanyinglixx/final_project_wanyingli) ![Release](https://github.com/wanyinglixx/final_project_wanyingli/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/final_project_wanyingli/badge/?version=latest)](https://final_project_wanyingli.readthedocs.io/en/latest/?badge=latest)

This is the final project for the Modern Data Structure course Fall 2020 at Columbia University.

Hi! Welcome to use my package. This package allows you to search for the historical country lending projects from the World Bank and the Asian Development Bank (ADB).

Context of this package: The World Bank (WB) and Asian Development Bank (ADB) are the major sources for countries in the Asia & Pacific region to get lending from. However, each bank maintains its own lending database, which makes it difficult to understand the big picture of each country --- the integrated historical lending information from all lending sources. Therefore, this package allows users to look at the cumulative lending amount a country received from the major multilateral development banks by searching a specific country code and time period.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ final_project_wanyingli
```

## Features

- TODO

## Dependencies

-Pandas
-json
-os
-requests
-numpy
-matplotlib
-pytest


## Usage

Below are some examples for the functions provided in the package.

1. Get a dataframe and print the cumulative WB project lending amount received by China from 2018-2019:
```bash
get_wb_countryyear('CN', 2018, 2019)
```

2. Get a dataframe and print the cumulative WB project lending amount with environmental cateory "B" from 2018-2019:
```bash
get_wb_environment('B', 2018, 2019)
```

3. Get a dataframe of all historical sovereign lending projects information since 2008:
```bash
get_adb_lending()
```

4. Get a dataframe and print the cumulative ADB lending amount received by China from 2018-2019:
```bash
get_adb_countryyear('CN', 2018, 2019)
```

5. Plot the top 10 receipient countries from the ADB since 2008:
```bash
plot_adb_top10()
```

## Documentation

The official documentation is hosted on Read the Docs: https://final_project_wanyingli.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/wanyinglixx/final_project_wanyingli/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
