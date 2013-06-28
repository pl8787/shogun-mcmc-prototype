from distribution.DensitsyFunction import DensityFunction
from numpy.lib.twodim_base import eye
from numpy.linalg.linalg import cholesky
from numpy.ma.core import asarray, shape, log, diag, zeros, reshape
from numpy.random import randn
from scipy.constants.constants import pi
from scipy.linalg.basic import solve_triangular

class Gaussian(DensityFunction):
    def __init__(self, mu=asarray([0, 0]), Sigma=eye(2), is_cholesky=False):
        DensityFunction.__init__(self, len(Sigma))
        
        assert(len(shape(mu)) == 1)
        assert(max(shape(Sigma)) == len(mu))
        self.mu = mu
        if is_cholesky: 
            self.L = Sigma
        else: 
            assert(shape(Sigma)[0] == shape(Sigma)[1])
            self.L = cholesky(Sigma)
    
    def sample(self, n=1):
        V = randn(self.dimension, n)

        # map to our desired Gaussian and transpose to have row-wise vectors
        return self.L.dot(V).T + self.mu
    
    def log_pdf(self, x):
        return self.log_pdf_multiple_points(reshape(x, (1, len(x))))

    def log_pdf_multiple_points(self, X):
        assert(len(shape(X)) == 2)
        assert(shape(X)[1] == self.dimension)
        
        log_determinant_part = -sum(log(diag(self.L)))
        
        quadratic_parts = zeros(len(X))
        for i in range(len(X)):
            x = X[i] - self.mu
            
            # solve y=K^(-1)x = L^(-T)L^(-1)x
            y = solve_triangular(self.L, x.T, lower=True)
            y = solve_triangular(self.L.T, y, lower=False)
            quadratic_parts[i] = -0.5 * x.dot(y)
            
        const_part = -0.5 * len(self.L) * log(2 * pi)
        
        return const_part + log_determinant_part + quadratic_parts
