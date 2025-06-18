import os, sys

#Set-ExecutionPolicy Unrestricted -Scope Process
#python -m venv .venv
#.\.venv\Scripts\Activate.ps1
#pip install colorama

def tree_visualizer(path) -> str:
	walk_tuple = os.walk(path)
	space = "    "
	for dirpath, dirnames, filenames in walk_tuple:
		position = dirpath.replace(path, "").count(os.sep)

		dirname = os.path.basename(dirpath)
		print(f"{Fore.LIGHTMAGENTA_EX}{space * position}{dirname}{Style.RESET_ALL}")

		for filename in filenames:
			print(f"{Fore.YELLOW}{space * (position + 1)}{filename}{Style.RESET_ALL}")

def main():
	if sys.argv.__len__() > 1:
		last_argv = sys.argv[sys.argv.__len__() - 1]
		try:
			size_check = os.path.getsize(last_argv)
			if size_check == 0:
				print(f"File or directory '{last_argv}' is empty")
			else:
				tree_visualizer(last_argv)
		except FileNotFoundError:
			print(f"No such file or directory: '{last_argv}'")

		#tree_visualizer(last_argv)

if __name__ == "__main__":
	from colorama import Fore, Style
	main()