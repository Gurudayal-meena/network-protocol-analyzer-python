"""
visualizer.py
-------------
This module visualizes network statistics
using graphical plots.
"""

import matplotlib.pyplot as plt


def plot_protocol_distribution(packet_counts):
    """
    Plot a bar graph showing protocol-wise packet distribution.

    Parameters:
    packet_counts (dict): Protocol-wise packet count
    """

    # Extract protocol names and their counts
    protocols = list(packet_counts.keys())
    counts = list(packet_counts.values())

    # Create a bar graph
    plt.figure()
    plt.bar(protocols, counts)

    # Label the axes
    plt.xlabel("Network Protocol")
    plt.ylabel("Number of Packets")

    # Title of the graph
    plt.title("Protocol Distribution in Network Traffic")

    # Display the graph
    plt.show()
