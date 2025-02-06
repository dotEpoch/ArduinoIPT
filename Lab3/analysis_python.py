import numpy as np
import matplotlib.pyplot as plt

path = "P:\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt"


# We open and read the data and put it into a list as a single string.
with open(path, "r") as doc:
    content = doc.read()
    string_data = content.split()

print("Data in list string format: ", string_data)
print()

# String is split by the ',' and put into a list.
data_split = string_data[0].split(',')

print("Data split: ", data_split)
print()

# We now extract the individual data points and turn into integers and put into
# a new data list.

data = []
for index in range(len(data_split) - 1):
    data.append(int(data_split[index]))

print("Pure raw data in integer form: ", data)

counts, bins = np.histogram(data)
plt.stairs(counts, bins, fill=True)
plt.show()
    