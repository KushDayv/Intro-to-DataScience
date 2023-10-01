import matplotlib.pyplot as plt

x1 = [2,3,4]
y1 = [5,5,5]
x2 = [1,2,3,4,5]
y2 = [2,3,2,3,4]
y3 = [6,8,7,8,7]

plt.scatter(x1,y1,label="gw")
plt.scatter(x2, y2, label="geo", marker='v', color='r')
plt.scatter(x2, y3, label="Samuel", marker='^', color='m')
plt.title('Scatter Plot')
plt.legend()
plt.show()

''' 
"." point
"," pixel
"o" circle
"v" triangle_down
"^" triangle_up 
'''
