import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

# Generate random height data
sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = lognormal_path

key_type = int

if file_name is lognormal_path or test_lognormal_path:
    key_type = np.int_
elif file_name is longlat_path:
    key_type = np.float

with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# for i in range(10):
#     print(arr[i])

# arr = np.divide(arr, np.sum(arr))

# Create CDF
counts, bin_edges = np.histogram(arr, bins=10000000, density=True)
cdf = np.cumsum(counts)
# cumulative_prob = cdf / float(len(arr))

# Plot CDF
plt.plot(bin_edges[1:], cdf)
plt.xlabel('Key')
plt.ylabel('CDF')
plt.savefig("CDFplot.png")
# plt.show()


# https://stats.stackexchange.com/questions/381588/how-does-this-code-find-the-cdf
