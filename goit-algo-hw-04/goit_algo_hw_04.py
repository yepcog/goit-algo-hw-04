# task 1:
from task1_task2 import total_salary

total, average = total_salary("path/to/salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n")

total, average = total_salary("path/to/no_salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n")

with open("path/to/empty_salary.txt", "w"):
	pass
total, average = total_salary("path/to/empty_salary.txt")
print(f"Total salary: {total}, Average salary: {average}\n\n")


# task 2:
from task1_task2 import get_cats_info

cats_info = get_cats_info("path/to/cats.txt")
print(f"{cats_info}\n")

cats_info = get_cats_info("path/to/no_cats.txt")
print(f"{cats_info}\n")

with open("path/to/empty_cats.txt", "w"):
	pass
cats_info = get_cats_info("path/to/empty_cats.txt")
print(f"{cats_info}\n\n")


# task 3:

# task 3 test w/ current directory
#python goit-algo-hw-04\task3.py ".\goit-algo-hw-04"

# task 3 test w/ empty directory
#python goit-algo-hw-04\task3.py "C:\Visual Studio projects\repos-temp\new04"


# task 4:

# task 4 bot access
#python goit-algo-hw-04\task4.py