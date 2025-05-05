num = int(input("Enter any number: "))

original_num = num  # Storing the original number for comparison
rev = 0

while num > 0:  # Loop runs until num is greater than 0
    d = num % 10
    rev = (rev * 10) + d
    num = num // 10

if rev == original_num:
    print(f"{original_num} is a palindrome number.")
else:
    print(f"{original_num} is not a palindrome number.")
