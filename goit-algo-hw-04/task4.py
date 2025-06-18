import sys

def parse_input(user_input) -> tuple:
	command, *args = user_input.split()
	command = command.strip().casefold()
	return command, *args

def arg_sep(args) -> tuple:
	alpha_args = []
	for arg in args:
		if arg.isalpha():
			alpha_args.append(arg)
		else:
			phone = arg
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
	name, phone = arg_sep(args)
	if name in contacts:
		return "Contact is already registered"
	for key, value in contacts.items():
		if value == phone:
			return "This phone number is already associated with another contact"
	contacts[name] = phone
	return "Contact added."

def show_phone(args, contacts) -> str:
	name = " ".join(args)
	for char in name:
		if char.isdigit():
			return invalid_args
	if name not in contacts and name.strip() != "":
		return "Contact is not on the list"
	elif name.strip() == "":
		return invalid_args
	return contacts.get(name)

def change_contact(args, contacts) -> str:
	name, phone = arg_sep(args)
	if name not in contacts:
		return "Contact is not on the list"
	elif contacts[name] == phone:
		return "This phone number is already associated with corresponding contact"
	for key, value in contacts.items():
		if value == phone:
			return "This phone number is already associated with another contact"
	contacts[name] = phone
	return "Phone number changed."

def modify_contact(new_name, contacts, old_name) -> str:
	# requires A LOT of rethinking
	if new_name in contacts:
		return "Contact with this name is already registered"
	try:
		phone = contacts.pop(old_name)
	except KeyError:
		return "Contact is not on the list"
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
		return "Contact is not on the list"
	return "Contact deleted."

def main():
	contacts = {}
	print("Welcome to the assistant bot!")
	while True:
		user_input = input("Enter a command: ")
		command, *args = parse_input(user_input)

		match command:
			case "hello":
				print(f"How can I help you?\n\
In order to view all available commands you can use 'help' command \
or 'help command' pattern to get information on a specific command")
			case "exit":
				print("Bye!")
				sys.exit(0)
			case "help":
				if args == []:
					print(available_commands)
				elif args != []:
					help_command = args[0].casefold()
					if help_command in available_commands:
						print(f"'{help_command}': '{available_commands.get(help_command)}'")
					else: 
						print(invalid_command)
			case "all":
				if args != []:
					print(invalid_args)
				else:
					print(contacts)
			case "add":
				try:
					print(add_contact(args, contacts))
				except UnboundLocalError:
					print(invalid_args)
			case "phone":
				print(show_phone(args, contacts))
			case "change":
				try:
					print(change_contact(args, contacts))
				except UnboundLocalError:
					print(invalid_args)
			case "modify":
				# too complicated, but it does the thing
				old_name = " ".join(args)

				old_isdigit = False
				for char in old_name:
					if char.isdigit():
						old_isdigit = True
						print(invalid_args)
						break
				if old_name.strip() == "":
					print(invalid_args)
				elif old_name not in contacts and old_isdigit == False:
					print("Contact is not on the list")
				elif old_name in contacts:
					# adding a loop there might be usefull
					new_name = input("Enter a new Name: ")
					new_isdigit = False
					for char in new_name:
						if char.isdigit():
							new_isdigit = True
							print(invalid_args)
							break
					try:
						new_command, *args = new_name.split()
						if new_command in available_commands:
							print(invalid_args)
						elif new_isdigit == False:
							print(modify_contact(new_name, contacts, old_name))
					except ValueError:
						print("Arguments don't match a command pattern.\n\
To modify a contact's Name, a new Name must be provided")
			case "delete":
				print(delete_contact(args, contacts))
			case _:
				print(invalid_command)

if __name__ == "__main__":
	main()