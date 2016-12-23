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
datetime_stamp = date-time_stamp.lower()
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
		if animation == True:
			word_by_word("Do you want to encrypt a message or decrypt one? Type exit to exit. If you want to write the sequence onto a file. Type write. If you want to read a file, just type read.")
		else:
			print("Do you want to encrypt a message or decrypt one? Type exit to exit. If you want to write the sequence onto a file. Type write. If you want to read a file, just type read.")
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
		for letter in user_sentence:
			new_sentence.append(characters.index(letter))
		length_of_sequence = len(new_sentence)
		#~ print ("The raw sequence" + str(new_sentence))
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
		for number in new_sentence:
			new_sentence_string.append(str(number))
		new_sentence_string = "".join(new_sentence_string)
		if animation == True:
			word_by_word("The sequence is " + str(new_sentence_string))
		else:
			print("The sequence is " + str(new_sentence_string))
		test = new_sentence_string
		write_to = "write" + str(session) + ".txt"
		if write == True:
			file_write = open(write_to, "a")
			if additional_write_text == True:
				file_write.write(user_sentence + ": " + new_sentence_string + "\n")
			else:
				file_write.write(new_sentence_string + "\n")
			if animation == True:
				word_by_word("Writing complete")
				word_by_word("The sequence has been written to " + write_to)
			else:
				print("Writing complete")
				print("The sequence has been written to " + write_to)
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
		#~ print(new_sentence)
		listed_new_sentence = []
		sentence = []
		for number in new_sentence:
			sentence.append(characters[int(number)])
		sentence = "".join(sentence)
		if animation == True:
			word_by_word("The sentence is " +  sentence)
		else:
			print("The sentence is " +  sentence)
	elif operation == "exit":
		break
	elif operation == "debugging mode":
		if debugging == False:
			if animation == True:
				word_by_word("Debugging mode enabled")
			else:
				print("Debugging mode enabled")
			debugging = True
		else:
			if animation == True:
				word_by_word("Debugging mode disabled")
			else:
				print("Debugging mode disabled")
			debugging = True
	elif operation == "write":
		if write == False:	
			write = True
			if animation == True:
				word_by_word("Writing enabled")
			else:
				print("Writing enabled")
		else:
			write = False
			if animation == True:
				word_by_word("Writing disabled")
			else:
				print("Writing disabled")
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
		if animation == True:
			word_by_word("That's not a valid operation")
		else:
			print("That's not a valid operation")
