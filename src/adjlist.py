#!/usr/bin/env python3

#
# Recommended order to get started:
# 1) AdjacencyList.{add_node,node_cardinality}
# 2) AdjacencyList._add_edge, Edge.add - note: if you run in debug mode, you
# will get all edges printed when selecting 'v: view' in the menu.
# 3) AdjacencyList.find_edge, Edge.find
#

import sys
import logging

log = logging.getLogger(__name__)

from math import inf

class AdjacencyList:
    '''
    A linked-list implementation of an adjacency list that keeps its nodes and
    edges lexicographically ordered at all times.
    '''
    def __init__(self, name=None, info=None):
        '''
        Initializes a new adjacency list.  It is considered empty if no head
        node is provided.  Optionally, a node can also have associated info.
        '''
        self._name = name # head node name
        self._info = info # head node info
        if not self.head().is_empty():
            self._tail = AdjacencyList() # empty tail
            self._edges = Edge() # empty list of edges

    def is_empty(self):
        '''
        Returns true if this adjacency list is empty.
        '''
        return self._name is None

    def head(self):
        '''
        Returns the head of this adjacency list.
        '''
        return self

    def tail(self):
        '''
        Returns the tail of this adjacency list.
        '''
        return self._tail

    def cons(self, tail):
        '''
        Returns the head of this adjacency list with a newly attached tail.
        '''
        self._tail = tail
        return self.head()

    def name(self):
        '''
        Returns the node name.
        '''
        return self._name

    def info(self):
        '''
        Returns auxilirary node info.
        '''
        return self._info

    def edges(self):
        '''
        Returns the edge head.
        '''
        return self._edges

    def set_name(self, name):
        '''
        Sets the node name to `name`.

        Returns an adjacency list head.
        '''
        self._name = name
        return self.head()

    def set_info(self, info):
        '''
        Sets the auxilirary info of this node to `info`.

        Returns an adjacency list head.
        '''
        self._info = info
        return self.head()

    def set_edges(self, edges):
        '''
        Sets the edge head of this node to `edges`.

        Returns an adjacency list head.
        '''
        self._edges = edges
        return self.head()

    ###
    # Node operations
    ###
    def add_node(self, name, info=None):
        '''
        Adds a new node named `name` in lexicographical order.  If node `name`
        is a member, its info-field is updated based on `info`.

        Returns an adjacency list head.
        '''
        log.info("TODO: add_node()")
        return self.head()

    def delete_node(self, name):
        '''
        Deletes the node named `name` if it is a member.

        Returns an adjacency list head.
        '''
        log.info("TODO: delete_node()")
        return self.head()

    def find_node(self, name):
        '''
        Returns True if the node named `name` is a member.
        '''
        if self.is_empty():
            return False
        if name == self.head().name():
            return True
        return self.tail().find_node(name)

    def node_cardinality(self):
        '''
        Returns the number of nodes.
        '''
        log.info("TODO: node_cardinality()")
        return 0

    ###
    # Edge operations
    ###
    def add_edge(self, src, dst, weight=1):
        '''
        Adds or updates an edge from node `src` to node `dst` with a given
        weight `weight`.  If either of the two nodes are non-members, the same
        adjacency list is returned without any modification.

        Returns an adjacency list head.
        '''
        if not self.find_node(dst):
            return self.head()
        return self._add_edge(src, dst, weight)

    def _add_edge(self, src, dst, weight):
        '''
        Adds a new (or updates an existing) edge from node `src` to node `dst`,
        setting the weight to `weight`.

        Returns an adjacency list head.

        Pre: `dst` is a member of this adjacency list.
        '''
        log.info("TODO: _add_edge()")
        return self.head()

    def delete_edge(self, src, dst):
        '''
        Deletes an edge from node `src` to node `dst` if it exists.

        Returns an adjacency list head.
        '''
        log.info("TODO: delete_edge()")
        return self.head()

    def delete_edges(self, name):
        '''
        Deletes all edges towards the node named `name`.

        Returns an adjacency list head.
        '''
        log.info("TODO: delete_edges()")
        return self.head()

    def find_edge(self, src, dst):
        '''
        Returns True if there's an edge from node `src` to node `dst`.
        '''
        log.info("TODO: find_edge()")
        return False

    def edge_cardinality(self):
        '''
        Returns the number of edges.
        '''
        log.info("TODO: edge_cardinality()")
        return 0

    def self_loops(self):
        '''
        Returns the number of loops in this adjacency list.  Note that a loop is
        defined as a node that has an edge towards itself, e.g., A->A.
        '''
        log.info("TODO: self_loops()")
        return 0

    def adjacency_matrix(self):
        '''
        Returns this adjacency list as an adjacency matrix.  For example,
        consider the following adjacency list where all edges have weight=1.
        
        a: a->b->c
        |
        v
        b: a->b
        |
        v
        c: c

        Then we would expect the following 3x3 adjacency matrix:

          a b c
        -+-----
        a|1 1 1
        b|1 1 *
        c|* * 1

        Where the corresponding python-matrix is:

        [ [1,1,1], [1,1,inf], [inf,inf,1] ]

        Note that inf indicates that there is no path between two nodes.  Also,
        all rows and columns are lexicographically ordered based on node names.

        Hint: depending on your solution, you may need to add a helper method
        that maps a node's name to it's numeric position in the adjacency list.
        '''
        if self.is_empty():
            return [[]]

        # In case you'd like to create an inf-initialized n x n matrix
        n = self.node_cardinality()
        matrix = [ [inf]*n for i in range(n) ]
        log.info("TODO: adjacency_matrix()")
        return matrix

    def list_nodes(self):
        '''
        Returns a list of node names in lexicographical order.
        '''
        head, node_names = self.head(), []
        while not head.is_empty():
            node_names += [ head.name() ]
            head = head.tail()
        return node_names

    def list_edges(self):
        '''
        Returns a list of edges in lexicographical order.
        '''
        if self.head().is_empty():
            return []
        return self.head().edges().list(self.head().name()) +\
            self.tail().list_edges()

class Edge:
    '''
    A linked-list implementation of edges that originate from an implicit source
    node.  Each edge has a weight and goes towards a given destination node.
    '''
    def __init__(self, dst=None, weight=1):
        '''
        Initializes a new edge sequence.  It is considered empty if no head edge
        is provided, i.e., dst is set to None.
        '''
        self._dst = dst # where is this edge's destination
        self._weight = weight # what is the weight of this edge
        if not self.head().is_empty():
            self._tail= Edge() # empty edge tail

    def is_empty(self):
        '''
        Returns true if this edge is empty.
        '''
        return self._dst is None
    
    def head(self):
        '''
        Returns the head of this edge.
        '''
        return self

    def tail(self):
        '''
        Returns the tail of this edge.
        '''
        return self._tail

    def cons(self, tail):
        '''
        Returns the head of this sequence with a newly attached tail.
        '''
        self._tail = tail
        return self.head()

    def dst(self):
        '''
        Returns the node name that this edge goes towards.
        '''
        return self._dst

    def weight(self):
        '''
        Returns the weight of this edge.
        '''
        return self._weight

    def set_dst(self, dst):
        '''
        Sets the destination of this edge to `dst`.

        Returns an edge head.
        '''
        self._dst = dst
        return self.head()

    def set_weight(self, weight):
        '''
        Sets the weight of this edge to `weight`.

        Returns an edge head.
        '''
        self._weight = weight
        return self.head()
    
    ###
    # Operations
    ###
    def add(self, dst, weight=1):
        '''
        Adds a new edge towards `dst` in lexicographical order.  If such an
        edge exists already, the associated weight-field is updated instead.

        Returns an edge head.
        '''
        log.info("TODO: add()")
        return self.head()

    def delete(self, dst):
        '''
        Deletes the edge that goes towards `dst` if it exists.

        Returns an edge head.
        '''
        log.info("TODO: delete()")
        return self.head()

    def find(self, dst):
        '''
        Returns True if there is an edge towards `dst` in this sequence.
        '''
        log.info("TODO: edge find()")
        return False

    def cardinality(self):
        '''
        Returns the number of edges in this sequence.
        '''
        log.info("TODO: edge cardinality()")
        return 0

    def list(self, src):
        '''
        Returns a list of edges in lexicographical order, e.g., if `src`
        goes to nodes A and B, the returned list would be:
            [ (src, A), (src, B) ]
        '''
        if self.head().is_empty():
            return []
        return [(src, self.head().dst(), self.weight())] + self.tail().list(src)

if __name__ == "__main__":
    log.critical("module contains no main method")
    sys.exit(1)
