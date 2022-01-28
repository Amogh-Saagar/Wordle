import random
import colorama
from colorama import init
from colorama import Back
from colorama import Fore
from colorama import Style
#key = b'FLPPrNMKgUPEfK_7FVuwvv7apiKdX227-nsWN4PxkqE='
#reading the txt of all english words
text_file = open("en.txt", "r")
cache = text_file.read()
#cache = bytes(cache, 'utf-8')
#cache = str(cache.decode())
cache = cache.split()
data = [ ]
print("Enter the Number of letters you want the in the answer word and the words you enter")
num_of_letters = int(input())

#shortening it for only the words with lenth inputted
for i in cache:
	if len(i) == num_of_letters:
		data.append(i)


#reading file for basic english words
text_file1 = open("en-basic.txt", "r")
cache= text_file1.read()
cache = cache.split()
data1 = [ ]

for i in cache:
	if len(i) == num_of_letters:
		data1.append(i)
word = data1[random.randint(0, (len(data1)-1))]
del data1
i = 1
init()
while i <= 6:
	print("Enter a word")
	x = str(input())
	if x == word:
		print(Back.GREEN + word)
		print(Style.RESET_ALL, end = "")
		print(Fore.GREEN + "Correct word")
		break
	elif x in data:
		for n, j in enumerate(x):
			if j in word and x[n] == word[n]:
				print(Back.GREEN + j, end = "")
				print(Style.RESET_ALL, end = "")
			elif j in word:
				print(Back.YELLOW + j, end = "")
				print(Style.RESET_ALL, end = "")				
			else:
				print(j, end = "")
				print(Style.RESET_ALL, end = "")
		print()			

		i += 1
		
	else:
		print("Your word isn't 5 letters or is not an english word")
	print(f"attempts remaining are {7-i}")
	
if word != x and i == 7:
	print(Fore.RED +"You Lost!")
	print(Style.RESET_ALL, end = "")
	print(Fore.RED + f"The word was {word}")
	print(Style.RESET_ALL, end = "")
