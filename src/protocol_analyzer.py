"""
protocol_analyzer.py
--------------------
Analyzes a captured network packet and identifies
its protocol and relevant metadata.
"""

from scapy.layers.inet import TCP, UDP, ICMP
from scapy.layers.dns import DNS
from scapy.layers.http import HTTPRequest


def analyze_packet(packet):
    """
    Analyze a Scapy packet and identify protocol details.

    Returns:
    protocol (str)
    size (int)
    dns_id (int or None)
    is_dns_response (bool)
    """

    size = len(packet)

    # Default values
    dns_id = None
    is_dns_response = False

    # ---------------- DNS ----------------
    if packet.haslayer(DNS):
        dns_layer = packet[DNS]
        dns_id = dns_layer.id

        # qr = 0 → request, qr = 1 → response
        is_dns_response = bool(dns_layer.qr)

        return "DNS", size, dns_id, is_dns_response

    # ---------------- HTTP ----------------
    if packet.haslayer(TCP) and packet.haslayer(HTTPRequest):
        return "HTTP", size, None, False

    # ---------------- TCP ----------------
    if packet.haslayer(TCP):
        return "TCP", size, None, False

    # ---------------- UDP ----------------
    if packet.haslayer(UDP):
        return "UDP", size, None, False

    # ---------------- ICMP ----------------
    if packet.haslayer(ICMP):
        return "ICMP", size, None, False

    return "OTHER", size, None, False
