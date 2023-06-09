import numpy as np
import matplotlib.pyplot as plt

sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"

file_name = test_longlat_path
key_type = np.int

if file_name == lognormal_path or file_name == test_lognormal_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path:
    key_type = np.float

# uncomment for binary file
with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# uncomment for text files
# arr = np.loadtxt(file_name)


# countFreq counts the frequencies of each unique key and inputs them into a new array where the
# frequencies are listed for each ith number
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
print("starting countFreq...")
counts_arr = countFreq(arr)

print("length of arr: ", len(arr))
for i in range(10):
    print(arr[i])
print("length of counts_arr: ", len(counts_arr))
for i in range(10):
    print(counts_arr[i])

# Calculate the probability density function
pdf = np.divide(counts_arr, len(arr))

# Calculate the cumulative distribution function
cdf = np.cumsum(pdf)

# Create a plot of the CDF
plt.plot(np.arange(len(cdf)), cdf)
plt.title('Lognormal CDF')
plt.xlabel('Keys')
plt.ylabel('CDF')
print("saving plot...")
# plt.savefig("updatedCDFPlot.png")
plt.show()