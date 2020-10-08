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
