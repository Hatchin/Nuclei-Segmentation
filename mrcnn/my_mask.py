import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import sys
import os
import time

start_time = time.time()


# file_name = sys.argv[1]
# read_dictionary = np.load('output_mask/' + file_name + '.npy').item()

# mask_test = read_dictionary['masks'].astype(int).sum(axis=2)
# matplotlib.image.imsave('output_mask/' + file_name + '-mask.png', mask_test)

file_folder = sys.argv[1]

for root, dirs, files in os.walk(file_folder):
    if files:
        for f in files:
            if f.endswith('.npy'):
                f_address = os.path.join(root, f)
                pixels = np.load(f_address).item()
                mask = pixels['masks'].astype(int).sum(axis=2)
                destination = os.path.join(root, f[:-4])
                matplotlib.image.imsave(destination+'-mask.png', mask)


end_time = time.time()
ellapsed_time = (end_time-start_time)/3600

print('Time required to train ', ellapsed_time, 'hours')

print('Time required to train ', (end_time-start_time)/60, 'min')