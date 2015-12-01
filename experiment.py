import matplotlib.pyplot as plt
import numpy as np

def score(A):
	N = np.arange(0.0, A+1, 1) # position
	return 101 + 1000*np.log(A) - 1000*np.log(N)

fig = plt.figure()
ax = fig.add_subplot(111) 


ax.plot(score(5), 'ro', label='A = 5') 


ax.plot(score(50), 'bx', label='A = 50') 


ax.plot(score(100), 'g^', label='A = 100') 

ax.legend(loc='upper left')
# plt.axis([0, 100, 0, 100])
plt.title("System II: Weight Scoring")
plt.ylabel('Score')
plt.xlabel('Postition')
plt.show()

"""
A = 5.0 # number of boats
N = np.arange(0.0, A, 1) # position
score_5 = 101 + 1000*np.log(A) - 1000*np.log(N)
plt.plot(N, score, 'g^')

A = 50.0 # number of boats
N = np.arange(0.0, A, 1) # position
score = 101 + 1000*np.log(A) - 1000*np.log(N)
plt.plot(N, score, 'r--')

A = 100.0 # number of boats
N = np.arange(0.0, A, 1) # position
score = 101 + 1000*np.log(A) - 1000*np.log(N)
plt.plot(N, score, 'bs')

plt.ylabel('score')
plt.show()
"""