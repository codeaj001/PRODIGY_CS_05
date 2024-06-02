# Packet Sniffer Tool 🚀

## Overview

The Packet Sniffer Tool is a Python-based utility that captures and analyzes network packets. It extracts and displays relevant information such as source and destination IP addresses, protocols, and payload data. This tool is useful for network administrators and security professionals to monitor and troubleshoot network traffic.

## Features ✨

- 📡 Captures network packets in real-time.
- 🗂️ Displays source and destination IP addresses.
- 🔍 Identifies protocols (TCP, UDP, ICMP, HTTP).
- 🌐 Extracts and prints HTTP request details.
- 📦 Shows payload data for deeper analysis.

## Requirements 🛠️

- 🐍 Python 3.x
- 📦 `scapy` library
- 🖥️ Npcap (for Windows users)

## Installation 🖱️

1. **Install Python 3.x**: If you don't have Python installed, download and install it from the [official Python website](https://www.python.org/).

2. **Install Scapy**: Install the `scapy` library using pip.
    ```bash
    pip install scapy
    ```

3. **Install Npcap** (Windows only): Download and install Npcap from the [Npcap website](https://nmap.org/npcap/#download). Ensure to select the option to install Npcap in "WinPcap API-compatible mode."

## Usage 🚀

1. **Clone or Download the Script**: Save the script as `packet_sniffer.py`.

2. **Run the Script with Administrator Privileges**:
   - Open Command Prompt or Terminal with administrator privileges.
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python packet_sniffer.py
     ```

3. **Output**: The script will start capturing packets and display the following information for each packet:
   - IP Source and Destination addresses.
   - Protocol type (TCP, UDP, ICMP).
   - Source and Destination ports (for TCP/UDP).
   - HTTP Method, Host, and Path (for HTTP packets).
   - Payload data.


## Troubleshooting 🛠️

- **RuntimeError: Sniffing and sending packets is not available at layer 2**: Ensure Npcap is installed correctly in "WinPcap API-compatible mode."
- **Permission Error**: Run the script with administrator privileges to allow packet capture.

## License 📜

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing 🤝

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact 📬

For issues and inquiries, please open an issue on the GitHub repository or contact the author directly.
