import scipy as sp
import numpy as np
import scipy.io as sio
import scipy.linalg
import csv
from tqdm import tqdm
from gibbs_sample import gibbs_sample

data = sio.loadmat('tennis_data.mat')

W=data['W']
G=data['G']

result = gibbs_sample(G,107,1100)

with open('result.csv','a') as newFile:
    newFileWriter = csv.writer(newFile)
    for line in range(len(W)):
        newFileWriter.writerow(result[line,:])
