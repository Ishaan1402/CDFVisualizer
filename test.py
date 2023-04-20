import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats


sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = test_lognormal_path
print("opening file: " + file_name)

# read binary
f = open(file_name, "rb")

# read text
# f_text = open(file_name, "r")

print("creating float array...")
# arr = np.fromfile(f_text, dtype=np.int)
arr = f.read().split()
# my_arr = np.load(lognormal_path)
# print(arr)

# arr = np.fromfile(f_text, dtype=np.float)
print("sorting array...")
arr.sort()

key_type = int

rand_dataset = np.random.randn(10000)  # generate samples from normal distribution (discrete data)
rand_dataset.sort()
if file_name is lognormal_path or test_lognormal_path:
    key_type = np.int_
elif file_name is longlat_path:
    key_type = np.float

# randArr = np.random.randint(0, 10, 5)
# randArr.sort()
with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# for i in range(10):
#     print(arr[i])

cdf = scipy.stats.norm.cdf(arr)
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
# plt.savefig("CDFplot.png")
plt.show()