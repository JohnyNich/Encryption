import random
import string
import sys
import time
import linecache
import datetime
def word_by_word(sentence):
	for letter in sentence:
		print(letter, end="")
		sys.stdout.flush()
		time.sleep(0.1)
	print ("")
def config_error(line):
	word_by_word("Error, can't find True or False at line " + str(line) + " of config.txt.")
	word_by_word("Shutting down")
	sys.exit()
def get_config_line(line):
	return linecache.getline("config.txt", line).strip()
write = False
start = True
has_read_sequence = False
characters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", "<", ".", ">", "/", "?", ";", ":","'", "\"", "\\", "|", "]", "}", "[", "{", "1", "!", "2", "@", "3", "#", "4", "$", "5", "%", "6", "^", "7", "&", "8", "*", "9", "(", "0", ")", "-", "_", "+", "+", "`", "~", "A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
animation = get_config_line(2)
animation = animation.lower()
if animation == "true":
	animation = True
elif animation == "false":
	animation = False
else:
	config_error(2)
def cout(text): # cout (Console out) prints to console and will automatically animate the text if animation is ture. That's why I put it here.
	if animation == True:
		word_by_word(text)
	else:
		print(text)
additional_write_text = get_config_line(4)
additional_write_text = additional_write_text.lower()
if additional_write_text == "true":
	additional_write_text = True
elif additional_write_text == "false":
	additional_write_text = False
else:
	config_error(4)
write = get_config_line(6)
write = write.lower()
if write == "true": # For auto-write config option
	write = True
elif write == "false":
	write = False
else:
	config_error(6)
debugging = get_config_line(8)
debugging = debugging.lower()
if debugging == "true":
	debugging = True
elif debugging == "false":
	debugging = False
else:
	config_error(8)
datetime_stamp = get_config_line(10)
datetime_stamp = datetime_stamp.lower()
if datetime_stamp == "true":
	datetime_stamp = True
elif datetime_stamp == "false":
	datetime_stamp = False
else:
	config_error(10)
session_read = open("session.txt", "r")
session = session_read.read()
session = int(session)
session_read.close()
session += 1
session_read = open("session.txt", "w")
session_read.write(str(session))
session_read.close()
while True:
	new_sentence = []
	new_sentence_string = []
	while_count = 0
	lengths = []
	counter1 = 0
	if start == True:
		cout("Do you want to encrypt a message or decrypt one? Type exit to exit. If you want to write the sequence onto a file. Type write. If you want to read a file, just type read.")
		start = False
	if has_read_sequence == False:
		if animation == True:
			word_by_word("What do you want to do?")
			operation = input()
		else:
			operation = input("What do you want to do?")
		operation = operation.lower()
	else:
			operation = "decrypt"
	if operation == "encrypt":
		if animation == True:
			word_by_word("Put in the word")
			user_sentence = input()
		else:
			user_sentence = input("Put in a word")
		if datetime_stamp == True:
			today = datetime.datetime.today()
			date = []
			date.append(str(today.day))
			date.append(str(today.month))
			date.append(str(today.year))
			date.append(str(today.hour))
			if today.minute < 10:
				date.append("0" + str(today.minute) + "-") # I've added this dash so that the program will now when to stop appending dates
			else:
				date.append(str(today.minute) + "-") # I've added this dash so that the program will now when to stop appending dates
			date = "-".join(date)
			print (date)
			for number in date:
				new_sentence.append(characters.index(number))
		for letter in user_sentence:
			new_sentence.append(characters.index(letter))
		length_of_sequence = len(new_sentence)
		single_numbered_list = []
		for number in new_sentence:
			if number >= 10:
				lengths.append(2)
				single_numbered_list.append(str(number)[0])
				single_numbered_list.append(str(number)[1])
			else:
				lengths.append(1)
				single_numbered_list.append(str(number))
		new_sentence = single_numbered_list
		num_of_letters = random.randint(int(len(user_sentence)/2), len(user_sentence)*2)
		#~ print ("The lengths are " + str(lengths))
		while while_count != num_of_letters:
			new_sentence.insert(random.randint(0, len(new_sentence)), random.choice(string.ascii_letters).upper())
			while_count += 1
		#~ print ("The sequence with the letters are " + str(new_sentence))
		for length in lengths:
			new_sentence.insert(counter1, length)
			counter1 += 2
		#~ print ("The sequence with lengths are " + str(new_sentence))
		new_sentence.append(random.choice(string.ascii_letters.upper()))
		new_sentence.append(length_of_sequence)
		if datetime_stamp == True:
			new_sentence.insert(0, "T")
		for number in new_sentence:
			new_sentence_string.append(str(number))
		new_sentence_string = "".join(new_sentence_string)
		cout("The sequence is " + str(new_sentence_string))
		test = new_sentence_string
		write_to = "write" + str(session) + ".txt"
		if write == True:
			file_write = open(write_to, "a")
			if additional_write_text == True:
				file_write.write(user_sentence + ": " + new_sentence_string + "\n")
			else:
				file_write.write(new_sentence_string + "\n")
			cout("Writing complete")
			cout("The sequence has been written to " + write_to)
			file_write.close()
	elif operation == "decrypt":
		if debugging != True and  has_read_sequence == False:
			if animation == True:
				word_by_word("What is the code")
				sequence = input()
			else:
				sequence = input("What is the code")
		elif has_read_sequence == True:
			has_read_sequence = False
		else:
			sequence = test
		if sequence[0] == "T":
			has_datetime_stamp = True
			sequence = list(sequence)
			sequence.remove("T")
			sequence = "".join(sequence)
		else:
			has_datetime_stamp = False
		lengths = [] # Redefining lengths in case it already contains something
		length_of_sequence = []
		for thing in sequence[::-1]:
			if thing in string.ascii_letters.upper():
				break
			else:
				length_of_sequence.append(thing)
		length_of_sequence = length_of_sequence[::-1]
		length_of_sequence = "".join(length_of_sequence)
		#~ print (length_of_sequence)
		while_count = 0 # Redefining while_count in case it already contains something
		counter2 = 0
		list_sequence = []
		for thing in sequence:
			list_sequence.append(thing)
		while counter2 != int(length_of_sequence): # This while loop appends the lengths
			lengths.append(list_sequence[while_count])
			while_count += 2 # while_count is used to count which indexes to append
			counter2 += 1 # counter2 is used to count the numbers of lengths
		counter2 = 0
		while_count = 0
		while counter2 != int(length_of_sequence): # This while loop is an almost exact copy of the above, except instead of appending lengths to a list, it's deleting the lengths from the sequence
			del list_sequence[while_count]
			while_count += 1 # while_count is used to count which indexes to append
			counter2 += 1 # counter2 is used to count the numbers of lengths
		sentence_only_numbers = []
		for item in list_sequence:
			if item not in string.ascii_letters:
				sentence_only_numbers.append(item)
		counter3 = 0
		new_sentence = []
		for length in lengths:
			if length == "1":
				number = sentence_only_numbers[counter3]
				new_sentence.append(number)
				counter3 += 1
			else:
				number = sentence_only_numbers[counter3:counter3 +2]
				number = "".join(number)
				new_sentence.append(number)
				counter3 += 2
		listed_new_sentence = []
		sentence = []
		for number in new_sentence:
			sentence.append(characters[int(number)])
		if datetime_stamp == True:
			counter4 = 0
			day = []
			for character in sentence:
				if character == "-":
					counter4 += 1
					break
				else:
					day.append(character)
				counter4 += 1
			sentence = sentence[counter4:]
			counter4 = 0
			day = "".join(day)
			month = []
			for character in sentence:
				if character == "-":
					counter4 += 1
					break
				else:
					month.append(character)
				counter4 += 1
			sentence = sentence[counter4:]
			counter4 = 0
			month = "".join(month)
			year = []
			for character in sentence:
				if character == "-":
					counter4 += 1
					break
				else:
					year.append(character)
				counter4 += 1
			sentence = sentence[counter4:]
			counter4 = 0
			year = "".join(year)
			hour = []
			for character in sentence:
				if character == "-":
					counter4 += 1
					break
				else:
					hour.append(character)
				counter4 += 1
			sentence = sentence[counter4:]
			counter4 = 0
			hour = "".join(hour)
			minute = []
			for character in sentence:
				if character == "-":
					counter4 += 1
					break
				else:
					minute.append(character)
				counter4 += 1
			minute = "".join(minute)
			sentence = sentence[counter4:]
			months = {1 : "January", 2 : "Feburary", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}
			endings = {1 : "st", 2 : "nd", 3 : "rd", 4 : "th", 5 : "th", 6 : "th", 7 : "th", 8 : "th", 9 : "th", 0 : "th"}
			if len(day) == 2:
				cout("This message was encrypted on " + day + endings[int(day[:0:-1])] + " of " + months[int(month)] + " of " + year + " at " + hour + ":" + minute)
			else:
				cout("This message was encrypted on " + day + endings[int(day)] + " of " + months[int(month)] + " of " + year + " at " + hour + ":" + minute)
		sentence = "".join(sentence)
		cout("The sentence is " +  sentence)
	elif operation == "exit":
		break
	elif operation == "debugging mode":
		if debugging == False:
			cout("Debugging mode enabled")
			debugging = True
		else:
			cout("Debugging mode disabled")
			debugging = True
	elif operation == "write":
		if write == False:	
			write = True
			cout("Writing enabled")
		else:
			write = False
			cout("Writing disabled")
	elif operation == "read":
		if animation == True:
			word_by_word("To read a file, make sure it is inside the folder in which this file is located. Then, just enter the line in which the sequence is.")
			word_by_word("Enter the name of the file. Make sure to add the ending (eg .txt)")
			read_file = input("")
			word_by_word("What line is it?")
			read_line = input("")
		else:
			print("To read a file, make sure it is inside the folder in which this file is located. Then, just enter the line in which the sequence is.")
			read_file = input("Enter the name of the file. Make sure to add the ending (eg .txt) \n")
			read_line = input("What line is it? \n")
		read_sequence = linecache.getline(read_file, int(read_line))
		sequence = read_sequence
		has_read_sequence = True
	else:
		cout("That's not a valid operation")
