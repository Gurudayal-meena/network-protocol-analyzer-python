"""
metrics.py
----------
Displays network performance metrics including latency.
"""

def print_metrics(packet_counts, throughput, dns_latencies):
    print("\n----------- Network Metrics -----------")

    for protocol, count in packet_counts.items():
        print(f"{protocol:6}: {count} packets")

    print(f"\nThroughput : {throughput:.2f} bytes/sec")

    if dns_latencies:
        avg_latency = sum(dns_latencies) / len(dns_latencies)
        print(f"Avg DNS Latency : {avg_latency * 1000:.2f} ms")

    print("---------------------------------------")
