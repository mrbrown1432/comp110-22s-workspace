"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730481331"

user_name: str = input("Enter a 5-Character Word:")
if len(user_name) != 5:
    print("Error: Word must contain 5 characters")
    exit()

user_name1: str = input("Enter a single character:")
if len(user_name1) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_name1 + " in " + user_name)

instance_count: int = 0

if user_name1 == user_name[0]:
    print(user_name1 + " found at index 0")
    instance_count += 1
if user_name1 == user_name[1]:
    print(user_name1 + " found at index 1")
    instance_count += 1
if user_name1 == user_name[2]:
    print(user_name1 + " found at index 2")
    instance_count += 1
if user_name1 == user_name[3]:
    print(user_name1 + " found at index 3")
    instance_count += 1
if user_name1 == user_name[4]:
    print(user_name1 + " found at index 4")
    instance_count += 1

if instance_count == 0:
    print("No instances of " + user_name1 + " found in " + user_name)
else:
    if instance_count == 1:
        print(str(instance_count) + " instance of " + user_name1 + " found in " + user_name)
    else:
        print(str(instance_count) + " instances of " + user_name1 + " found in " + user_name)