import random
sentence = input("Put in the word")
sentnece = sentence.lower()
new_sentence = []
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
		new_sentence.append(0
num_of_letters = random.randint((len(sentence)/2), (len(sentence)*2))
print (new_sentence)
		
