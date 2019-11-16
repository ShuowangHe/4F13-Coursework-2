import scipy as sp
import numpy as np
import scipy.io as sio

data = sio.loadmat('tennis_data.mat')

W=data['W']
G=data['G']
print(type(W))
