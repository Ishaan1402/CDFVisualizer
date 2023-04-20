import numpy as np
import matplotlib.pyplot as plt

# Generate random height data
sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = lognormal_path

key_type = int

if file_name == lognormal_path or file_name == test_lognormal_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path:
    key_type = np.float

with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# Compute the histogram
counts_arr = np.bincount(arr)

# Calculate the probability density function (PDF)
pdf = counts_arr / len(arr)

# Calculate the cumulative distribution function (CDF)
cdf = np.cumsum(pdf)

# Create a plot of the CDF
plt.plot(np.arange(len(cdf)), cdf)
plt.xlabel('Value')
plt.ylabel('CDF')
plt.show()
