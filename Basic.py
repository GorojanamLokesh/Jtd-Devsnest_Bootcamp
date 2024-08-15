# Example 1
# Input:
#     World
# Output:
#     Hello, World
# Example 2
# Input:
#     John
# Output:
#     Hello, John

user_name=input()
print("Hello, " +user_name)


# Input:
#     4
# Output:
#     7

num1=int(input())
num2=3
num3=num1+num2
print(num3)

# Example 1
# Input:
#     4
# Output:
#     1

num1=int(input())
num2=3
num3=num1-num2
print(num3)


# Input:
#     4
# Output:
#     12

num1=int(input())
num2=3
num3=num1*num2
print(num3)

# Example 1
# Input:
#     6
# Output:
#     2.0

num1=int(input())
num2=3
num3=num1/num2
print(num3)

# Example 1
# Input:
#     4
# Output:
#     1

num1=int(input())
num2=3
num3=num1%num2
print(num3)

# Example 1(operators=====>>>>)
# Input:
#     10
#     4
#     7
# Output:
#     10
# Example 2
# Input:
#     5
#     11
#     4
# Output:
#     11\

num1=int(input())
num2=int(input())
num3=int(input())
if num1 >= num2 and num1>=num3:
    print(num1)
elif num2 >=num1 and num2 >=num3:
    print(num2)
else:
    print(num3)

#   Example 1
# Input:
#     32
#     11
# Output:
#     32
# Example 2:
# Input:
#     17
#     44
# Output:
#     44  
num1=int(input())
num2=int(input())
if num1>num2:
    print(num1)
else:
    print(num2)

#     Example 2
# Input:
#     multiply
#     30
#     5
# Output:
#     150
# Example 3
# Input:
#     divide
#     5
#     0
# Output:

operation=input()
num1=int(input())
num2=int(input())
if operation=="add":
    print(num1+num2)
elif operation=="subtract":
    print(num1-num2)
elif operation=="multiply":
    print(num1*num2)
elif operation=="divide":
    if num2!=0:
        print(num1/num2)
    else:
        print("cannot be divided by zero")

#         Example 1
# Input:
#     4
#     5
# Output:
#     False
# Example 2
# Input:
#     9
#     9
# Output:
#     True
num1=int(input())
num2=int(input())
if num1==num2:
    print("True")
else:
    print("False")


# Example 1
# Input:
#     4
#     5
# Output:
#     True
# Example 2
# Input:
#     9
#     9
# Output:
#     False

num1=int(input())
num2=int(input())
if num1!=num2:
    print("True")
else:
    print("False")

#   Input:
#     45
#     30
# Output:
#     Student passed!
# Example 2
# Input:
#     50
#     70
# Output:
#     Student failed!  


score=int(input())
threshold=int(input())
if score>threshold:
    print("Student passed!")
else:
    print("Student failed!")

#  Example 1
# Input:
#     55
# Output:
#     The number is less than 100
# Example 2
# Input:
#     100
# Output:
#     The number is equal to 100
# Example 3
# Input:
#     123

# Output:
   
num=int(input())
if num<100:
    print("The number is less than 100")
else:
  if num==100:
    print("The number is equal to 100")
  else:
     if num>100:
      print("The number is greater than 100")

# Example 1 (loops===>>>)
# Input:
#     35
#     citizen
# Output:
#     You are eligible to vote.
# Example 2
# Input:
#     23
#     non-citizen
# Output:
#     You are not eligible to vote. 
# 
age=int(input())
citizenship_status=input()
if age>=18 and citizenship_status=="citizen":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

        
# Example 1
# Input:
#     300
#     False
# Output:
#     You are eligible for free shipping.
# Example 2
# Input:
#     21
#     False
# Output:
#     You are not eligible for free shipping. 
# 
totalorderAmount=int(input())
premiumMember=input()
if totalorderAmount>=50 or premiumMember=="True":
    print("You are eligible for free shipping.")
else:
    print("You are not eligible for free shipping.")    

# Example 1
# Input:
#     25
# Output:
#     300       

age=int(input())
print(age*12)


# Example 1
# Input:
#     5
#     5
#     3
# Output:
#     Isosceles triangle
# Example 2
# Input:
#     3
#     4
#     5
# Output:
#     Scalene triangle
# Example 3
# Input:
#     7
#     4
#     3
# Output:
#     Not a valid triangle!

side1=int(input())
side2=int(input())
side3=int(input())

if side1 <=0 or side2 <=0 or side3 <=0:
    print("Not a valid triangle!")
elif side1+ side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("Not a valid triangle!")
elif side1 ==side2 ==side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Isosceles triangle")
else:
    print("Scalene triangle")    


#  Input:
#     2
#     7
# Output:
#     2
#     3 
#     4 
#     5 
#     6 
#     7   

num1=int(input())
num2=int(input())

for i in range(num1,num2+1):
    print(i)


#   Example 1
# Input:
#     !dlroW ,olleH
# Output:
#     Hello, World!  
l=input()
x=len(l)

while x>0:
    print(l[x-1],end="")
    x-=1

# Example 1(patterns==>>>>)
# Input:
#     5
# Output:
#     1
#     12
#     123
#     1234
#     12345
# Example 2
# Input:
#     3
# Output:
#     1
#     12
#     123    

num=int(input())

for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Example 1
# Input:
#     5
# Output:
#     1
#    12
#   123
#  1234
# 12345

n= int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range (1,i+1):
        print(j,end="")
    print("")     


# Example 1
# Input:
#     5
# Output:
# 12345
#  1234
#   123
#    12
#     1    

n= int(input())
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    for j in range (1,i+1):
        print(j,end="")
    print("")     

# Example 1(List====>>>>)
# Input:
#     2 1 2 4 5
# Output:
#     2.8
# Explanation: The total sum is calculated as 2 + 1 + 2 + 4 + 5, resulting in 14. The average would be 14 / 5 = 2.8. 

string = input().split()
sum=0
count=0
for i in string:
    sum+=float(i)
    count+=1
average = sum/count
print(average)    


# Example 1
# Input:
#     6 1 4 0 9
#     2
# Output:
#     [6, 1, 4, 0]
#     [6, 1, 4]

string= [int(x) for x in input().split()]
poped=int(input())

for x in range (len(string),0,-1):
    string.pop()
    print(string)
    poped-=1
    if poped==0:
        break

#   Example 1
# Input:
#     add.subtract.multiply.divide
#     .
# Output:
#     ['add', 'subtract', 'multiply', 'divide'] 

s=input()
r=s.split(input())
print(r)

# Example 1
# Input:
#     Bob
#     25
# Output:
#     Hello, Bob! You are 25 years old.

name=input()
age=int(input())
print(f"Hello, {name}! You are {age} years old.")

# Example 1
# Input:
#     "   apple,  banana,  orange,   grapefruit, kiwi   "
# Output:
#     "apple banana orange grapefruit kiwi"
# Note: Print the result without quotes.

string=input().strip()
words=string.split(",")

cleaned_word=[word.strip() for word in words]
result_string=" ".join(cleaned_word)
print(result_string)


# Example 1
# Input:
#     2 7 8 5 0 1
#     5
# Output:
#     3
# Example 2
# Input:
#     1 5 1 1 2 1
#     3
# Output:
#     -1
# Example 3
# Input:
#     10 10 10 20
#     10
# Output:
#     0

def solve(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums=[2,7,8,5,0,1]
target = 5
print(solve(nums,target))

# Example 1
# Input:
#     3 4 -1 0 -5 -9 1 1 -2
# Output:
#     [3, 4, 1, 1]

abc= [int(x) for x in input().split()]
result = []
for x in abc:
    if x>0:
        result.append(x)
print(result)        

# Example 1:(Functions===>>>)
# Input:
#     "Mac"
# Output:
#     "Hello, Mac!"
# Explanation:
#     Given a String, Mac is Concatenated with string "Hello, " at the beginning and "!" at the end

def solve(str):
    return "Hello, "+str+"!"

    solve("Mac")

# Example 1:
# Input:
#     5
#     2
# Output:
#     21
# Explanation:
#     Sum is (5 + 2)  = 7 and Difference is (5 - 2) = 3. The product of Sum and Difference is 21.
# Example 2:
# Input:
#     -14
#     -4
# Output:
#     180
# Explanation:
#     The Sum is -18 and Difference is -10. The product is 180.

def solve(a, b):
    sum= a+b
    diff= a-b
    prod= sum*diff

    return prod #in define we use return so to avoid many print commands 

# Example 1:
# Input:
#     21
#     5
# Output:
#     16.8
# Explanation:
#     The int and float value of 21 / 5 is 4 and 4.2 respectively. The product is 16.8
# Example 2:
# Input:
#     11
#     4
# Output:
#     5.5
# Explanation:
#     The integer and float value of (11 / 4) is 2 and 2.75 respectively. The product is 5.5
def solve(a, b):
    # CODE HERE
    x=a/b
    y=a//b
    prod=x*y
    return prod #return consider as print

# Example 1:(Hashing===>>>)
# Input:
#     6
#     6 2 5 4 3 1
#     2
#     5
# Output:
#     3.25
# Explanation:
#     The elements between indices 2 and 5 are 5, 4, 3 and 1. The Average is: 
#          (5 + 4 + 3 + 1) / 4 = 3.25
# Example 2:
# Input:
#     2
#     7 2
#     0
#     1
# Output:
#     4.5
# Explanation:
#     The elements between indices 0 and 1 are 7 and 2. The average is:
#         (7 + 2) / 2 = 4.5

def solve(n, arr, x, y):
    
    total_sum= 0
    count= 0
    for i in range(x, y + 1):
        total_sum += arr[i]
        count += 1
    average = total_sum / count
    return average    

#Example 1:
# Input:
#     5
# Output:
#     1
#     121
#     12321
#     1234321
#     123454321
# Explanation:
#     The size of staircase is 5. So you have to generate string of integers in such a way that it is palindromic. 
# Example 2:
# Input:
#     3
# Output:
#     1
#     121
#     12321
def solve(n):
    result = []
    for i in range(1,n+1):
        half_stair=''
        for j in range(1,i+1):
            half_stair+=str(j)
        full_stair= half_stair+half_stair[-2::-1]
        result.append(full_stair)
    return result      


# Example 1:
# Input:
#     6
#     2 1 2 8 7 8
# Output:
#     7
# Explanation:
#     The second largest element is 7.
# Example 2:
# Input:
#     2
#     20 10
# Output:
#     10
# Explanation:
#     The second largest is 10.
# Constraints

def solve(n, arr):
    if n<2:
        return "Enter more than two numbers "
    largest=float('-inf')
    second_largest=float('-inf')
    for num in arr:
        if num>largest:
            second_largest=largest
            largest=num
        elif num>second_largest and num!=largest:
            second_largest=num
    return second_largest            

# Example 1
# Input: 
#     9
#     27
# Output:
#     ------------.|.------------
#     ---------.|..|..|.---------
#     ------.|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|.---
#     ---------DEVSNEST!---------
#     ---.|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|.------
#     ---------.|..|..|.---------
#     ------------.|.------------

def solve(M, N):
    arr=[]
    for i in range(1,M,2):
        arr.append((i*".|.").center(N,"-"))
    arr.append(("DEVSNEST!").center(N,"-"))
    for j in range(M-2,0,-2):
        arr.append((j*".|.").center(N,"-"))
    return arr

# Example 1:
# Input:
#     5 2
#     3 37
#     1 41
#     2 37
#     5 41
#     4 35
# Output:
#     2 3
# Explanation:
#      5 2 is the size of the leaderboard. The second lowest score is 37 and their corresponding players are 2 and 3.
# Example 2:
# Input:
#     7 2
#     1 41
#     3 47
#     6 41
#     4 50
#     7 36
#     2 47
#     5 50
# Output:
#     1 6
# Explanation:
#     7 2 is the size of the leaderboard. The second lowest score is 41 and the corresponding players are 1 and 6.
def solve(leaderboard):
    leaderboard.sort(key=lambda x: x[1])
    second=None
    for i in range(1,len(leaderboard)):
        if leaderboard[i][1]>leaderboard[i-1][1]:
            second=leaderboard[i][1]
            break
    
    result = []
    for player in leaderboard:
        if player[1]==second:
            result.append(player[0])
    
    return sorted(result)

# Example 1:

# Input: 
#       N=5
#       nums = 5 3 6 1 12
#       original = 3
# Output: 24
# Explanation: 
# - 3 is found in nums. 3 is multiplied by 2 to obtain 6.
# - 6 is found in nums. 6 is multiplied by 2 to obtain 12.
# - 12 is found in nums. 12 is multiplied by 2 to obtain 24.
# - 24 is not found in nums. Thus, 24 is returned.
# Example 2:
# Input: 
#       N=3
#       nums = 2 7 9
#       original = 4
# Output: 4
# Explanation:
# - 4 is not found in nums. Thus, 4 is returned.

def solve(N, nums, original):
    num=set(nums)
    while original in num:
        original *= 2
    return original

# Example 1:
# Input:
# 6
# 1 2 2 1 1 3
# Output: 
# 1
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
# Example 2:
# Input:
# 2
# 1 2
# Output: 
# 0
# Example 3:
# Input: 
# 10
# -3 0 1 -3 1 1 1 -3 10 0
# Output: 
# 1
def solve(N, arr):
    count={}
    for num in arr:
        count[num] = count.get(num,0)+1

    occurrence_count=list(count.values())
    unique_occurrence=len(set(occurrence_count))==len(occurrence_count)
    return 1 if unique_occurrence else 0


# Example 1
# Input:
#     Python is easy to learn.
# Output:
#     5
s=input().split()
print(len(s))

# Example 1:
# Input : 
#    4
#    2 7 11 15
#    9
# Output : 
#     0 1
# Explaination : nums[0] + nums[1] == 9, return 0, 1
# Example 2:
# Input : 
#     3
#     3 2 4
#     6
# Output : 
#      1 2
def solve(n, nums, target): #3[ 3,2 4], 6
    d={} # d[3]=0,d[2]=1,
    for i in range(n): #n=0,1,2
        cnum=nums[i] 
        p=target-cnum 
        if p in d:
            return [d[p],i]
        d[cnum]=i

#  Example 1:
# Input:
# book
# Output: 
# 1
# Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
# Example 2:
# Input: 
# textbook
# Output: 
# 0
# Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
# Notice that the vowel o is counted twice.       

def solve(s): #book
    n=len(s) #4
    a=s[:n//2] #2 bo
    b=s[n//2:] #2 ok
    vowels=set("aeiouAEIOU")
    v1=v2=0
    for c in a:
        if c in vowels:
            v1=v1+1
    for c in b:
        if c in vowels:
            v2=v2+1
    return 1 if v1==v2 else 0


# Example 1:(Fibinocci series==>>)
# Input:
#     3
# Output:
#     2
# Explanation:
#     F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 2:
# Input:
#     4
# Output:
#     3
# Explanation:
#     F(4) = F(3) + F(2) = 2 + 1 = 3.

def solve(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return(solve(n-1)+solve(n-2))
    return ans


# Example 1:
# Input : 4
# Output : 24

def solve(n):
    if n==0:
        return 1
    return n*solve(n-1) 
    return res
    return res

# Example 1:(Recursion===>>)
# Input:
#     3
#     4
# Output:
#     81
# Example 2:
# Input:
#     7
#     5
# Output:
#     16807
def solve(x,n):
    ans=1
    while n:
        ans=ans*x
        n-=1
    return ans

# Example 1
# Input: 22
# Output: 0
# Explanation: 22 is not power of 2.
# Example 2
# Input: n=1
# Output: 1
# Explanation: 2 to power 0 is 1
# Example 3
# Input: n= 64
# Output: 1
# Explanation: 2 to power 6 is 64

def solve(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2==1:
        return 0
    return solve(n//2)