'''1.start = int(input("Start: "))  #prime numbers between range
end = int(input("End: "))

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)'''



'''2.a = int(input("Enter a: "))    #finding GCD
b = int(input("Enter b: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)'''

