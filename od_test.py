import numpy as np
import matplotlib.pyplot as plt

sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
test_longitudes_path = "datasets/longitudes-200M.bin.data"
test_ycsb_path = "datasets/ycsb-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"
longitudes_path = "/users/ipatel9/dataset/longitudes-200M.bin.data"
ycsb_path = "/users/ipatel9/dataset/ycsb-200M.bin.data"
amazon_path = "datasets/amazon.out.text"
test_enron_path = "datasets/enron.out"
enron_path = "/users/ipatel9/dataset/enron.out"

file_name = longitudes_path
key_type = np.int64

if file_name == lognormal_path or file_name == test_lognormal_path or file_name == ycsb_path or file_name == test_ycsb_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path or file_name == test_longitudes_path or file_name == longitudes_path:
    key_type = np.float

# uncomment for binary file
# with open(file_name, 'rb') as file:
#     arr = np.fromfile(file, dtype=key_type)

# uncomment for text files
arr = np.loadtxt(file_name)


# countFreq counts the frequencies of each unique key and inputs them into a new array where the
# frequencies are listed for each ith number
# def countFreq(array):
#     freq_dict = {}
#     for num in array:
#         if num in freq_dict:
#             freq_dict[num] += 1
#         else:
#             freq_dict[num] = 1
#
#     unique_nums = list(freq_dict.keys())
#     unique_nums.sort()
#
#     freq_arr = [0] * len(unique_nums)
#     for i, num in enumerate(unique_nums):
#         freq_arr[i] = freq_dict[num]
#
#     return freq_arr


# Create array counting the occurrences of integers in arr and return their frequency at each index
# print("start countFreq")
# counts_arr = countFreq(arr)

print("length of arr: ", len(arr))
# print(arr)
# print("length of count_arrs: ", len(counts_arr))
# print(counts_arr)

# Calculate the probability density function
# pdf = np.divide(counts_arr, len(arr))

# Calculate the cumulative distribution function
# cdf = np.cumsum(pdf)

# Create a plot of the CDF
ecdf = np.arange(1, len(arr)+1) / len(arr)
arr.sort()

# Plot the eCDF
plt.step(arr, ecdf)
# plt.step(arr.sort(), cdf)
locs, labels = plt.yticks()  # Get the current locations and labels.
plt.yticks(np.arange(0, 1.1, step=0.25))
plt.grid(axis = 'y')
plt.title('Enron')
plt.xscale("log")
plt.xlabel('Key')
plt.ylabel('CDF')
print("saving plot...")
plt.savefig("enron_ecdf.png")
# plt.show()


