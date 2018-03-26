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
