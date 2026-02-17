"""
String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.
"""

days = int(input("Enter days till your birthday: "))

print(f"There are {int(days/7)} weeks and {days%7} days till your birthday")