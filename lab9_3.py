import matplotlib.pyplot as plt
examMarks=[25,72,83,91,61]
cwkMarks=[64,84,92,73,77]
fig = plt.figure()
ax = fig.add_subplot(111) 
ax.plot(examMarks, 'ro', label='Exam') 
ax.plot(cwkMarks, 'bx', label='Cwk') 
ax.legend(loc='upper left')
plt.show()