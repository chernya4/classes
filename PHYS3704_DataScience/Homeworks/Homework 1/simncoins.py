import numpy as np
import matplotlib.pyplot as plt
from numpy import random

def simncoins(nsims, ncoins):
    # 1 - Heads
    # 2 - Tails

    # Floor:
    coins_f = np.floor(random.rand(nsims,ncoins) * 2) + 1
    count_of_ones = np.sum(coins_f == 1, axis=1)
    
    return count_of_ones