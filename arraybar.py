#Importing the required libraries and modules
import matplotlib.pyplot as plt 
import numpy as np 

#Creating the data values for the vertical y and horizontal x axis 

x = np.array(["BSE","BBIT","BSCIT","BCS","BCM"])
y = np.array([200,400,250,180,180])

#Using the pyplot.bar function 
plt.bar(x,y)
plt.plot()
plt.xlabel("COURSE")
plt.ylabel("Number of students")
plt.title("Intake as per the courses")

#showing the graph
plt.show()

