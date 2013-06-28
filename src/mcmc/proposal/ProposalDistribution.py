from abc import abstractmethod
from distribution.DensitsyFunction import DensityFunction

class ProposalDistribution(DensityFunction):
    def __init__(self, dimension, is_symmetric):
        DensityFunction.__init__(self, dimension)
        self.is_symmetric=is_symmetric
        
    @abstractmethod
    def propose(self):
        """
        returns an instance of SampleObject
        """
        raise NotImplementedError()