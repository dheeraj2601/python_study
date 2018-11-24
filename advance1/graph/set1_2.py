import matplotlib.pyplot as plt

x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1, y1, label="line1")

x2 = [2,4,5]
y2 = [1,5,3]
plt.plot(x2, y2, label="line2")

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title ("two line same graph")
plt.legend()
plt.show()
