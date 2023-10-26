''' ### Problem **3: Append new string in the middle of a given string**

Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

**Given**:

```
s1 = "Ault"
s2 = "Kelly"
```
'''

s1 = "Ault"
s2 = "Kelly"

# Calculate the middle index of s1
middle = len(s1) // 2

# Create the new string s3 by combining the first half of s1, s2, and the second half of s1
s3 = s1[:middle] + s2 + s1[middle:]

print(s3)

