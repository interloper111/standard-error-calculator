import numpy as np
from standard_error import find_standard_errors

data = np.genfromtxt("data.txt",dtype='float',delimiter=',',skip_header=0)

print(find_standard_errors(data))
