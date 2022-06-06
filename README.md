# Patch Compliance

Patch Compliance is a tool that is used to ensure that your networks windows devices are updated to the latest versions. The tool will produce a report that shows any missing patches, along with their corresponding devices, so an administrator can quickly identify problem areas and provide fixes. The tool is best used as a scheduled job so that it can retrieve the latest patch data on a regular basis. 


## Table of Contents

* <a href="#key-features">Key Features</a></br>
* <a href="#installation">Installation</a></br>
* <a href="#how-to-use">How To Use</a> </br>
* <a href="#notes">Notes</a></br>
* <a href="#license">License</a>


## Key Features

* Gather patch data of devices within a network
* Collect the latest patch data from Windows
* Compares device patch data against an official patch list to identify potential gaps 
* Outputs a report identifying devices with missing patches


## Installation

```bash
# Clone this repository
$ git clone https://github.com/chrome-dino/mysql_enumerator.git

# From the directory containing your git projects
$ pip install -e mysql_enumerator

Uses the following non standard libraries:
* bs4

Requires the following:
* PowerShell


## How To Use

### Help Menu

```bash
usage: __main__.py [-h] -db HOSTNAME -u USERNAME -p PASSWORD [-port PORT] [-s SCHEMA] [-t TABLE] [-a | --admin | --no-admin]
                   [-v | --verbose | --no-verbose]

options:
  -h, --help            show this help message and exit
  -db HOSTNAME, --hostname HOSTNAME
                        IP address or hostname of the target database
  -u USERNAME, --username USERNAME
                        Login username
  -p PASSWORD, --password PASSWORD
                        Login Password
  -port PORT, --port PORT
                        Port number (Defaults to 3306)
  -s SCHEMA, --schema SCHEMA
                        Name of the schema to be used in table extraction mode. Requires the table option
  -t TABLE, --table TABLE
                        Name of the table to be used in table extraction mode. Requires the schema option
  -a, --admin, --no-admin
                        Enable admin mode to extract database user info. Requires admin credentials
  -v, --verbose, --no-verbose
                        List additional details in the user report
```

### Video
* https://youtu.be/ENCz8EvVfuc

### Examples

```bash
# run the report generator with a standard user
$ py -m mysql_enumerator -db hostname -u user -p password

# run the report generator with elevated permissions and extract info on database users
$ py -m mysql_enumerator -db hostname -u root -p password -a

# extract the rows from a table
$ py -m mysql_enumerator -db hostname -u user -p password -s schema_name -t table_name1,table_name2
```


## Notes

* Tested on python 3.10.4


## License

MIT
