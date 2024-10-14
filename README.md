# Secure Endpoint Computer Data Script

This Python script retrieves and displays computer data from Cisco Secure Endpoint systems.


## Installation:

1. **Download Files**: 
   Download all the files from this repository.

2. **Install Dependencies**: 
   Ensure you have the `requests` package installed. You can install it using pip:

   ```sh
   pip install requests
   ```
##  Usage:  


   ```sh
   python3 secureendpoint_list_computer.py
   ```

For example:


   ```sh
----------------------------------------  
Hostname: WINDOWS-VICTIM  
Operating System: Windows 11, SP 0.0 (Build 22000.2538)
Connector GUID: XXX-YYY-XXX
Active: True
----------------------------------------
Hostname: MacBook Air
Operating System: macOS 14.6.1
Connector GUID: AAAA-BBB-CCC
Active: True
AV Status: Definitions Up To Date
Detection Engine: ClamAV
Version: 2049
Updated At: 2024-10-12T20:33:33+00:00
----------------------------------------
   ```



