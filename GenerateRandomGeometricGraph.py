# -*- coding: utf-8 -*-

# Author: Zhihao Qiu
# Date  : 09/03/2023
import json

import networkx as nx
import time
import matplotlib.pyplot as plt
import numpy as np


def generate_RGG():
    time_start = time.time()
    G = nx.random_geometric_graph(10000, 0.2)

    time_end = time.time()
    print('time cost', time_end - time_start, 's')

    # Get the (x,y) positions of each node from the "pos" attribute
    # node_pos = nx.get_node_attributes(G, 'pos')
    # # another method to get pos
    # # pos = G.nodes._nodes
    # # pos1 = {key: tuple(value['pos']) for key, value in pos.items()}
    #
    # # Draw the graph using the (x,y) positions
    # fig, ax = plt.subplots()
    # nx.draw(G, pos=node_pos, with_labels=True, ax=ax)
    #
    # # Set the x and y limits of the plot based on the node positions
    # x_vals = [pos[0] for _, pos in node_pos.items()]
    # y_vals = [pos[1] for _, pos in node_pos.items()]
    # plt.xlim(min(x_vals) - 0.1, max(x_vals) + 0.1)
    # plt.ylim(min(y_vals) - 0.1, max(y_vals) + 0.1)
    #
    # # Turn on axes
    # limits = plt.axis('on')
    # ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
    #
    # # Show the plot
    # plt.show()

    # # save data
    # with open('C:\data\geometric shortest path problem\RGG\RGG1POSITION.txt','w') as f:
    #     f.write(json.dumps(pos1))
    # nx.write_edgelist(G,'C:\data\geometric shortest path problem\RGG\RGG1.txt')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_RGG()

