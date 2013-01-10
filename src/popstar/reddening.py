#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Description of file here!
'''

class RedLawCardelli(object):
	
	def __init__(self, v=0.1, rv=3.1):
		'''
		
		\f$R_v = \frac{A_v}{E(B-V)} \f$
		
		@param v Extinction in the v band.
		@param rv Relative extinction in the v band. 
		'''
		self.v = v
		self.rv = rv
	
	def extinctionForWavelength(self, wavelength=None):
		'''
		Returns the extinction value for the given wavelength.
		
		@param wavelength The wavelength in Ångstroms.
		'''
		
	def extinctify(self, wavelengths=None, values=None):
		'''
		Given wavelength grid and (flux or luminosity) values, returns the extincted values.
		
		The extinction applied is \f$F_{extincted} = 10^{-0.4A_\lambda}F_{unextincted}\f$
		
		where \f$A_{\lambda}\f$ is the extinction at wavelength \f$\lambda\f$.
		
		@param wavelengths Array of wavelength values in Ångstroms.
		@param flux Flux values.
		@returns The extincted value array.
		'''
		if None in [wavelengths, values]:
			raise Exception("{0}: Either the wavelength or value array was not defined.".format(self.__class__.__name__))
		
		extinction_array = np.zeros(shape=wavelengths.shape)
		for idx, w in enumerate(wavelengths):
			extinction_array[idx] = self.extinctionForWavelength(wavelength=w)
		
		return np.power(10,-0.4*extinction_array) * np.array(values)
		
		
	def ...(self, ...):
		'''
		Returns an array of extinction values binned by wavelength.
		
		'''

r = RedLawCardelli()
r.extinction(min_wavelength=, max_wavelength=)