Python Notes

* Usage of sets

```python
# list to sets
set([1,2,2,3,4])

# sets to list
list(set([1,2,2,3,4]))
```

* Switch

```python
switcher = {
    0: "zero",
    1: "one",
    2: "two",
  }
  return switcher.get(argument, "nothing")
```

* XOR

```python
z = x ^ y
```

* join

```python
",".join(["a", "b", "c"])
```

* reverse a string

```python
x = "abc"
x[::-1]
```

* iterate through a list with index

```python
l = ['a','b','c']
for idx, val in enumerate(l):
  print(l)
```

* remove element from list by index

```python
l = ['a','b','c']
del l[0]
del l[-1]
```

* copy a list

```python
l = ['a','b','c']
m = l[:]
```

* prepend in a list

```python
l = ['a','b','c']
l.insert(0,'z')
```

* maxint

```python
import sys
sys.maxsize
```

* reduce

```python
# in Python3, reduce is removed, use functools.reduce
import operator, functools
functools(operator.add, [1,2,3])
```

* Performance issue

Use \*+- > / > \*\*
Use as less as space
Use no imports (other than high performance collections)

* MySQL is null

```SQL
-- you need to use is null to judge field instead of = null
```

* loop

```python
for i in range(2,2):
  print(i)
```

will print out nothing, since the loop is never entered

* sort a string

```python
s = '4387'
sorted(s) # ['3','4','7','8']
```

* usage of zip

```python
matrix = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

# row to column
list(zip(*matrix))
# [
# [1,4,7],
# [2,5,8],
# [3,6,9]
# ]

# rotate
list(zip(*matrix))[::-1]

# [
# [3,6,9],
# [2,5,8],
# [1,4,7]
# ]
#
```
