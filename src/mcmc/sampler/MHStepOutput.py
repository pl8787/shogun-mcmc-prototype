from mcmc.sampler.StepOutput import StepOutput

class MHStepOutput(StepOutput):
    def __init__(self, sample_object, proposal_object, log_lik_current, acceptance_prob, is_accepted):
        StepOutput.__init__(self, sample_object)
        self.proposal_object = proposal_object
        self.acceptance_prob = acceptance_prob
        self.is_accepted = is_accepted
