import matplotlib.pyplot as plt
examMarks=[25,72,83,91,61]
plt.plot(examMarks, 'ro')
plt.axis([0, 4, 0, 100])
plt.title("Exam Marks")
plt.ylabel('Mark')
plt.xlabel('Student')
plt.show()
