# Number
numbers = [1,2,3]
numbers_list = [number + 1 for number in numbers]

# String
name = "arif"
letters_list = [letter for letter in name]

# Range
range_list = [number * 2 for number in range(1,5)]

# IF
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
conditional_list = [name.upper() for name in names if len(name) > 5]

print(f"Number List: {numbers_list}\n"
      f"Letters List: {letters_list}\n"
      f"Range List: {range_list}\n"
      f"Conditional List: {conditional_list}\n"
      )
