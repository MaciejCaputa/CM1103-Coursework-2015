import matplotlib.pyplot as plt
examMarks=[25,72,83,91,61]
cwkMarks=[64,84,92,73,77]
plt.plot(examMarks, cwkMarks, 'bx')
plt.ylabel('Cwk mark')
plt.xlabel('Exam mark')
plt.title('Marks')
plt.axis([0, 100, 0, 100])
plt.show()