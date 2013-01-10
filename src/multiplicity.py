defaultMFamp = 0.44
defaultMFindex = 0.51
defaultCSFamp = 0.50
defaultCSFindex = 0.45
defaultCSFmax = 3
defaultQindex = -0.4
defaultQmin = 0.01
default_aMean = 100.0 # log (AU)
default_aSigma = 0.1  # log (AU)

class Multiplicity(object):
    def __init__(self, MFamp=defaultMFamp, MFindex=defaultMFindex,
                 CSFamp=defaultCSFamp, CSFindex=defaultCSFindex,
                 CSFmax=defaultCSFmax,
                 Qindex=defaultQindex, Qmin=defaultMultiQmin,
                 aMean=default_aMean, aSigma=default_aSigma):
         
    #def binary_properties(self, mass, MFamp=defaultMFamp, MFindex=defaultMFindex,
    #              CSFamp=defaultCSFamp, CSFindex=defaultCSFindex, CSFmax=defaultCSFmax):
    def getMultiplicityFraction(self):
        """
        Given a star's mass, determine the probability that the star is in a
        multiple system (multiplicity fraction = MF) and its average number of
        companion stars (companion star fraction = CSF).
        """
        # Multiplicity Fraction
        mf = MFamp * mass**MFindex
        mf[mf > 1] = 1

    def getCompanionStarFraction(self):
        """
        Given a star's mass, determine the probability that the star is in a
        multiple system (multiplicity fraction = MF) and its average number of
        companion stars (companion star fraction = CSF).
        """
        # Companion Star Fraction
        csf = CSFamp * mass**CSFindex
        csf[csf > 3] = CSFmax

        return mf, csf

    def q_cdf_inv(self, x, qLo, beta):
        """
        Generative function for companion mass ratio (q = m_comp/m_primary).

        Inputs:
        x -- random number between 0 and 1.
        qLo -- lowest possible mass ratio
        beta -- p(q) \propto q^beta
        """
        b = 1.0 + beta
        return (x * (1.0 - qLo**b) + qLo**b)**(1.0/b)

