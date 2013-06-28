from distribution.Gaussian import Gaussian
from distribution.SampleObject import SampleObject
from mcmc.chain.Chain import Chain
from mcmc.chain.ChainParams import ChainParams
from mcmc.sampler.MetropolisHastings import MetropolisHastings
from numpy.lib.twodim_base import eye
from numpy.ma.core import zeros

if __name__ == '__main__':
    start=SampleObject(zeros(2))
    target=Gaussian(mu=zeros(2), Sigma=eye(2))
    sampler=MetropolisHastings(target, start)
    params=ChainParams(1000)
    chain=Chain(params, sampler)
    chain.run()