# Patch Compliance

Patch Compliance is a tool that is used to ensure that your networks windows devices are updated to the latest versions. The tool will produce a report that shows any missing patches, along with their corresponding devices, so an administrator can quickly identify problem areas and provide fixes. The tool is designed to be run as a scheduled job so that it can retrieve the latest patch data on a regular basis. 


## Table of Contents

* <a href="#key-features">Key Features</a></br>
* <a href="#installation">Installation</a></br>
* <a href="#notes">Notes</a></br>
* <a href="#license">License</a>


## Key Features

* Gather patch data of devices within a network
* Collect the latest patch data from Windows
* Compares device patch data against an official patch list to identify potential gaps 
* Outputs a report identifying devices with missing patches


## Installation

1. Populate the hosts.txt file with a list of fqdns or IPs, one per line
2. Open the Windows Task Scheduler
3. In the directory menu on the left, right click the task scheduler library and create a new folder for your job
4. With the new folder selected, click the create task option in the action menu
5. In the general tab, fill out the name and select a user or group. It is reccommended to use a service account
6. In the triggers tab, click new and choose a trigger to start the job. It is reccommended to use a timed schedule and run it once a day
7. In the actions tab, click new and select the start a program option
8. Add '/k c:\PATH TO SCRITPS\patch_batch.bat' to the arguments and click finish


Uses the following non standard libraries:
* pandas
* pymysql
* setuptools
* cryptography
* openpyxl
* 

### Video
* https://youtu.be/ENCz8EvVfuc


## Notes

* Tested on python 3.10.4


## License

MIT
