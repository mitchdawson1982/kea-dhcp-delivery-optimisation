# Kea dhcp Delivery Optimisation
 
This repo is a tool for applying custom dhcp option data configuration as required for delivery optimisation (option 234) into an existing kea dhcp json file.
The tool generates a unique GUID per FITS WAN site id (FITS_ID).

## Requirements
Python 3.5 or higher

## Getting Started

1) Install Python3 (3.5 or higher) from https://python.org or locate an existing installation. 
2) Clone the repository
3) Rename your input dhcp json file to 'kea_dhcp_input.json' and place it within the config folder.
4) CD into the repository
5) Run 
'''path-to-python-executable main.py'''
6) The output file will be presented as follows 'config\kea_dhcp_ouput.json'