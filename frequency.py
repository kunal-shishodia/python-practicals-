s = input("enter a string to check" )

freq = {}
for c in s:
   if c in freq:
       freq[c] += 1
   else:
       freq[c] = 1
print(freq)
