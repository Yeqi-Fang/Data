fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

count = 0

while count < 5:
    print(count)
    count += 1


age = 18

if age < 18:
    print("你未成年。")
elif age >= 18 and age < 21:
    print("你已成年，但不允许饮酒。")
else:
    print("你可以合法地饮酒。")
