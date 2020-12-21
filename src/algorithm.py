#!/usr/bin/env python3

# adding this line to test git func

import sys
import logging

log = logging.getLogger(__name__)

from math import inf


def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Pre: adjlist is not empty.
    '''
    n = adjlist.node_cardinality()
    distanceMatix = adjlist.adjacency_matrix()

    # algoritmen fungerar bara om det inte finns några loopar med sig själva
    if adjlist.self_loops() > 0:
        print("contains loops")
        return [[]]

    # puting zeros in loops
    for index in range(n):
        distanceMatix[index][index] = 0

    # the algoritmen
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distanceMatix[i][j] = min(
                    distanceMatix[i][j], distanceMatix[i][k] + distanceMatix[k][j])
                print(distanceMatix[i][j])

    return distanceMatix


def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Pre: adjlist is not empty.
    '''
    n = adjlist.node_cardinality()
    distanceMatix = adjlist.adjacency_matrix()

    # algoritmen fungerar bara om det inte finns några loopar med sig själva
    if adjlist.self_loops() > 0:
        print("contains loops")
        return [[]]

    # puting zeros in loops
    for index in range(n):
        distanceMatix[index][index] = 0

    # the algoritmen
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distanceMatix[i][j] = min(
                    distanceMatix[i][j], distanceMatix[i][k] + distanceMatix[k][j])
                if distanceMatix[i][j] is not inf:
                    distanceMatix[i][j] = True

    return distanceMatix
    

def dijkstra(adjlist, start_node):
    '''
    Returns the result of running Dijkstra's algorithm as two N-length lists:
    1) distance d: here, d[i] contains the minimal cost to go from the node
    named `start_node` to the i:th node in the adjacency list.
    2) edges e: here, e[i] contains the node name that the i:th node's shortest
    path originated from.

    If the index i refers to the start node, set the associated values to None.

    Pre: start_node is a member of adjlist.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 2
    b|* * 2
    c|* * *

    For start node "a", the expected output would then be:

    d: [ None, 1, 2]
    e: [ None, 'a', 'a' ]
    '''
    log.info("TODO: dijkstra()")
    d = []
    e = []
    return d, e


def prim(adjlist, start_node):
    '''
    Returns the result of running Prim's algorithm as two N-length lists:
    1) lowcost l: here, l[i] contains the weight of the cheapest edge to connect
    the i:th node to the minimal spanning tree that started at `start_node`.
    2) closest c: here, c[i] contains the node name that the i:th node's
    cheapest edge orignated from. 

    If the index i refers to the start node, set the associated values to None.

    Pre: adjlist is setup as an undirected graph and start_node is a member.

    === Example ===
    Suppose that we have the following adjacency matrix:

      a b c
    -+-----
    a|* 1 3
    b|1 * 1
    c|3 1 *

    For start node "a", the expected output would then be:
    Note: easiest example, what if it goes backwards? e.g, start_node = b

    l: [ None, 1, 1]
    c: [ None, 'a', 'b' ]
    '''
    '''

    current_node = start_node

    '''
    n = adjlist.node_cardinality()
    weightMatix = adjlist.adjacency_matrix()

    node_name = adjlist.list_nodes()

    added_nodes = []
    l = []
    c = []
    for i in range(n):
        l.append(inf)
        c.append(inf)

    print(l)
    print(c)

    added_nodes.append(start_node)
    start_index = adjlist._findIndex(start_node)
    current_node = start_node
    #idea: rearange the matrix so that the start node is to the left

    #if start_node is not at the first pos in matrix    

    for i in range(n):
        shortest_weight = inf
        shortest_to_node = None
        for j in range(n):
            #find shortest path
            if weightMatix[i][j] < shortest_weight and node_name[j] not in added_nodes:
                shortest_weight = weightMatix[i][j]
                shortest_to_node = node_name[j]
        added_nodes.append(shortest_to_node)
        #print(shortest_weight)
        if shortest_weight is inf or node_name[i] == start_node:
            l[adjlist._findIndex(current_node)] = None
        else:
            l[adjlist._findIndex(current_node)] = shortest_weight
        #print(shortest_to_node)
        if shortest_weight is not inf:
            c[adjlist._findIndex(current_node)] = node_name[i]
        elif node_name[i] == start_node:
            c[adjlist._findIndex(current_node)] = None
        else:
            c[adjlist._findIndex(current_node)] = None
        current_node = shortest_to_node
    
    return l, c


if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
