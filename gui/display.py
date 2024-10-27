"""
Module for displaying matplotlib graphs
Using: matplotlib, numpy
"""

import fastf1.plotting as f1plt
import matplotlib.pyplot as plt


def convert_abb_to_color(abb):
    return f1plt.DRIVER_COLORS[f1plt.DRIVER_TRANSLATE[abb]]


def draw_max_speeds(speeds):
    """
    :param speeds: dict [abb:speed]
    :return: nothing
    """
    # offset is used to get some tolerance for the lower and upper value of tha graph, so min value sint nothing
    offset = 10
    # colors for the tower graphs with driver colors
    color = [convert_abb_to_color(abb) for abb in speeds]

    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(speeds.keys(), speeds.values(), color=color, width=0.8)
    plt.ylim(min(speeds.values()) - offset, max(speeds.values()))

    plt.show()
