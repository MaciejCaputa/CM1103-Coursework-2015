Python 3.4.3 |Anaconda 2.3.0 (x86_64)| (default, Mar  6 2015, 12:07:41) 
[GCC 4.2.1 (Apple Inc. build 5577)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> a = [1, 2, 3]
>>> a[:].remove(1).remove(2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'remove'
>>> type(a[:].remove(1))
<class 'NoneType'>
>>> 
>>> 
>>> def bob():
...    return 5, 6
... 
>>> 
>>> bob()
(5, 6)
>>> a = bob()
>>> 
>>> a[0]
5
>>> a[1]
6
>>> a, b = bob()
>>> a
5
>>> b
6
>>> 
>>> 
>>> from probability import *
>>> monty(1)
 car door :  1
 selection :  1
 goat door :  2
(1, 0)
>>> monty(10)
 car door :  1
 selection :  3
 goat door :  2
 car door :  2
 selection :  2
 goat door :  3
 car door :  1
 selection :  1
 goat door :  2
 car door :  3
 selection :  3
 goat door :  1
 car door :  2
 selection :  1
 goat door :  3
 car door :  2
 selection :  1
 goat door :  3
 car door :  2
 selection :  2
 goat door :  1
 car door :  2
 selection :  1
 goat door :  3
 car door :  1
 selection :  1
 goat door :  2
 car door :  3
 selection :  1
 goat door :  2
(5, 5)
>>> 
>>> 
>>> from probability import *
>>> monty(10)
 car door :  3
 selection :  1
 goat door :  2
 car door :  1
 selection :  3
 goat door :  2
 car door :  2
 selection :  2
 goat door :  1
 car door :  2
 selection :  3
 goat door :  1
 car door :  1
 selection :  1
 goat door :  3
 car door :  1
 selection :  2
 goat door :  3
 car door :  1
 selection :  3
 goat door :  2
 car door :  3
 selection :  1
 goat door :  2
 car door :  3
 selection :  3
 goat door :  2
 car door :  1
 selection :  2
 goat door :  3
(3, 7)
>>> import probability
>>> probility.monty(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'probility' is not defined
>>> probability.monty(10)
 car door :  1
 selection :  1
 goat door :  3
 car door :  1
 selection :  3
 goat door :  2
 car door :  3
 selection :  1
 goat door :  2
 car door :  2
 selection :  3
 goat door :  1
 car door :  3
 selection :  3
 goat door :  1
 car door :  3
 selection :  3
 goat door :  1
 car door :  2
 selection :  2
 goat door :  3
 car door :  1
 selection :  2
 goat door :  3
 car door :  2
 selection :  2
 goat door :  1
 car door :  1
 selection :  1
 goat door :  3
(6, 4)
>>> reload(probability)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reload' is not defined
>>> 