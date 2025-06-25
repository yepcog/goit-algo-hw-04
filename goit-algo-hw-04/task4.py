import sys

def parse_input(user_input) -> tuple:
	command, *args = user_input.split()
	command = command.strip().casefold()
	return command, *args

def arg_sep(args) -> tuple:
	alpha_args = []
	phone = ""
	for arg in args:
		if phone != "" and arg.isalpha():
			return invalid_args
		elif arg.isalpha():
			alpha_args.append(arg)
		# temporary solution
		elif arg.isdigit():
			phone += arg
		else:
			return "Inappropriate contact Name or phone number."
	if phone == "":
		return invalid_args
	name = " ".join(alpha_args)
	return name, phone

# maybe returning a list of all commands (w/out description) will be better than returning the whole dictionary
available_commands = {
						"hello": "simple greeting command, \
gives advice on how to use 'help' command and why you should consider using it",
						"exit": "to exit bot assistant and close the program",
						"help": "provides a list of all available commands \
or information on a specific command by using pattern 'help command'",
						"all": "provides a list of all saved contacts",
						"add": "to add new contact to the list of contacts, \
command should match 'add Name phone' pattern",
						"phone": "provides a phone number of a specific contact, \
command should match 'phone Name' pattern",
						"change": "to change a phone number for an existing contact, \
command should match 'change Name phone' pattern",
						"modify": "to modify a Name of an existing contact, \
command should match 'modify Name' pattern",
						"delete": "to permanently delete a contact from the list of contacts, \
command should match 'delete Name' pattern"
}

invalid_command = "Invalid command.\n\
You can use 'help' command or 'help command' pattern to verify argument requirements for corresponding command"

# raw temporary solution
invalid_args = "Arguments don't match a command pattern.\n\
You can use 'help' command or 'help command' pattern to verify argument requirements for corresponding command"

def add_contact(args, contacts) -> str:
	try:
		name, phone = arg_sep(args)
		if name in contacts:
			return "Contact is already registered."
		for key, value in contacts.items():
			if value == phone:
				return "This phone number is already associated with another contact."
		contacts[name] = phone
		return "Contact added."
	except ValueError:
		return arg_sep(args)
	except TypeError:
		return invalid_args

def show_phone(args, contacts) -> str:
	name = " ".join(args)
	for char in name:
		if char.isdigit():
			return invalid_args
	if name not in contacts and name.strip() != "":
		return "Contact is not on the list."
	elif name.strip() == "":
		return invalid_args
	return contacts.get(name)

def change_contact(args, contacts) -> str:
	try:
		name, phone = arg_sep(args)
		if name not in contacts:
			return "Contact is not on the list."
		elif contacts[name] == phone:
			return "This phone number is already associated with corresponding contact."
		for key, value in contacts.items():
			if value == phone:
				return "This phone number is already associated with another contact."
		contacts[name] = phone
		return "Phone number changed."
	except ValueError:
		return arg_sep(args)
	except TypeError:
		return invalid_args

def modify_contact(old_name, new_name, contacts) -> str:
	# requires A LOT of rethinking
	if new_name in contacts:
		return "Contact with this name is already registered."
	try:
		phone = contacts.pop(old_name)
	except KeyError:
		return "Contact is not on the list."
	contacts[new_name] = phone
	return "Contact modified."

def delete_contact(args, contacts) -> str:
	name = " ".join(args)
	for char in name:
		if char.isdigit():
			return invalid_command
	if name.strip() == "":
		return invalid_args
	try:
		del contacts[name]
	except KeyError:
		return "Contact is not on the list."
	return "Contact deleted."

# temp handlers

hello_str = "How can I help you?\n\
In order to view all available commands you can use 'help' command \
or 'help command' pattern to get information on a specific command"

def no_args(command, args, other=None) -> str | list:
	if args != []:
		if command == "help":
			help_command = args[0].casefold()
			if args.__len__() > 1:
				return invalid_command
			elif help_command in other:
				return f"'{help_command}': '{other.get(help_command)}'"
			else: 
				return invalid_command
		elif command == "add":
			return add_contact(args, other)
		elif command == "change":
			return change_contact(args, other)
		elif command == "modify":
			return prep_modify(args, other)
			#try:
				#old_name, new_name = prep_modify(args, other)
				#return modify_contact(old_name, new_name, other)
			#except ValueError:
				#return prep_modify(args, other)
			#except TypeError:
				#return prep_modify(args, other)
		else:
			return invalid_command
	elif args == []:
		if command == "hello":
			return other
		elif command == "exit":
			print("Bye!")
			return sys.exit(0)
		elif command == "help":
			return list(other.keys())
		elif command == "all":
			return other
		elif command == "add":
			return invalid_args
		elif command == "change":
			return invalid_args
		elif command == "modify":
			return invalid_args

def prep_modify(args, contacts) -> str:
		old_name = " ".join(args)
		old_isdigit = False
		for char in old_name:
			if char.isdigit():
				old_isdigit = True
				return invalid_args
		if old_name.strip() == "":
			return invalid_args
		elif old_name not in contacts and old_isdigit == False:
			return "Contact is not on the list."
		elif old_name in contacts:
			while True:
				new_name = input("Enter a new Name: ")
				new_isdigit = False
				for char in new_name:
					if char.isdigit():
						new_isdigit = True
						print("Inappropriate contact Name.")
						break
				try:
					new_command, *args = new_name.split()
					if new_name.strip() == "exit" or new_command == "exit" and args == []:
						return "Contact modification cancelled."
					elif new_command in available_commands and new_isdigit == False:
						print("Inappropriate contact Name.\n\
You can use 'exit' command to cancel contact modification")
					elif new_isdigit == False:
						#return old_name, new_name
						return modify_contact(old_name, new_name, contacts)
				except ValueError:
					print("To modify a contact's Name, a new Name must be provided.\n\
You can use 'exit' command to cancel contact modification")
					continue

def main():
	contacts = {}
	print("Welcome to the assistant bot!")
	while True:
		user_input = input("Enter a command: ")
		command, *args = parse_input(user_input)

		match command:
			case "hello":
				# changed
				print(no_args(command, args, hello_str))
			case "exit":
				# changed
				print(no_args(command, args))
			case "help":
				# changed
				print(no_args(command, args, available_commands))
			case "all":
				# changed
				print(no_args(command, args, contacts))
			case "add":
				# changed
				print(no_args(command, args, contacts))
			case "phone":
				print(show_phone(args, contacts))
			case "change":
				# changed
				print(no_args(command, args, contacts))
			case "modify":
				# changed
				print(no_args(command, args, contacts))
			case "delete":
				print(delete_contact(args, contacts))
			case _:
				print(invalid_command)

if __name__ == "__main__":
	main()