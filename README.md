This is a python script that lets users quickly view their database table schema. I wrote this as a simple way to quickly view my database table columns.

## Installation

```sh
pip install git+https://github.com/rrickgauer/tables.git
```

## Usage

To see a list of all your connections:

```sh
tables list
```

To add a new connection:

```sh
tables add
```

To delete a connection:

```sh
tables delete
```

To view the tables of a connection:

```sh
tables view
```


### View Command

There are several different options for viewing a database schema.

#### Tables/Views

List all tables and views:

```sh
tables view -n connection_name
```

Dump schemas of both tables and views:

```sh
tables view -n connection_name [-a,--all]
```

Dump schemas of tables:

```sh
tables view -n connection_name [-t,--tables]
```

Dump schemas of views:

```sh
tables view -n connection_name [-v,--views]
```

#### Save output to file

To write the output to a file, you can use the `-o,--output` flag:

```sh
tables view -n connection_name --output /desktop/tables-output.txt
```

#### Format

You can specify the format of the output by using the `-f,--format` option:

```sh
tables view -n connection_name {-f,--format} format_value
```

Currently, there are 4 options you can choose from:

1. table (default)
1. markdown
1. html
1. json


## Additional notes

This script stores the data needed to access your mysql database onto a file called ```.tables.config```. It is located the same directory as the ```tables.py```. If the configuration file does not exist, the script will prompt the user to enter info needed to connect to the database. The info is stored as plain text, so if you are worried about having your password, username, host, or database name stored on a plain text file, this is not the right option for you. I added ```.tables.config``` to the .gitignore file so the configuration file will never be accidentally pushed onto a public repo.

Pull requests are welcome!
