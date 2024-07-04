# Wireless Controller AP Status Checker

This Python script allows users to connect to a Cisco Wireless LAN Controller (WLC) via SSH to retrieve and analyze the status of Access Points (APs) managed by the WLC.

## Features

- **SSH Connection**: Securely connect to your WLC using SSH.
- **AP Summary Retrieval**: Fetches a summary of all APs managed by the WLC.
- **AP Status Analysis**: Analyzes the fabric status of each AP.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- `netmiko` library installed. You can install it using pip:

  ```bash
  pip install netmiko
  ```

## Usage

To use the script, follow these steps:

Run the script from the terminal:
  
  ```bash
  python main.py
  ```

- Enter the IP address of the WLC SSH username and password (input will be hidden).

The script will then connect to the WLC, retrieve the AP summary, and perform the status analysis.
