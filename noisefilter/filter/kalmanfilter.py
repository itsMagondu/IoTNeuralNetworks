# Kalman filter in Python adopted from http://scipy-cookbook.readthedocs.io/items/KalmanFiltering.html
import numpy as np
import matplotlib.pyplot as plt
import time

class KalmanFilter:
	def __init__(self,base_value=24,iterations=200,initial_guess=20.0,posteri_estimate=4.0,plot=True):
		# intial parameters
		self.n_iter = iterations  # How many iterations to create test data
		sz = (self.n_iter,) # size of array
		self.x = base_value # This is the base value that shall be used to create noisy data. It is the true value
		self.z = np.random.normal(self.x,1,size=sz) # observations (normal about x, sigma=0.1)

		self.Q = 1e-5 # process variance

		# allocate space for arrays
		self.xhat=np.zeros(sz)      # a posteri estimate of x
		self.P=np.zeros(sz)         # a posteri error estimate
		self.xhatminus=np.zeros(sz) # a priori estimate of x
		self.Pminus=np.zeros(sz)   

		# a priori error estimate
		self.K=np.zeros(sz)         # gain or blending factor

		self.R = 2

		# intial guesses
		self.xhat[0] = initial_guess #Initial estimate
		self.P[0] = posteri_estimate#Estimate of the error made

		self.plot = plot
		
	def filter(self):
		print  "starting the filter"
		start = time.time()
		for k in range(1,self.n_iter):
		    # time update
		    self.xhatminus[k] = self.xhat[k-1]
		    self.Pminus[k] = self.P[k-1]+self.Q

		    # measurement update
		    self.K[k] = self.Pminus[k]/( self.Pminus[k]+self.R )
		    self.xhat[k] = self.xhatminus[k]+self.K[k]*(self.z[k]-self.xhatminus[k])
		    self.P[k] = (1-self.K[k])*self.Pminus[k]
		end = time.time()

		print("Took %s seconds" % (time.time() - start))

		print "Noisy data: "
		print self.z 

		print "Estimates:"
		print self.xhat

		print "Truth Value:"
		print self.x

		#print "Error estimate"
		#print self.P

		if self.plot:
			self.plot_results()

		return self.z, self.xhat, self.x

	def plot_results(self):
		plt.rcParams['figure.figsize'] = (10, 8)
		plt.figure()
		plt.plot(self.z,'k+',label='noisy measurements')
		plt.plot(self.xhat,'b-',label='a posteri estimate')
		plt.axhline(self.x,color='g',label='truth value')
		plt.legend()
		plt.title('Estimate vs. iteration step', fontweight='bold')
		plt.xlabel('Iteration')
		plt.ylabel('Temperature')

		#plt.figure()
		#valid_iter = range(1,self.n_iter) # Pminus not valid at step 0
		#plt.plot(valid_iter,self.Pminus[valid_iter],label='a priori error estimate')
		#plt.title('Estimated $\it{\mathbf{a \ priori}}$ error vs. iteration step', fontweight='bold')
		#plt.xlabel('Iteration')
		#plt.ylabel('$(Temparature)^2$')
		#plt.setp(plt.gca(),'ylim',[0,.01])
		plt.show()
