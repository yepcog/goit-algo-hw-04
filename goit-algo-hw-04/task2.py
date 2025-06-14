import os

my_path = "path/to/cats.txt"

with open(my_path, "w") as file:
	file.write("60b90c1c13067a15887e1ae1,Tayson,3\n\
60b90c2413067a15887e1ae2,Vika,1\n\
60b90c2e13067a15887e1ae3,Barsik,2\n\
60b90c3b13067a15887e1ae4,Simon,12\n\
60b90c4613067a15887e1ae5,Tessi,5")

#function will throw an error if file not found or file is empty
def get_cats_info(path):
	error_result = [{"id": "error", "name": "error", "age": "error"}]
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

	result = []
	for line in lines:
		line = line.strip().split(",")
		line = {"id": line[0], "name": line[1], "age": line[2]}
		result.append(line)

	return result