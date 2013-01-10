from astropy import unit
import pylab

def makeIntegratedSpectrum():
    """
    Make an spectrum of an integrated cluster in the optical V-band.
    """
    
    # Pick the IMF and multiplicity properties
    multiProps = MultplicityDefault()
    imf = IMFSalpeter1955(multiplicity=multiProps)

    # Pick the Stellar Evolution Model (isochrone)
    evoModel = StellarEvolutionGeneva()

    # Pick out the specific isochrone
    isochrone = evoModel.isochrone(age=age, metallicity=metallicity)

    # Produce a simple stellar population
    ssp = SimpleStellarPopulation(imf=imf, isochrone=isochrone)

    # Pick the Stellar Atmosphere Models
    atmos = StellarAtmosphereModel()

    # Pick an extinction law
    redden = RedLawCardelli()

    # Redden the simple stellar population
    ssp.redden(redLaw=redden)

    # Generate the integrated spectrum of the SSP in luminosity
    distance = 1.0 * unit.Mpc
    spectrum = ssp.integratedSpectrum(atmospheres=atmos, distance=distance)
    
    # Trim to a specific wavelength range and plot it up.
    star = spectrum.trimSpectrum(star, 3000, 10000)

    pylab.clf()
    pylab.semilogy(star.wave, star.flux)
    pylab.xlabel('Wavelength (Angstroms)')
    pylab.ylabel('Flux (??)')
    
