## Note: we need to do the imports necessary
## for the module within the module's files

import numpy as np
import numpy.random as random

def sim2coins(ntests):
    ntests=int(ntests)
# simulate ntests tosses of 2 coins 
    coin1=np.random.rand(ntests) > 0.5
    coin2=np.random.rand(ntests) > 0.5
    tails_and_heads = np.logical_and(coin1==False, coin2==True)
    return tails_and_heads.sum()/int(ntests)

