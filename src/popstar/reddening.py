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
		
		 #Convert wavelength in Angtroms to inverse microns
		inv_wave_mu = (1/(wavelength*1e-4))

                #Define x and y according to Cardelli Eqns 3a and 3b of Cardelli 1989
		x = inv_wave_mu
		y = x - 1.82

		if ( (min.x < 0.3) || (max.x > 3.3)):
			raise Exception("{0}: Wavelength value outside of defined wavelength range of Cardelli 1989 Law.".format(self.__class__.__name__))

		a = np.zeros(wavelength.shape)
		b = np.zeros(wavelength.shae)

                #Define a(x) and b(x) according to Cardelli
                #Blue range x in [3.3,1.1]
		blue_ind = (x <= 3.3)
		bluer_ind = (x[blue_ind] >= 1.1)
		i = blue_ind[bluer_ind]
		a[i] =  1 + 0.17699*y[i] - 0.50447*(np.power(y[i],2)) - 0.02427*(np.power(y[i],3)) +0.72085*(np.power(y[i],4)) + 0.01979*(np.power(y[i],5)) - 0.77530*(np.power(y[i],6)) + 0.32999*(np.power(y[i],7))

		b[i] = 1.41338*y[i] + 2.28305*(np.power(y[i],2)) +1.07233*(np.power(y[i],3)) - 5.38434*(np.power(y[i],4)) - 0.62251*(np.power(y[i],5)) + 5.30260*(np.power(y[i],6)) - 2.09002*(np.power(y[i],7));
    
                #Red range x in [0.3,1.1)
		red_ind = (x >= 0.3)
		redder_ind = (x[red_ind] < 1.1)
		j = red_ind[redder_ind]
		a[j] = 0.574*pow(j,1.61);
		b[j] = -0.527*pow(j,1.61);

		#Find extinction function of wavelength
		ext_wave = (a +b/Rv)*av
		return ext_wave
		
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
