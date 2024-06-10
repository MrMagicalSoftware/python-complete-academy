import hashlib
 
# encoding GeeksforGeeks using md5 hash
# function 
result = hashlib.md5(b'GeeksforGeeks')
 
# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end ="")
print(result.digest())