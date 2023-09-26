import numpy as np


python_lst = [i for i in range(100)]
print("python_lst: ", python_lst)

np_arr = np.array(python_lst)

print("np_arr: ", np_arr)

np_arr_zeros = np.zeros(100)
print("np_arr_zeros: ", np_arr_zeros)



lst = ["fun stuff in here, every data type", 1, 100, 5.55]
np_whoops = np.array(lst)

print(np_whoops, "everything is a string now")