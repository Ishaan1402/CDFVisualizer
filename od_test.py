import numpy as np
import matplotlib.pyplot as plt

# Test Paths
sequential_path = "datasets/sequential-dataset.txt"
test_lognormal_path = "datasets/lognormal-190M.bin.data"
test_longlat_path = "datasets/longlat-200M.bin.data"
test_longitudes_path = "datasets/longitudes-200M.bin.data"
test_ycsb_path = "datasets/ycsb-200M.bin.data"
test_amazon_path = "datasets/amazon.out.text"
test_enron_path = "datasets/enron.out"
test_cit_path = "datasets/cit-patents.out"
test_fb_path = "datasets/fb-wall.out"

# True Paths
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"
longitudes_path = "/users/ipatel9/dataset/longitudes-200M.bin.data"
ycsb_path = "/users/ipatel9/dataset/ycsb-200M.bin.data"
enron_path = "/users/ipatel9/dataset/enron.out"
amazon_path = "/users/ipatel9/dataset/amazon.out.text"
cit_path = "/users/ipatel9/dataset/cit-patents.out"
fb_path = "/users/ipatel9/dataset/fb-wall.out"


file_name = longlat_path
key_type = np.int64

if file_name == lognormal_path or file_name == test_lognormal_path or file_name == ycsb_path or file_name == test_ycsb_path:
    key_type = np.int_
elif file_name == longlat_path or file_name == test_longlat_path or file_name == test_longitudes_path or file_name == longitudes_path:
    key_type = np.float

# uncomment for binary file
with open(file_name, 'rb') as file:
    arr = np.fromfile(file, dtype=key_type)

# uncomment for text files
# arr = np.loadtxt(file_name)


print("length of arr: ", len(arr))

# Create a plot of the CDF
ecdf = np.arange(1, len(arr)+1) / len(arr)
arr.sort()

# Plot the eCDF
print("plotting cdf...")
plt.step(arr, ecdf)

title_font = {'family' : 'sans-serif',
        'fontweight' : 'medium',
        'size'   : 26}

axis_font = {'family' : 'sans-serif',
        'fontweight' : 'medium',
        'size'   : 20}

plt.title("longlat", **title_font)
plt.xlabel('Key', **axis_font)
# plt.ylabel('CDF', **axis_font)
plt.subplots_adjust(bottom=0.15)
locs, labels = plt.yticks()
plt.yticks(np.arange(0, 1.1, step=0.25))
ax = plt.gca()
ax.get_yaxis().set_visible(False)
plt.grid(axis = 'y')
print("saving plot...")
plt.savefig("longlat_ecdf.png")
# plt.show()
