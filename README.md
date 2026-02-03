# Advanced Network Protocol Analyzer (with Latency Measurement)

## Overview
This project is a Python-based **Network Protocol Analyzer** that captures and analyzes live network traffic.  
It identifies common network protocols, measures throughput, calculates DNS and HTTP latency, and visualizes protocol distribution.


---

##  Features
- Live packet capture from network interface
- Protocol detection:
  - TCP
  - UDP
  - HTTP
  - DNS
  - ICMP
- Packet count per protocol
- Network throughput calculation
- DNS latency measurement (request–response based)
- HTTP latency estimation (flow-based)
- Graphical visualization of protocol distribution

---

## How Latency is Measured

### DNS Latency
- DNS requests and responses share a **transaction ID**
- Latency = response time − request time
- Average DNS latency is displayed in milliseconds

### HTTP Latency
- HTTP runs over TCP and has no explicit transaction ID
- Latency is approximated as:
  - Time between first HTTP request packet
  - and first server response packet in the same TCP flow
- This approach is commonly used in passive network monitoring

---

##  Tech Stack
- **Language:** Python 3
- **Libraries:**
  - scapy
  - pyshark
  - matplotlib
- **Tools:**
  - Wireshark / tshark (backend)

---

## Project Structure
