# SortingAlgorithm
 
This algorithm sorts 10 totally random numbers.
It loops through the entire list of number 100 times. When a number is larger than the number after that one it switches places with those two.
Example:
``` python
if Current[y] > Current[y+1]:
    Memory = Sort[y]
    Current[y] = Current[y+1]
    Current[y+1] = Memory
```
variable y is the current number
y+1 is the next number