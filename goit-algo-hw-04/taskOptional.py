import os, sys
#from colorama import Style, init, Fore

my_directory = os.makedirs("C:\\Visual Studio projects\\python\\goit-algo-hw-04\\empty_goit-algo-hw-04", exist_ok = True)

def tree_visualizer(path):
	error_result = "error"
	
	try:
		file_error = os.stat(path).st_size
		if file_error == 0:
			print(f"File or directory '{path}' is empty")
			return error_result
	except FileNotFoundError:
		print(f"No such file or directory: '{path}'")
		return error_result

	walk_tuple = os.walk(path)
	space = "    "
	for dirpath, dirnames, filenames in walk_tuple:
		position = dirpath.replace(path, "").count(os.sep)

		dirname = os.path.basename(dirpath)
		print(f"{space * position}{dirname}")

		for filename in filenames:
			print(f"{space * (position + 1)}{filename}")


if len(sys.argv) > 1:
		last_input = sys.argv[len.sys.argv - 1]
		print(f"invoking task3 function for a {last_input} path")
		tree_visualizer(last_input)

	
#tO = os.path.abspath("taskoptional.py")	
#print(f"{tO}")
	

#def tree_visualizer(path):
	#walk_tuple = os.walk(path)
	#space = "    "
	#for dirpath, dirnames, filenames in walk_tuple:
		#position = dirpath.replace(path, "").count(os.sep)

		#dirname = os.path.basename(dirpath)
		#print(+ f"{space * position}{dirname}")

		#for filename in filenames:
			#print(f"{space * (position + 1)}{filename}")

#Set-ExecutionPolicy Unrestricted -Scope Process
#python -m venv .venv
#.\.venv\Scripts\Activate.ps1
#pip install colorama