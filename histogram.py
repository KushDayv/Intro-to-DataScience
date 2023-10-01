import matplotlib.pyplot as plt
import numpy as np 

n = 5 + np.random.randn(1000) #used to generate an array of random numbers from a normal distribution (also called Gaussian distribution or a bell curve)

m = [m for m in range (len(n))]
plt.bar(m,n)
plt.title("Raw Data")
plt.show()

'''Bins which are the number of intervals that one can use to divide all of your data into such that 
it can be displayed as bars on histogram '''

#width = (1000 - 0) / 20 = 200

plt.title("Histogram")
plt.show()

#When the cumulative is set to True these functions, it means that the operation will be performed cumulatively on the elements of the array
plt.hist(n, cumulative=True, bins=20, edgecolor="yellow", color="green")
plt.title("Cumulative Histogram")
plt.show()

