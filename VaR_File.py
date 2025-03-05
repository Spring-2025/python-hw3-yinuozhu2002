import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r, confidence, principal=1):
    alpha = 1 - confidence
    var_value = np.percentile(r, alpha * 100)
    return abs(var_value) * principal 
