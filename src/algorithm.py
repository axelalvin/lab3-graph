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


def indexfromword(word):
    #
    # OM NODEerna inte är i boksatvsordning funkar det inte tex a d f funkar inte
    #
    index = 0
    while chr(ord("a") + index) != word:
        index += 1
    return index

def my_min(sequence):

    min = sequence[0]

    for item in sequence:
        if item[1] < min[1]:
            min = item
    return min[1]

def extract_min(Q):
    min = my_min(Q)
    v  = None
    for index, m in enumerate(Q):
        if m[1] == min:
            print(f"I = {index}")
            print()
            v = Q.pop(index)
    return v , Q

def findeIndexInAlist(_list, des):
    for index, name in enumerate(_list):
            if name[0].name() == des:
                return index

def _findIndex(_list, des):

    for index, name in enumerate(_list):
        if name == des:
            return index

    return None



    

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
    d = []
    e = []

    Q = []

    node = adjlist.head()
    index = node._findIndex(start_node)

    Nameofnodes = node.list_nodes()

    #Init-Single-Source(adjlist, startnode)
    while not node.is_empty():
        d.append(inf)
        e.append(None)
        Q.append([node, inf])
        node = node.tail()    
    d[index] = Q[index][1] = 0

    while len(Q) > 0:
        print("Q = ")
        for q in Q:
            print(f"[{q[1]}, {q[0].name()}], ")
        print()
        print(f"d = {d}")
        print()

        # extract-min(Q)
        u , Q = extract_min(Q)
    
        print(f"u = {u[0].name()}")
        print()


        for v in u[0].edges().list(u[0].name()):
            (src, dst, weight) = v
            indexU = _findIndex(Nameofnodes, src)
            indexV = _findIndex(Nameofnodes, dst)
            # Relax
            if d[indexV] > d[indexU] + weight:
                d[indexV] = d[indexU] + weight
                e[indexV] = src
                #it change, then
                #Decrease-Key(Q,v,d[v])
                indexQ = findeIndexInAlist(Q, dst) 
                Q[indexQ][1] = d[indexV]

    d[index] = e[index] = None

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

    l: [ None, 1, 1]
    c: [ None, 'a', 'b' ]
    '''
    log.info("TODO: prim()")
    l = []
    c = []
    return l, c


if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
