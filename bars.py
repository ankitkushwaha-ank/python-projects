import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2,4,4,6,6]

# Create a new figure
plt.figure()

# Plot the data
plt.plot(x,y, marker='o', linestyle='-', color='b', label='Prime Numbers')

# Add a title
plt.title('Sample Line Graph')

# Label the x and y axes
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Add a legend
plt.legend()

# Display the plot
plt.show()

# import matplotlib.pyplot as plt
#
# x = [2,4,6,8,9]
# y = ['ankit,saurav,adarsh,umkwon,aayushi']
#
# plt.figure()
#
# plt.plot(x,y, marker='o', linestyle='-', color='b', label='Prime Numbers')
#
# plt.title('reesult')
#
# plt.xlabel('X axis')
# plt.ylabel('Y axis')
#
# plt.legend()
# plt.show()