from abc import abstractmethod
from numpy.ma.core import asarray

class DensityFunction(object):
    def __init__(self, dimension):
        self.dimension=dimension
        
    @abstractmethod
    def log_pdf(self, x):
        """
        x is a 1d point
        """
        raise NotImplementedError()
    
    def log_pdf_multiple_points(self, X):
        """
        x is a 2d array
        """
        return asarray([self.log_pdf(x) for x in X])
        
    def sample(self, n=1):
        raise NotImplementedError()