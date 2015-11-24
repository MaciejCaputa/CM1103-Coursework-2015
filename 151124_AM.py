Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> def birthdayProb(n):
    if n > 365:
        return 1.0
    
    p_diff = (math.factorial(365) / math.factorial(365 - n)) / (365.0 ** n)
    return 1 - p_diff
... ... ... ... ... ... 
>>> 
>>> import math
>>> 
>>> birthdayProb(10)
0.11694817771107757
>>> birthdayProb(20)
0.41143838358058005
>>> birthdayProb(25)
0.5686997039694639
>>> 
>>> 
>>> import pylab

>>> >>> 
>>> def plotBirthdays(n):
    p = []
    for x in range(1, n + 1):
        p.append(birthdayProb(x))

    pylab.plot(range(1, n + 1), p, '.-')
    pylab.xlabel('n')
    pylab.ylabel('Prob shared birthday')
    pylab.show()
... ... ... ... >>>   File "<stdin>", line 1
    pylab.plot(range(1, n + 1), p, '.-')
    ^
IndentationError: unexpected indent
>>>   File "<stdin>", line 1
    pylab.xlabel('n')
    ^
IndentationError: unexpected indent
>>>   File "<stdin>", line 1
    pylab.ylabel('Prob shared birthday')
    ^
IndentationError: unexpected indent
>>>   File "<stdin>", line 1
    pylab.show()
    ^
IndentationError: unexpected indent
>>> def plotBirthdays(n):
    p = []
    for x in range(1, n + 1):
        p.append(birthdayProb(x))
    
    pylab.plot(range(1, n + 1), p, '.-')
    pylab.xlabel('n')
    pylab.ylabel('Prob shared birthday')
    pylab.show()
... ... ... ... ... ... ... ... ... 
>>> 
>>> plotBirthdays(100)

>>> >>> 
>>> math.factorial(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: factorial() not defined for negative values
>>> 