from mcmc.sampler.StepOutput import StepOutput

class MHStepOutput(StepOutput):
    def __init__(self, sample_object, proposal_object, log_lik_current, log_ratio, is_accepted):
        StepOutput.__init__(self, sample_object)
        self.proposal_object = proposal_object
        self.log_ratio = log_ratio
        self.is_accepted = is_accepted
