import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    data_mean =  np.mean(data)
    
    r_squared =  1 - ( (np.square(data - predictions).sum())/(np.square(data - data_mean).sum()))

    return r_squared
