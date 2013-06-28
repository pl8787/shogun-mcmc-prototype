from abc import abstractmethod

class Sampler(object):
    def __init__(self, target, start):
        self.target=target
        self.current=start
        
    @abstractmethod
    def step(self):
        raise NotImplementedError()