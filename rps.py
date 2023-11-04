import random

message = """Bonjour et bienvenue dans un jeu pierre-papier-ciseaux version ordinateur !!!!! 
Les differents choix sont : 
1-Papier 
2-Pierre 
3-Ciseaux
Le jeu se joue en trois manches, le premier ou la premiere a en remporter 2 gagne"""
print(message)


#variable to count the number of win for the computer
victories = 0

for i in range (3):
	#the computer randomly choose its hand
	choice_ordi = random.randint(1,3)
	#gamer choose its hand
	choice_player = int(input("Veuillez choisir votre main :"))
	#we need to test first if the number is in the list of options
	while choice_player not in [1, 2, 3]: # thanks chatGPT for this line 
		choice_player = int(input("Mauvais choix, veuillez choisir un nombre entre 1 et 3 correspondant a la main que vous comptez utiliser :"))
	#test
	if choice_ordi > choice_player :
		victories =+1 
		print("Mauvaise main")
	else :
		print("Bonne main")
	# end test
	
if victories == 2 :
	print("Game Over")
else :
	print("Bravo !!!")



# the command line on sublim is weird when I build the file 
# the program works well on debian 12 command line 

