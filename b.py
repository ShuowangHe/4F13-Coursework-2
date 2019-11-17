import scipy as sp
import numpy as np
import scipy.io as sio
import scipy.linalg
import csv
from tqdm import tqdm
from eprank import eprank
import matplotlib.pyplot as plt

data = sio.loadmat('tennis_data.mat')

W=data['W']
G=data['G']

result = np.array(eprank(G,107,1100))
Ms = result[0,:]
Ps = result[1,:]
print(Ms)
plt.plot(Ms)
plt.show()
