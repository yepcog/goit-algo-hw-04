# task 1:
from task1 import total_salary

total, average = total_salary("path/to/salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n")

total, average = total_salary("path/to/no_salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n")

with open("path/to/empty_salary.txt", "w"):
	pass
total, average = total_salary("path/to/empty_salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n\n")


# task 2:
from task2 import get_cats_info

cats_info = get_cats_info("path/to/cats.txt")
print(f"{cats_info}\n")

cats_info = get_cats_info("path/to/no_cats.txt")
print(f"{cats_info}\n")

with open("path/to/empty_cats.txt", "w"):
	pass
cats_info = get_cats_info("path/to/empty_cats.txt")
print(f"{cats_info}\n\n")


# task 3:
from taskOptional import tree_visualizer
#import taskOptional

#for colorfull visualization of the directory tree run commands listed below in your developer PowerShell/Command Prompt
#Set-ExecutionPolicy Unrestricted -Scope Process
#python -m venv .venv
#.\.venv\Scripts\Activate.ps1
#pip install colorama

# task 3 (as a function call)
tree_visualizer("C:\\Visual Studio projects\\python\\goit-algo-hw-04\\goit-algo-hw-04") #tree_visualizer(".")

tree_visualizer("C:\\Visual Studio projects\\python\\goit-algo-hw-04\\no_goit-algo-hw-04")

tree_visualizer("C:\\Visual Studio projects\\python\\goit-algo-hw-04\\empty_goit-algo-hw-04")

#prototype, I'll move it in the final ver
#def main():
	#from taskOptional import tree_visualizer
	#tree_visualizer(".")

# task 4:
