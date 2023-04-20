import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats


sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = lognormal_path
print("opening file: " + file_name)

# read binary
with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=np.int_)


# for i in range(10):
#     print(arr[i])

# arr = np.divide(arr, np.sum(arr))

# plot the cdf
print("plotting line...")
# Create CDF
counts, bin_edges = np.histogram(arr, bins=10000000, density=True)
cdf = np.cumsum(counts)
# cumulative_prob = cdf / float(len(arr))

# for empirical cdf add drawstyle="steps-post" as 3rd parameter in next line
my_plot = sns.lineplot(x=arr, y=cdf)
# plt.savefig(my_plot)
print("showing graph...")
plt.show(block=True)
# Plot CDF
plt.plot(bin_edges[1:], cdf)
plt.xlabel('Key')
plt.ylabel('CDF')
plt.savefig("testCDFplot.png")
# plt.show()
