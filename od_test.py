import numpy as np
import matplotlib.pyplot as plt

# Generate random height data
sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = sequential_path
key_type = int

if file_name == lognormal_path or file_name == test_lognormal_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path:
    key_type = np.float

with open(file_name, 'r') as file:
    arr = np.fromfile(file, dtype=key_type)


def countFreq(array):
    freq_dict = {}
    for num in array:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    unique_nums = list(freq_dict.keys())
    unique_nums.sort()

    freq_arr = [0] * len(unique_nums)
    for i, num in enumerate(unique_nums):
        freq_arr[i] = freq_dict[num]

    return freq_arr


# Create array counting the occurrences of integers in arr and return their frequency at each index
counts_arr = countFreq(arr)

print(len(counts_arr))
print(len(arr))

# Calculate the probability density function
pdf = np.divide(counts_arr, len(arr))

# Calculate the cumulative distribution function
cdf = np.cumsum(pdf)

# Create a plot of the CDF
plt.plot(np.arange(len(cdf)), cdf)
plt.xlabel('Value')
plt.ylabel('CDF')
plt.show()


