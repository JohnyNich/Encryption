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
		user_sentence = input("Put in the word")
		user_sentence = user_sentence.lower()
		for letter in user_sentence:
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
				new_sentence.append(16)
			elif letter == "q":
				new_sentence.append(17)
			elif letter == "r":
				new_sentence.append(18)
			elif letter == "s":
				new_sentence.append(19)
			elif letter == "t":
				new_sentence.append(20)
			elif letter == "u":
				new_sentence.append(21)
			elif letter == "v":
				new_sentence.append(22)
			elif letter == "w":
				new_sentence.append(23)
			elif letter == "x":
				new_sentence.append(24)
			elif letter == "y":
				new_sentence.append(25)
			elif letter == "z":
				new_sentence.append(26)
			elif letter == " ":
				new_sentence.append(0)
		length_of_sequence = len(new_sentence)
		print ("The raw sequence" + str(new_sentence))
		for number in new_sentence:
			if number >= 10:
				lengths.append(2)
			else:
				lengths.append(1)
		print ("The lengths are " + str(lengths))
		num_of_letters = random.randint(int(len(user_sentence)/2), len(user_sentence)*2)
		while while_count != num_of_letters:
			new_sentence.insert(random.randint(0, len(new_sentence)), random.choice(string.ascii_letters).upper())
			while_count += 1
		print ("The sequence with the letters are " + str(new_sentence))
		for length in lengths:
			new_sentence.insert(counter1, length)
			counter1 += 2
		print ("The sequence with lengths are " + str(new_sentence))
		new_sentence.append(length_of_sequence)
		for number in new_sentence:
			new_sentence_string.append(str(number))
		new_sentence_string = "".join(new_sentence_string)
		print ("The final sequence is " + str(new_sentence_string))
		print (lengths)
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
		while counter2 != int(length_of_sequence): # This while loop appends the lengths
			lengths.append(list_sequence[while_count])
			while_count += 2 # while_count is used to count which indexes to append
			counter2 += 1 # counter2 is used to count the numbers of lengths
		print ("The sequence is  " + str(list_sequence))
		print ("Lengths are " + str(lengths))
		counter2 = 0
		while_count = 0
		print (list_sequence[4])
		print (list_sequence[6])
		while counter2 != int(length_of_sequence): # This while loop is an almost exact copy of the above, except instead of appending lengths to a list, it's deleting the lengths from the sequence
			print ("This is turn number " + str(counter2) + ". It will delete what is at index " + str(while_count) + ", which is " + list_sequence[while_count])
			del list_sequence[while_count]
			while_count += 1 # while_count is used to count which indexes to append
			counter2 += 1 # counter2 is used to count the numbers of lengths
		print ("Without lengths is " + str(list_sequence))
		sentence_only_numbers = []
		for item in list_sequence:
			if item not in string.ascii_letters:
				sentence_only_numbers.append(item)
		print ("The sequence with only numbers is " + str(sentence_only_numbers))
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
		print (new_sentence)
		listed_new_sentence = []
		sentence = []
		for number in new_sentence:
			if number == "1":
				sentence.append("a")
			elif number == "2":
				sentence.append("b")
			elif number == "3":
				sentence.append("c")
			elif number == "4":
				sentence.append("d")
			elif number == "5":
				sentence.append("e")
			elif number == "6":
				sentence.append("f")
			elif number == "7":
				sentence.append("g")
			elif number == "8":
				sentence.append("h")
			elif number == "9":
				sentence.append("i")
			elif number == "10":
				sentence.append("j")
			elif number == "11":
				sentence.append("k")
			elif number == "12":
				sentence.append("l")
			elif number == "13":
				setnence.append("m")
			elif number == "14":
				sentence.append("n")
			elif number == "15":
				sentence.append("o")
			elif number == "16":
				sentence.append("p")
			elif number == "17":
				sentence.append("q")
			elif number == "18":
				sentence.append("r")
			elif number == "19":
				sentence.append("s")
			elif number == "20":
				sentence.append("t")
			elif number == "21":
				sentence.append("u")
			elif number == "22":
				sentence.append("v")
			elif number == "23":
				sentence.append("w")
			elif number == "24":
				sentnece.append("x")
			elif number == "25":
				sentence.append("y")
			elif number == "26":
				sentence.append("z")
			elif number == "0":
				sentence.append(" ")
		print (sentence)
	elif operation == "exit":
		break
	else:
		print ("That's not a valid operation")
