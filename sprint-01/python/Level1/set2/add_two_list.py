''' 
### Problem **5: Concatenate two lists index-wise**

Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

**Given**:

```
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
```

**Expected output:**
['My', 'name', 'is', 'Kelly']
'''

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# Find the length of the shorter list
min_len = min(len(list1), len(list2))

# Initialize the result list
result = []

# Concatenate elements index-wise
for i in range(min_len):
    result.append(list1[i] + list2[i])

# Add any remaining elements from the longer list
result.extend(list1[min_len:])
result.extend(list2[min_len:])

print(result)
