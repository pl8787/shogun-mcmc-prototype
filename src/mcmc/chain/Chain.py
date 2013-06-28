from numpy.ma.core import zeros
from numpy import int64

class Chain(object):
    def __init__(self, params, sampler):
        self.params=params
        self.sampler=sampler
        
        self.iteration=int64(0)
        self.samples=zeros((params.num_iterations, sampler.target.dimension))
    
    
    def run(self, num_iterations):
        raise NotImplementedError()
    