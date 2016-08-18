from __future__ import division
import numpy as np
from collections import deque
from NeuralNet import NeuralNetwork

def _scale_to_binary(e, minV, maxV):
    result = ((e-minV)/(maxV-minV))*(1-0)+0
    return result

def rescale_from_binary(e, minV, maxV):
    result = e*(maxV-minV) + minV
    return result


def create_series(in_array,window_size,period, minV, maxV, layer_nodes = [2,3], sigmoid = 'tanh', epochs = 50000):
    global_max = maxV
    global_min = minV
    
    #What is the window size? I guess it is the number of records used to train
            
    X_train = []
    y_train = []
    for i in range(len(in_array)-window_size):#Get the first item in the list till windowsize
        X = []
        for j in range(window_size):
            X.append(_scale_to_binary(in_array[i+j],global_min,global_max)) #Scale the values to something btwn 0 and 1
        X_train.append(X) #Add the list to the training lst
        y_train.append(_scale_to_binary(in_array[i+window_size],global_min,global_max))#The back propagation layer
        
    X_train = np.array(X_train)
    y_train = np.array(y_train) 

        
    layers = []
    layers.append(window_size)
    for i in range(len(layer_nodes)):
        layers.append(layer_nodes[i])
    
                     
        
    n = NeuralNetwork(layers,sigmoid)
       
    n.fit(X_train,y_train, epochs)
        
       
        
    X_test = in_array[-window_size:]

    for i in range(len(X_test)):
        X_test[i]=_scale_to_binary(X_test[i],global_min,global_max)

    preds = []   
    X_test = deque(X_test)
          
    for i in range(period):
        val = n.predict(X_test)
        preds.append(rescale_from_binary(val[0], global_min, global_max))
            
        X_test.rotate(-1)
        X_test[window_size-1] = val[0]
        
              
    return preds