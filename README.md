# most-active-cookie
CLI for finding the most active cookies from log files

## Installation
1. Clone this repo
```
$ git clone git@github.com:william-galvin/most-active-cookie.git
$ cd most-active-cookie
```
1. Install dependencies and CLI with pip
```
pip install -r requirements.txt
pip install -e .
```

## Usage
```
$ most_active_cookie [file].csv -d [date]
```
Where `file` is a csv file in the following format:
| cookie           | timestamp |
| -------          | --------- |
| 4sMM2LxV07bPJzwf | 2018-12-08T21:30:00+00:00 |
| ...              | ...  |
Here, `cookie` is an arbitrary string and `timestamp` is in the [UTC format](https://en.wikipedia.org/wiki/ISO_8601).

The `date` parameter for the `-d` flag should be in the form yyyy-mm-dd. 

The program will output to stdout the most commom cookie(s) for the specified date.
