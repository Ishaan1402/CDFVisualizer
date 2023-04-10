import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

longlat_path = "/users/ipatel9/dataset/longlat-200M.bin.data"
lognormal_path = "/users/ipatel9/dataset/lognormal-190.bin.data"
sequential_path = "/users/ipatel9/dataset/sequential-dataset.txt"

file_name = longlat_path
print("opening file: " + file_name)

# read binary
f = open(file_name, "rb")

# read text
f_text = open(file_name, "r")

print("creating float array...")
arr = np.fromfile(f, dtype=np.float)
print("sorting array...")
arr.sort()


# rand_dataset = np.random.randn(10000) # generate samples from normal distribution (discrete data)
# rand_dataset.sort()

# randArr = np.random.randint(0, 10, 5)
# randArr.sort()

# print(randArr)

# norm_cdf = scipy.stats.norm.cdf(randArr)  # calculate the cdf - also discrete
print("arranging in evenly spaced values (CDF)...")
new_cdf = np.arange(1, len(arr)+1)/float(len(arr))
# mass_cdf = np.arange(1, len(rand_dataset)+1)/float(len(rand_dataset))

# plot the cdf
print("plotting line...")
sns.lineplot(x=arr, y=new_cdf, drawstyle="steps-post")
print("showing graph...")
plt.show(block=True)


# https://stats.stackexchange.com/questions/381588/how-does-this-code-find-the-cdf
