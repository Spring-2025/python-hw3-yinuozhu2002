import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def VaR(r, confidence, principal=1):
    alpha = 1 - confidence
    var_value = np.percentile(r, alpha * 100)

    plt.hist(r, bins=50, alpha=0.75)
    plt.axvline(var_value, color='red', linestyle='dashed', linewidth=2)
    plt.title(f'Value at Risk (VaR) at {confidence * 100:.2f}% Confidence Level')
    plt.xlabel('Returns')
    plt.ylabel('Frequency')
    plt.show()

    return -var_value * principal
