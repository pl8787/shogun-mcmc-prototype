from abc import abstractmethod
from mcmc.sampler.MHStepOutput import MHStepOutput
from mcmc.sampler.Sampler import Sampler
from numpy.ma.core import log
from numpy.random import rand

class MetropolisHastings(Sampler):
    def __init__(self, target, start):
        """
        start - sample object
        target - target distribution to sample from
        """
        Sampler.__init__(self, target, start)
        
        self.current_log_lik = self.target.log_pdf(self.current.sample)
        self.current_proposal = self.construct_proposal(self.current.sample)
    
    @abstractmethod
    def construct_proposal(self, point):
        """
        point - 1d point where to construct proposal
        Returns an instance of ProposalDistribution at the given point
        """
        raise NotImplementedError()
        
    def step(self):
        proposal_object = self.current_proposal.propose()
        proposal_sample = proposal_object.sample
        proposal_new = self.construct_proposal(proposal_sample)
        
        if not self.current_proposal.is_symmetric:
            log_current_given_proposal = proposal_new.log_pdf(self.current.sample)
            log_proposal_given_current = self.current_proposal.log_pdf(proposal_sample)
        else:
            log_proposal_given_current = 0
            log_current_given_proposal = 0
            
        log_lik_proposal = self.target.log_pdf(proposal_sample)
        
        log_ratio = log_lik_proposal - self.log_lik_current \
                    + log_current_given_proposal - log_proposal_given_current
        
        log_ratio = min(log(1), log_ratio)
        accepted = log_ratio > log(rand(1))
        
        if accepted:
            sample_object = proposal_object
            self.log_lik_current = log_lik_proposal
            self.current_proposal = proposal_new
        else:
            sample_object = self.current
            
        # adapt state: position and proposal_2d
        self.current = sample_object
        return MHStepOutput(sample_object, proposal_object, self.log_lik_current, log_ratio, accepted)

