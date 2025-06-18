import re
from pathlib import Path

my_directory = Path("path/to")
my_directory.mkdir(parents=True, exist_ok=True)

# task 1:
with open("path/to/salary.txt", "w") as file:
	file.write("Alex Korp,3000\n\
Nikita Borisenko,2000\n\
Sitarama Raju,1000")

#function will throw an error if: file not found, file is empty, salary values <= 0
#can distinguish text line w/ hyphen before number from negative number
#for example: Alex Korp - 3000 and Alex Korp -3000 (first line will be considered as valid)
def total_salary(path: Path) -> tuple:
	error_message = f"Something went wrong, please verify the values in file '{path}'"
	error_result = ("error", "error")
	
	try:
		file_error = Path(path).stat().st_size
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


# task 2:
with open("path/to/cats.txt", "w") as file:
	file.write("60b90c1c13067a15887e1ae1,Tayson,3\n\
60b90c2413067a15887e1ae2,Vika,1\n\
60b90c2e13067a15887e1ae3,Barsik,2\n\
60b90c3b13067a15887e1ae4,Simon,12\n\
60b90c4613067a15887e1ae5,Tessi,5")

#function will throw an error if file not found or file is empty
def get_cats_info(path: Path) -> list:
	error_result = [{"id": "error", "name": "error", "age": "error"}]
	try:
		file_error = Path(path).stat().st_size
		if file_error == 0:
			print(f"File or directory '{path}' is empty")
			return error_result
	except FileNotFoundError:
		print(f"No such file or directory: '{path}'")
		return error_result

	with open(path, "r") as file:
		file.seek(0)
		lines = file.readlines()

	result = []
	for line in lines:
		line = line.strip().split(",")
		line = {"id": line[0], "name": line[1], "age": line[2]}
		result.append(line)

	return result