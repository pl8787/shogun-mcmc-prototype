from abc import abstractmethod
from mcmc.DensitsyFunction import DensityFunction

class ProposalDistribution(DensityFunction):
    def __init__(self, dimension):
        DensityFunction.__init__(self, dimension)
        
    @abstractmethod
    def propose(self):
        """
        returns an instance of ProposalSample
        """
        raise NotImplementedError()