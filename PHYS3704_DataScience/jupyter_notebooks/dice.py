import numpy.random as random
import numpy as np
import matplotlib.pyplot as plt

def rolldice(nsims):
# nsims is number of simulations to do
    nsims=int(nsims)
    prob=1/6. #this is a shortcut to say 1 out of 6
    is_one=(random.rand(nsims,100) < prob)
# generate nsims sets of 100 rolls
    ndice_array=np.array([2,5,10,25,100])

    for i,ndice in enumerate(ndice_array):
        plt.figure(i) # create a new figure for each plot
        plt.hist( np.sum(is_one[:,0:ndice],axis=1), 
        range=(-0.5,ndice+0.5),bins=(ndice + 1))
        plt.title(str(ndice) + ' dice')
        # convert ndice to a string with str(), then use that to title the plot
        plt.xlabel('Total number of ones')

        print(f'ndice: {ndice}')
        print(f'np.mean: {np.mean(np.sum(is_one[:,0:ndice],axis=1))}')
        print(f'np.sum: {np.sum(np.sum(is_one[:,0:ndice],axis=1))/nsims:.4f}')
        print(f'Expected mean: {ndice*prob:.4f} ')

        print(f'np.std**2:{np.std( np.sum(is_one[:, 0:ndice],axis=1) )**2:.4f}')
        print(f'np.var: {np.var( np.sum(is_one[:, 0:ndice],axis=1) ) :.4f}')
        print(f'Expected variance: {ndice*prob*(1-prob):.4f}')
        print('')
    
