
data = (1, 2, 3, 4, 5, 6, 7, 8,9,10)  
n = len(data)

# Print half of the tuple in one line and the other half in the next line
print("First half:", data[:n//2])
print("Second half:", data[n//2:])

# Find and return the maximum and minimum values
max_value = max(data)
min_value = min(data)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
