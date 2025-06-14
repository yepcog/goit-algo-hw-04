import os, re

my_path = "path/to/salary.txt"
directory = os.path.dirname(my_path)
my_directory = os.makedirs(directory, exist_ok = True)
with open(my_path, "w") as file:
	file.write("Alex Korp,3000\n\
Nikita Borisenko,2000\n\
Sitarama Raju,1000")

#function will throw an error if: file not found, file is empty, salary values <= 0
#can distinguish text line w/ hyphen before number from negative number
#for example: Alex Korp - 3000 and Alex Korp -3000 (first line will be considered as valid)
def total_salary(path):
	error_message = f"Something went wrong, please verify the values in file '{path}'"
	error_result = ("error", "error")
	
	try:
		file_error = os.stat(path).st_size
		if file_error == 0:
			print(f"File or directory '{path}' is empty")
			return error_result
	except FileNotFoundError:
		print(f"No such file or directory: '{path}'")
		return error_result

	with open(path, "r") as file:
		file.seek(0)
		lines = file.readlines()

	total = 0
	i = 0

	for line in lines:
		try:
			pattern = re.compile(r"-?\d+")
			value = float(pattern.search(line).group(0))
			if value <= 0:
				print(error_message)
				return error_result
		except AttributeError:
			print(error_message)
			return error_result
		total += value
		i += 1

	average = total / i
	result = (total, average)

	return result