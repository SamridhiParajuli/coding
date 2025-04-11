A = [1,2,3]
print(A)

#Apped on the end - on average O(1)

A.append(5)
print(A)

#Delete from end of array
A.pop()
print(A)

#insert at the other position but not the end - O(N)
A.insert(2,5) #at position 2 insert 5
print(A)

#Modify the element - O(1)

A[0] = 7
print(A)

#accessing any array - O(1)
print(A[1])

if 7 in A:
    print (True)


#strings
#append
S="Hello"
b = S + 'z'
print(b)

#check if something in the string

if 'e' in S:
    print(True)


#length O(1)
print(len(A))