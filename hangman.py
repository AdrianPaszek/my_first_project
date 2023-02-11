
import random
pic1 = [' ',
    '''
||=========
||    |    
||         
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||         
||         
||         
||         ''',
'''
||=========
||    |    
||    0    
||    |    
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|    
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||   /     
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||   / \   
||         
||          ''',
]

pic2 = [' ',
'''
||=========
||    |    
||    0    
||         
||         
||         
||         ''',
'''
||=========
||    |    
||    0    
||    |    
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||   /     
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||   / \   
||         
||          ''',
]

pic3 = [' ',
'''
||=========
||    |    
||    0    
||         
||         
||         
||         ''',
'''
||=========
||    |    
||    0    
||   /|\   
||         
||         
||          ''',
'''
||=========
||    |    
||    0    
||   /|\   
||   / \   
||         
||          ''',
]
with open("latwy.txt", "r") as f:
    word = f.readlines()
word = random.choice(word) [:-1]

with open("sredni.txt", "r") as f:
    word = f.readlines()
word = random.choice(word) [:-1]

with open("trudny.txt", "r") as f:
    word = f.readlines()
word = random.choice(word) [:-1]

print("")
print("Witaj w świecie gier i zabawy.")
print("Mam nadzieje, że będziesz się świetnie bawić :)")
print("")
print("Jak mam się do Ciebie zwracać?" )
print("")
nick = str(input())
nick=nick.upper()
print("")
print("Miło mi Cię poznać " + nick)
print("")
print("Nazywam się HANGMAN i opowiem Ci kilka słów o sobie...")
print("Chcą mnie powiesić, a Ty " + nick + " jesteś moją ostatnią deską ratunku.")
print("Jeśli uda Ci się odgadnąć tajne hasło, pozwolą mi żyć.")
print("Pamiętaj, że każdy Twój błąd to dla mnie krok bliżej do stryczka. Bądź skupiony proszę.")
print("")
print("Na koniec mała podpowiedź - hasło to nazwa państwa lub miasta.")
print("")
print("PAMIĘTAJ! W każdej chwili możesz przerwać grę wpisując 'quit'")
print("")
wybor=input("Jeśli chcesz zacząć wpisz 'start': ")

if wybor=="start":
	print("No to lecimy")
	print("")
else:
	print("Chyba jednak nie chcesz grać. No cóż...")
	print("do zobaczenia innym razem.")
	exit()

def choose_difficulty():
	print("Wybierz poziom trudności: łatwy, średni, trudny")
	difficulty_levels = {
		"łatwy": ("latwy.txt", pic1, 7),
		"średni": ("sredni.txt", pic2, 5),
		"trudny": ("trudny.txt", pic3, 3),
	}
	difficulty = input()			
	if difficulty in difficulty_levels:
		return difficulty_levels[difficulty]
	else:
		print(difficulty + " nie jest poprawnie wpisanym poziomem trudności. Spróbuj ponownie.")
		return choose_difficulty()

def hangman(word: str, num_lives: int):
	guessed_letters = {}
	wrong_letters=[]
	pic_num=0

	
	while num_lives > 0:
		clue = ""
		num_guessed_letters = 0
		for character in word:
			if character.lower() in guessed_letters:
				clue += character
				num_guessed_letters += 1
			else:
				clue += " _ "
		print(clue)
		if num_guessed_letters == len(word):
			print("BRAWO!!! WYGRAŁEŚ! " + nick)
			return
		guess = input("Zgadnij literę. Pozostała liczba prób: " + str(num_lives)+"\n")
		if guess.lower()=="quit":
			print("Do zobaczenia innym razem " + nick)
			exit()
		if len(guess) != 1:
			print("Błędnie wprowadzona litera!. Spróbuj ponownie.")
			continue
		if guess.lower() in guessed_letters:
			print (guess + " Ta litera już była sprawdzana!. Spróbuj ponownie wybierając inną literę.")
			continue
		if guess.lower() not in word:
			num_lives -= 1
			pic_num += 1
			wrong_letters.append(guess)
			print(picture[pic_num])
			print("Błędne litery: ", str(wrong_letters))
		guessed_letters[guess.lower()] = True
	print("Nie masz więcej prób. PRZEGRAŁEŚ. " + nick)

words_file, picture, lives = choose_difficulty()

hangman(word, lives)