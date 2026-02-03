"""
packet_sniffer.py
-----------------
Main controller for the Network Protocol Analyzer.
Includes DNS latency measurement.
"""

from scapy.all import sniff
from protocol_analyzer import analyze_packet
from metrics import print_metrics
from visualizer import plot_protocol_distribution
import time


packet_counts = {
    "TCP": 0,
    "UDP": 0,
    "HTTP": 0,
    "DNS": 0,
    "ICMP": 0,
    "OTHER": 0
}

total_bytes = 0
start_time = time.time()

# Store DNS request timestamps
dns_requests = {}

# Store measured DNS latencies
dns_latencies = []


def packet_handler(packet):
    global total_bytes

    protocol, size, dns_id, is_dns_response = analyze_packet(packet)

    packet_counts[protocol] = packet_counts.get(protocol, 0) + 1
    total_bytes += size

    current_time = time.time()

    # ---------------- DNS LATENCY LOGIC ----------------
    if protocol == "DNS" and dns_id is not None:

        # DNS Request
        if not is_dns_response:
            dns_requests[dns_id] = current_time

        # DNS Response
        else:
            if dns_id in dns_requests:
                latency = current_time - dns_requests[dns_id]
                dns_latencies.append(latency)
                del dns_requests[dns_id]

    elapsed = current_time - start_time
    throughput = total_bytes / elapsed if elapsed > 0 else 0

    print_metrics(packet_counts, throughput, dns_latencies)


if __name__ == "__main__":

    print("=" * 55)
    print(" Advanced Network Protocol Analyzer (with Latency)")
    print(" Press CTRL+C to stop")
    print("=" * 55)

    try:
        sniff(prn=packet_handler, store=False)

    except KeyboardInterrupt:
        print("\nStopping capture...")
        plot_protocol_distribution(packet_counts)
