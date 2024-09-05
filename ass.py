input_str = input("Enter a list of integers separated by spaces: ")
split_input = input_str.split()
result_str = ""
for item in split_input:
    result_str += "'" + str(int(item)) + "'"

result_str = result_str.strip()
print(f"Converted list: {result_str}")
