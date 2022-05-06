# tables

This is a python script that lets users quickly view their database table schema. I wrote this as a simple way to quickly view my database table columns.

## Installation

```sh
pip install git+https://github.com/rrickgauer/tables.git
```

## Usage

To run:

```sh
tables [list, view, delete, add]
```


## Additional notes

This script stores the data needed to access your mysql database onto a file called ```.tables.config```. It is located the same directory as the ```tables.py```. If the configuration file does not exist, the script will prompt the user to enter info needed to connect to the database. The info is stored as plain text, so if you are worried about having your password, username, host, or database name stored on a plain text file, this is not the right option for you. I added ```.tables.config``` to the .gitignore file so the configuration file will never be accidentally pushed onto a public repo.

Pull requests are welcome!
