import math
import numpy as np
from scipy.stats import bernoulli

simlen = 100000

prob1 = 13/49
data_bern1 = bernoulli.rvs(size=simlen,p=prob1)
err_ind1 = np.nonzero(data_bern1 == 1)
print("Probability of picking a heart:")
print("actual:",prob1)
print("simulation:",np.size(err_ind1)/100000)
print("Simulated values: ", data_bern1)

prob2 = 3/49
data_bern2 = bernoulli.rvs(size=simlen ,p=prob2)
err_ind2 = np.nonzero(data_bern2 == 1)
print("Probability of picking a king:")
print("actual:",prob2)
print("simulation:",np.size(err_ind2)/100000)
print("Simulated values: ", data_bern2)


