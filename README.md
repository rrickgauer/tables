# tables

This is a python script that lets users quickly view their database table schemas. I wrote this as a simple way to quickly view my database table columns.

## Installation

Go to your directory and download/clone this repository via:
```
git clone https://github.com/rrickgauer/tables.git
```

## Usage

Make sure you are in the same directory as your ```tables.py``` file. There are 2 ways to use this:

1. Print a list of all the table names
    * Similar to ```SHOW TABLES;```
2. Print a list table(s) fields and types
    * Similar to ```DESCRIBE Table;```

### Show Tables

```
py tables.py
```

### Describe Table(s)

```
py tables.py -t table_name
```

You can also list multiple table names:
```
py tables.py -t table_one table_two table_three
```

## Additional notes

This script stores the data needed to access your mysql database onto a file called ```.tables.config```. It is located the same directory as the ```tables.py```. If the configuration file does not exist, the script will prompt the user to enter info needed to connect to the database. The info is stored as plain text, so if you are worried about having your password, username, host, or database name stored on a plain text file, this is not the right option for you. I added ```.tables.config``` to the .gitignore file so the configuration file will never be accidently pushed onto a public repo.

Pull requests are welcome!
