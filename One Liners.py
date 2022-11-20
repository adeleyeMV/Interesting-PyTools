#1
#One Liner If-Else in Python
isReady = False

# A regular if-else
if isReady:
    print("Yay")
else:
    print("Nope")
    
# A neat little shorthand
print("Yay") if isReady else print("Nope")


#2
#Swap two variable without a helper variable
a = 1
b = 2

a, b = b, a

# Now a = 2 and b = 1


#3
#Chain Ckmparisons
x > 0 and x < 200
0 < x < 200

#4
#One liners or loop in python
numbers = [1, 2, 3, 4, 5]
[num * num for num in numbers]


#4
#Lambda Expression
numbers = [1, 2, 3, 4, 5, 6]
list(filter(lambda x : x % 2 == 0 , numbers))


#5
#Repeat string using loops
print("word" * 4)


#6
#Reverse a string in python
sentence = "This is just a test"
sentence[::-1]


#7
#Simplied if statement condition
if n == 0 or n == 1 or n == 2 or n == 3 or n == 4 or n == 5:
  
if n in [0, 1, 2, 3, 4, 5]


#8
#Find the Most Frequent Element in a List in Python
max(set(nums), key = nums.count)
nums = [2, 2, 6, 2, 2, 3, 4, 2, 13, 2, 1]
max(set(nums), key = nums.count)


#9
#Tear Values to Variables from a List
arr = [1, 2, 3]
a, b, c = arr
print(a, b, c)


#10
#Use F-Strings to Format Strings in Python
name = "Matt"
age = 25

sentence = f"Hi, I'm {name} and I'm {age} years old"
print(sentence)



#11
#Join a list of string in python
words = ["This", "is", "a", "Test"]
print(" ".join(words))
