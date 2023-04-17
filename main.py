import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190M.bin.data"
sequential_path = "datasets/sequential-dataset.txt"

file_name = lognormal_path
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


rand_dataset = np.random.randn(10000)  # generate samples from normal distribution (discrete data)
rand_dataset.sort()

# randArr = np.random.randint(0, 10, 5)
# randArr.sort()


cdf = scipy.stats.norm.cdf(arr)

# plot the cdf
print("plotting line...")

# for empirical cdf add drawstyle="steps-post" as 3rd parameter in next line
my_plot = sns.lineplot(x=arr, y=cdf)
# plt.savefig(my_plot)
print("showing graph...")
plt.show(block=True)


# https://stats.stackexchange.com/questions/381588/how-does-this-code-find-the-cdf
