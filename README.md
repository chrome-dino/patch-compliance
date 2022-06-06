# Patch Compliance

Patch Compliance is a tool that is used to ensure that your networks windows devices are updated to the latest versions. The tool will automatically search for the latest released Windows Patches from a wide list of Windows operating systems. This will be compared against the patch status of your network and will produce a report that shows any missing patches, along with their corresponding devices, so an administrator can quickly identify problem areas and provide fixes. The tool is best used as a scheduled job so that it can retrieve the latest patch data on a regular basis. 


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
$ git clone https://github.com/chrome-dino/patch_compliance.git

# From the directory containing your git projects
$ pip install -e patch_compliance
```

Populate the included hosts.txt file or a text file of your choosing with a line separated list of IPs/FQDNs and OSs. The format of each line should be as follows: IP/OS. If using your own file be sure to use the host file flag.

The following are valid OS names:
* Windows XP
* Windows XP x64 Edition
* Windows Vista
* Windows 7
* Windows 8
* Windows 10
* Windows Server 2003
* Windows Server 2003 R2
* Windows Server 2008
* Windows Server 2008 R2
* Windows Server 2012
* Windows Server 2012 R2
* Windows Server 2016
* Windows Server 2019

Uses the following non standard libraries:
* bs4

Requires the following:
* PowerShell


## How To Use

### Help Menu

```bash
usage: __main__.py [-h] [-f FILE] -o OPERATING_SYSTEMS

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Name of the host file containing line seperated list
                        of IPs or FQDNs. Defaults to hosts.txt
  -o OPERATING_SYSTEMS, --operating_systems OPERATING_SYSTEMS
                        Comma seperated list of operating systems. Valid OSs
                        are as follows: 'Windows XP','Windows XP x64
                        Edition','Windows Vista','Windows 7','Windows
                        8','Windows 10','Windows Server 2003','Windows Server
                        2003 R2','Windows Server 2008','Windows Server 2008
                        R2','Windows Server 2012','Windows Server 2012
                        R2','Windows Server 2016','Windows Server 2019'
```

### Video
* https://youtu.be/ENCz8EvVfuc

### Examples

```bash
# run the report generator with a standard user
$ py -m patch_compliance -f hosts.txt -o "Windows 7, Windows Server 2003 R2"
```


## Notes

* Tested on python 3.10.4


## License

MIT
