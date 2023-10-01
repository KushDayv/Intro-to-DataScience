import matplotlib.pyplot as plt
x1 = ["BSE","BBIT","BSCIT","BCS","BCM"]
y1 = [200,400,250,180,180]

plt.bar(x1,y1,label = "yellow Bar", color='y')
plt.plot()
plt.xlabel("COURSE")
plt.xlabel("Number of students")
plt.ylabel("Intake as per the courses")
plt.legend()
plt.show()
