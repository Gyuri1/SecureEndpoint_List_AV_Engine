#!/usr/bin/env python3

'''
This script will list the Tetra engine version of a Secure Endpoint.
This script works in US / NAM Secure Endpoint Cloud.
Please update the region based on Your preference!

More information:
https://developer.cisco.com/docs/secure-endpoint/#!authentication
https://developer.cisco.com/docs/secure-endpoint/#

'''

import requests
import json
import sys

# API
#Please update these values according to this doc:
#https://developer.cisco.com/docs/secure-endpoint/#!authentication

#
# https://{your_client_id}:{your_api_key}@{api_endpoint}/{api_version}/{resource}
#

CLIENT_ID = "XXX"
API_KEY = "YYY"

# Base URL for the Cisco Secure Endpoint API
BASE_URL = 'https://api.amp.cisco.com/v1/'

def get_computers():
    url = f"{BASE_URL}computers"
    response = requests.get(url, auth=(CLIENT_ID, API_KEY))
    
    if response.status_code == 200:
        computers = response.json()
        return computers
    else:
        print(f"Failed to retrieve computers: {response.status_code}")
        return None

def print_computer_data(computers):
    if 'data' in computers:
        for computer in computers['data']:

            #print(computer)
            print(f"Hostname: {computer.get('hostname', 'N/A')}")
            print(f"Operating System: {computer.get('operating_system', 'N/A')}")
            print(f"Connector GUID: {computer.get('connector_guid', 'N/A')}")
            print(f"Active: {computer.get('active', 'N/A')}")

            av_update = computer.get('av_update_definitions', {})
            if av_update:
                print(f"AV Status: {av_update.get('status', 'N/A')}")
                print(f"Detection Engine: {av_update.get('detection_engine', 'N/A')}")
                print(f"Version: {av_update.get('version', 'N/A')}")
                print(f"Updated At: {av_update.get('updated_at', 'N/A')}")
            print("-" * 40)
    else:
        print("No computers found")

if __name__ == "__main__":
    computers = get_computers()
    if computers:
        print_computer_data(computers)
