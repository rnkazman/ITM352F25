# Create  a list of all odd numbers from 1 to 50 (inclusive)
# Name: Rick Kazman
# Date: 9/30/2025

nums = []
for number in range(1,51):
    if number % 2 == 1:
        nums.append(number)
print(nums)