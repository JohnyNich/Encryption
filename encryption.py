import random
import string
new_sentence = []
new_sentence_string = []
while_count = 0
lengths = []
counter1 = 0
while True:
	operation = input("Do you want to encrypt a message or decrypt one? Type exit to exit.")
	operation = operation.lower()
	if operation == "encrypt":
		sentence = input("Put in the word")
		sentence = sentence.lower()
		for letter in sentence:
			if letter == "a":
				new_sentence.append(1)
			elif letter == "b":
				new_sentence.append(2)
			elif letter == "c":
				new_sentence.append(3)
			elif letter == "d":
				new_sentence.append(4)
			elif letter == "e":
				new_sentence.append(5)
			elif letter == "f":
				new_sentence.append(6)
			elif letter == "g":
				new_sentence.append(7)
			elif letter == "h":
				new_sentence.append(8)
			elif letter == "i":
				new_sentence.append(9)
			elif letter == "j":
				new_sentence.append(10)
			elif letter == "k":
				new_sentence.append(11)
			elif letter == "l":
				new_sentence.append(12)
			elif letter == "m":
				new_sentence.append(13)
			elif letter == "n":
				new_sentence.append(14)
			elif letter == "o":
				new_sentence.append(15)
			elif letter == "p":
				new_sentence.append(14)
			elif letter == "q":
				new_sentence.append(15)
			elif letter == "r":
				new_sentence.append(14)
			elif letter == "s":
				new_sentence.append(15)
			elif letter == "t":
				new_sentence.append(16)
			elif letter == "u":
				new_sentence.append(17)
			elif letter == "v":
				new_sentence.append(18)
			elif letter == "w":
				new_sentence.append(19)
			elif letter == "x":
				new_sentence.append(20)
			elif letter == "y":
				new_sentence.append(21)
			elif letter == "z":
				new_sentence.append(22)
			elif letter == " ":
				new_sentence.append(0)
		length_of_sequence = len(new_sentence)
		for number in new_sentence:
			if number >= 10:
				lengths.append(2)
			else:
				lengths.append(1)
		num_of_letters = random.randint(int(len(sentence)/2), len(sentence)*2)
		while while_count != num_of_letters:
			new_sentence.insert(random.randint(0, len(new_sentence)), random.choice(string.ascii_letters).upper())
			while_count += 1
		for length in lengths:
			new_sentence.insert(counter1, length)
			counter1 += 2
		new_sentence.append(length_of_sequence)
		for number in new_sentence:
			new_sentence_string.append(str(number))
		new_sentence_string = "".join(new_sentence_string)
		print (new_sentence_string)
	elif operation == "decrypt":
		sequence = input("What is the code")
		lengths = [] # Redefining lengths in case it already contains something
		length_of_sequence = sequence[len(sequence) - 1]
		print (length_of_sequence)
		while_count = 0 # Redefining while_count in case it already contains something
		counter2 = 0
		list_sequence = []
		for thing in sequence:
			list_sequence.append(thing)
		while counter2 != int(length_of_sequence):
			lengths.append(list_sequence[while_count])
			del list_sequence[while_count]
			while_count += 2 # while_count is used to count which indexes to append
			counter2 += 1 # counter2 is used to count the numbers of lengths
		print (lengths)
		sentence_only_numbers = []
		for item in list_sequence:
			if item not in string.ascii_letters:
				sentence_only_numbers.append(item)
		print (sentence_only_numbers)
		counter3 = 0
		new_sentence = []
		for length in lengths:
			if length == "1":
				new_sentence.append(sentence_only_numbers[counter3])
				counter3 += 1
			else:
				new_sentence.append(sentence_only_numbers[counter3:counter3 +2])
				counter3 += 2
		print (new_sentence)
	elif operation == "exit":
		break
	else:
		print ("That's not a valid operation")
