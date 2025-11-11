# Bookbot

BookBot reads text file and provides statistics on the content. It counts the total number of words and how often each character appears.

This is the starter code used in Boot.dev's [Build a Bookbot in Python](https://www.boot.dev/courses/build-bookbot-python) course.

---

## Requirements

- Python 3

---

## Installation

1. Clone the repository.

---

## Usage

### Analize a file
```bash
python3 main.py <path/to/input.txt>
```

#### Example
```bash
python3 main.py books/Frankenstein.txt
```

#### Output
```bash
============ BOOKBOT ============
Analyzing book found at books/Frankenstein.txt...
----------- Word Count ----------
Found 73859 total words
--------- Character Count -------
e: 42874
t: 28190
a: 25115
i: 23142
o: 23039
n: 22530
s: 19545
r: 19057
h: 18834
d: 15738
l: 11824
m: 9858
u: 9571
c: 8625
f: 8052
y: 7404
w: 7154
p: 5727
g: 5360
b: 4588
v: 3771
k: 1502
x: 671
j: 403
q: 308
z: 234
============= END ===============
```
