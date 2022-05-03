# tables

This is a python script that lets users quickly view their database table schema. I wrote this as a simple way to quickly view my database table columns.

## Installation

```sh
pip install git+https://github.com/rrickgauer/tables/tree/branch-issue-18
```

## Usage

Make sure you are in the same directory as your ```tables.py``` file. There are 2 ways to use this:

1. Print a list of all the table names
    * Similar to ```SHOW TABLES;```
2. Print a list table(s) fields and types
    * Similar to ```DESCRIBE Table;```

### Show Tables

To get a list of all the tables in your database:
```
py tables.py
```

### Describe Table(s)

To describe a single table, just include the table name in the ```--table``` argument.
```
py tables.py -t table_name
```

You can also list multiple table names:
```
py tables.py -t table_one table_two table_three
```

If you want to describe all of the tables in the database, simply use * for the table name:
```
py tables.py -t *
```

### Output

There are 3 different output options: *display*, *save*, or *both*. The corresponding argument is ```-o``` or ```--output```. It defaults to display.

The display option prints the output to your console screen:
```
py tables.py -t table_one -o display
```

The *save* option saves the output to a file called *tables.output.txt*:
```
py tables.py -t table_one -o save
```

Lastly, the *both* option prints the output to the console, and saves the output to the *tables.output.txt* file.
```
py tables.py -t table_one -o both
```

## Additional notes

This script stores the data needed to access your mysql database onto a file called ```.tables.config```. It is located the same directory as the ```tables.py```. If the configuration file does not exist, the script will prompt the user to enter info needed to connect to the database. The info is stored as plain text, so if you are worried about having your password, username, host, or database name stored on a plain text file, this is not the right option for you. I added ```.tables.config``` to the .gitignore file so the configuration file will never be accidentally pushed onto a public repo.

Pull requests are welcome!
