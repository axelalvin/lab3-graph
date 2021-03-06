#!/usr/bin/env python3

# adding this line to test git func

import sys
import logging

log = logging.getLogger(__name__)

from math import inf


def floyd(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Warshall's
    algorithm.

    Pre: adjlist is not empty.
    '''
    n = adjlist.node_cardinality()
    distanceMatix = adjlist.adjacency_matrix()

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


def warshall(adjlist):
    '''
    Returns an NxN matrix that contains the result of running Floyd's algorithm.

    Pre: adjlist is not empty.
    '''
    # beacuse floyd and warshall using the same algorithm we can use floyd and just change the results

    n = adjlist.node_cardinality()

    floydMatix = floyd(adjlist)

    for i in range(n):
        for j in range(n):
            floydMatix[i][j] = False if floydMatix[i][j] == inf else True


    return floydMatix


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
            v = Q.pop(index)
    return v , Q

def _findIndex(_list, des):

    for index, name in enumerate(_list):
        if name == des:
            return index

    return None

def findMin(_list1, _list2):

    _min = inf
    smallest = inf
    for i in range(len(_list1)):
        if (_list1[i] < smallest) and (_list2[i] is False):
            _min = i
            smallest = _list1[i]

    
    return _min



    

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

    #Init-Single-Source(adjlist, startnode)
    while not node.is_empty():
        d.append(inf)
        e.append(None)
        Q.append([node, inf]) 
        node = node.tail()    
    d[index] = Q[index][1] = 0

    while len(Q) > 0:
  
        # extract-min(Q)
        u , Q = extract_min(Q)
    
        for v in u[0].edges().list(u[0].name()):
            (src, dst, weight) = v
            indexU = _findIndex(adjlist.head().list_nodes(), src)
            indexV = _findIndex(adjlist.head().list_nodes(), dst)
            # Relax
            if d[indexV] > d[indexU] + weight:
                d[indexV] = d[indexU] + weight
                e[indexV] = src
                
                #Decrease-Key(Q,v,d[v])
                                    # creating a list that only contains the name of the nodes in Q
                indexQ = _findIndex([Q[x][0].name() for x in range(len(Q))], dst) 
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

    disMatrix = adjlist.adjacency_matrix()
    node = adjlist.head()
    index = node._findIndex(start_node)
    v = adjlist.node_cardinality()

    l = []  #nodeWeight
    c = []  #parent node
    setMst = [] #TRUE -> node is included in MST
    

    #set sizes to all lists to number of nodes
    #and append values
    while not node.is_empty():
        l.append(inf)
        c.append(inf)
        setMst.append(False)
        node = node.tail()
    l[index] = 0
    c[index] = None

    node = adjlist.head()

    for i in range(v-1):
        #set u to min element in l
        u = findMin(l, setMst)
        setMst[u] = True

        #iterate through every column for node u
        for j in range(v):
            if (disMatrix[u][j] != 0) and (setMst[j] is False) and (disMatrix[u][j] < l[j]):
                l[j] = disMatrix[u][j]
                c[j] = node._findName(u)
    

    l[index] = c[index] = None
    return l, c


if __name__ == "__main__":
    logging.critical("module contains no main")
    sys.exit(1)
