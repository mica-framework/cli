# The MiCA-CLI

## Requirements
You can run the script with Python 2.7 but Python 3.5 and above is recommended.

## How to run the CLI
Currently there's only the option on running the CLI under a unix-like command line tool.
That means, you need a linux or mac-os operating system which natively integrates such terminals.
The second approach is to use cmder or something like that on windows.

Running the CLI can be done within the following four steps. Therefore you need to clone this repo to your local machine.
Finally run the following steps within your console:
```python
# 1 - Start by creating a virutal environment within the CLI project
$ python -m virtuelenv .env   # with python2.7
$ python3 -m venv .env        # with python3.X

# 2 - Activate the virutal environment
$ . .env/bin/activate     # on unix devices
$ . .env/scripts/activate # on windows

# 3 - Now install the dependencies
$ pip install -r requirements.txt

# 4 - Run the cli
$ python3 mica-cli.py
```

## License
This project is licensed under the terms of the MIT license. See the [LICENSE](https://raw.githubusercontent.com/mica-framework/cli/master/LICENSE) file.
