import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
test_longitudes_path = "datasets/longitudes-200M.bin.data"
test_ycsb_path = "datasets/ycsb-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"
longitudes_path = "/users/ipatel9/dataset/longitudes-200M.bin.data"
ycsb_path = "/users/ipatel9/dataset/ycsb-200M.bin.data"

file_name = test_longlat_path
key_type = np.int

if file_name == lognormal_path or file_name == test_lognormal_path or file_name == ycsb_path or file_name == test_ycsb_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path or file_name == test_longitudes_path or file_name == longitudes_path:
    key_type = np.float

with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# Create CDF
counts, bin_edges = np.histogram(arr, bins=62500, density=True)
cdf = np.cumsum(counts)

# Plot CDF
plt.plot(bin_edges[1:], cdf)
# plt.xlim([0, 1])
plt.title("Longlat Plot")
locs, labels = plt.yticks()  # Get the current locations and labels.
plt.yticks(np.arange(0, 1.1, step=0.25))
plt.grid(axis = 'y')
plt.xlabel('Key')
plt.ylabel('CDF')
# plt.savefig("lognormal_cdf.png")
plt.show()


# YCSB - 20 bins? (magnitude of 1e-18, no 0.0 min on y; in theory needs 2 * 10^19 bins for proper y-axis)
# lognormal - 1000000 bins? (magnitude of 1e-8 on y, curve exceeds 1.0, no 0.0 min on y; in theory needs 10^14 bins for proper y-axis)
# longitudes - 357 bins
# longlat - 62500 bins

# notes:
# YCSB x-axis goes up to 1, in theory should go past 1
# YCSB only one that doesn't start at 0.0 for y
