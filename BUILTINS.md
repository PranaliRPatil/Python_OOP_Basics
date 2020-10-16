# Python Built-in Functions
**[Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-funcs)** are the functions of **Python interpreter**. Let see some of them with examples :

1. ### **abs(x: int/float)**:
   Return the absolute value (magnitude) of a number.
   ```python
      >>> var = -10
      >>> abs(var)
      10 
    ```

2. ### **all(iterable)**:
    Return True if all elements of the iterable are true (or if the iterable is empty).
    Its somewhat similar to AND operation.
    ``` python
      >>> my_list1 = [1,'',2]
      >>> all(my_list1)
      False
      >>> my_list2 = [1,'a',2]
      >>> all(my_list2)        
      True
      >>> my_list3 = []        
      >>> all(my_list3) 
      True
    ```

3. ### **any(iterable)**:
    Return True if any element of the iterable is true. If the iterable is empty, return False.
    Its somewhat similar to OR operation.
    ``` python
      >>> my_list = [1,'',2]
      >>> any(my_list)
      True
      >>> my_list1 = [0,'',[]]
      >>> any(my_list1)
      False
      >>> my_list2 = []        
      >>> any(my_list2) 
      False
    ```
    
4. ### **bin(x)**:
   Convert an integer number to a binary string prefixed with “0b”.
   ```python
      >>> bin(10)
      '0b1010'
    ```

5. ### **bool(x)**:
   Return a Boolean value, i.e. one of True or False. If x is false or omitted (any of like blank string/list/dictionary), this returns False; otherwise it returns True. 
   ```python
      >>> bool([])
      False
      >>> bool('ab')
      True 
   ```

6. ### **zip(*iterables)**:
   The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity. zip() should only be used with unequal length      inputs when you don’t care about trailing, unmatched values from the longer iterables.
   ```python
      >>> x = [1, 2, 3]
      >>> y = [4, 5, 6]
      >>> zipped = zip(x, y)
      >>> list(zipped)
      [(1, 4), (2, 5), (3, 6)]
    ```
