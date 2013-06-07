from mcmc.DensitsyFunction import DensityFunction

class MCMCTarget(DensityFunction):
    def __init__(self, dimension):
        DensityFunction.__init__(self, dimension)
        
    def get_gradient(self, x):
        """
        parameters:
        x - 1d array with point to evaluate gradient at
        
        returns:
        1d array which contains gradients at x
        """
        raise NotImplementedError()
    
    def get_hessian(self, x):
        """
        parameters:
        x - 1d array, point to evaluate the hessian at
        
        returns:
        2d array which contains hessian at x
        """
        raise NotImplementedError()
    
    def get_tensor(self, x, i):
        """
        parameters:
        x - 1d array, point to evaluate the tensors at
        i - index of the tensor to evaluate
        
        returns:
        2d array which contains tensor at index i
        """
        raise NotImplementedError()
    
    def get_all_tensors(self, x):
        return [self.get_tensor(self, x, i) for i in range(self.dimension)]