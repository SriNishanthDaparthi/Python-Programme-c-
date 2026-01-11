'''1.n = int(input("Enter n: ")) #even and odd number printing upto n numbers
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Even sum:", even_sum)
print("Odd sum:", odd_sum)'''


'''2.num = int(input("Enter number: ")) #finding of palindrome number
temp = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
if rev == temp:
    print("Palindrome")
else:
    print("Not a palindrome")'''


'''3.num = int(input("Enter number: ")) #factors of number

for i in range(1, num + 1):
    if num % i == 0:
        print(i)'''


