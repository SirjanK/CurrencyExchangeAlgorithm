import numpy as np

class NetworkGraph():
    matrix = None
    V = None

    def __init__(self, V, default_values = 0):
        self.matrix = default_values*np.ones((V,V))
        self.V = V

    # Sets the weight of an edge
    #   @edge is a tuple (u,v)
    #   @weight is the desired weight to set
    def set_weight(self, edge, weight):
        assert type(edge) is tuple and len(edge) == 2, 'Invalid edge: {}. Edge must be a tuple of form (u,v)'.format(edge)
        u,v = edge
        assert u < self.V and v < self.V, 'Invalid edge: {} for graph with {} vertices'.format(edge, self.V)
        self.matrix[u,v] = weight

    # Returns all edges of the form (v, .)
    def get_out_edges(self, v):
        assert v < self.V, 'Invalid vertex: {} for graph with {} vertices'.format(v, self.V)
        return self.matrix[v,:]

    # Returns all edges of the form (.,v)
    def get_in_edges(self, v):
        assert v < self.V, 'Invalid vertex: {} for graph with {} vertices'.format(v, self.V)
        return self.matrix[:,v]

    def get_edges(self):
        return np.argwhere(self.matrix > 0)
