from numpy.ma.core import zeros
from numpy import int64

class Chain(object):
    def __init__(self, params, sampler):
        self.params=params
        self.sampler=sampler
        
        self.iteration=int64(0)
        self.samples=zeros((params.chain_length, sampler.target.dimension))
        
        # fields for the chain
        num_iterations = self.params.chain_length
        self.samples = zeros((num_iterations, self.sampler.target.dimension))
        self.log_ratios = zeros(num_iterations)
        self.log_liks = zeros(num_iterations)
        self.accepteds = zeros(num_iterations)
    
    def run(self):
        # run chain
        while self.iteration < self.params.chain_length:
            i = self.iteration
            # mcmc step
            step_output = self.sampler.step()
            
            # collect results
            self.samples[i, :] = step_output.sample_object.sample
            self.log_ratios[i] = step_output.log_ratio
            self.accepteds[i] = step_output.accepted
            self.log_liks[i] = step_output.log_lik
            
            # update chain state
            self.iteration += 1
