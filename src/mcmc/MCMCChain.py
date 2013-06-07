from numpy.ma.core import zeros
from numpy import int64

class MCMCChain(object):
    def __init__(self, mcmc_params, mcmc_sampler):
        self.mcmc_params=mcmc_params
        self.mcmc_sampler=mcmc_sampler
        
        self.iteration=int64(0)
        self.samples=zeros((mcmc_params.num_iterations, mcmc_sampler.target.dimension))
    
    
    def run(self, num_iterations):
        raise NotImplementedError()
    