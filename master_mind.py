from tkinter import OFF
from colorist import Color, Effect, BrightColor, BgBrightColor, blue, red, green, yellow, white, black, magenta
import random
import time

pions_combi = ['b', 'r', 'v', 'j', 'm']
pions_indic = ['blanc', 'noir']

def master_mind():

	def generate_combi():
		random.shuffle(pions_combi)
		combi_to_find = pions_combi[:4]
		return combi_to_find
    
	def text_to_emo(char):
		if char == 'B':
			char = (f"{BgBrightColor.BLACK}⚪{BgBrightColor.OFF}")
			return char
		elif char == 'N':
			char = (f"{BgBrightColor.BLACK}⚫{BgBrightColor.OFF}")
			return char
		elif char == 'b':
			char = ('🔵')
			return char
		elif char == 'r':
			char = ('🔴')
			return char
		elif char == 'v':
			char = ('🟢')
			return char
		elif char == 'j':
			char = ('🟡')
			return char
		elif char == 'm':
			char = ('🟣')
			return char
		elif char == '.':
			char = (f"{BgBrightColor.BLACK}❌{BgBrightColor.OFF}")
			return char
		else:
			return char


	combi_to_find = generate_combi()

	print('''\nVous devez trouver une combinaison de 4 couleurs dans le bon ordre.\n\nLes couleurs possibles sont Bleu('b'), Rouge('r'), Vert('v'), Jaune('j') et Mauve('m').\n\nUne fois votre combinaison entrée, le jeu vous indique par un point blanc que vous avez la bonne couleur mais pas à la bonne place,\npar un point noir que vous avez la bonne couleur à la bonne place et par une croix rouge que vous n'avez pas la bonne couleur.''')
	for c in combi_to_find:
		print(text_to_emo(c), end=' ')
	table = []

    
	def game():
		def combi_proposal():
			combi = []
			while True:
				input_combi = input("\nEntrez une couleur non déja choisie parmi 'b', 'r', 'v', 'j' ou 'm':  ")
				if input_combi in pions_combi and input_combi not in combi:
					combi.append(input_combi)
					[(print(text_to_emo(c), end=' ')) for c in combi]
					if len(combi) == 4:
						print('\n')
						break
				else:
					print("Saisissez une lettre comme indiqué")
					[(print(text_to_emo(c), end=' ')) for c in combi]
			return combi

		print('\n')

		def combi_check(combi):
			indication = []
			for c in combi:
				if c in combi_to_find and combi.index(c) == combi_to_find.index(c):
					indication.append('N')
				elif c in combi_to_find and combi.index(c) != combi_to_find.index(c):
					indication.append('B')
				else:
					indication.append('.')
			random.shuffle(indication)
			return indication
        
		combi = combi_proposal()
		checking_res = combi_check(combi)

		table.insert(0, (' ').join(combi) + '    ' + (' ').join(checking_res))
		for l in table:
			print('')
			for c in l:
				print(text_to_emo(c), end='')

		while True:
			if len(table) > 5 and checking_res != ['N', 'N', 'N', 'N']:
				print("\n\nLa combinaison était:\n")
				[(time.sleep(1), print(text_to_emo(c))) for c in combi_to_find]
				print("\n\nPERDU :(\n")
				input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
				if input_play_again == 'o':
					return(master_mind())
				else:
					return "AU REVOIR..."
					
			elif checking_res == ['N', 'N', 'N', 'N']:
				# if checking_res == ['N', 'N', 'N', 'N']:
				print("\n\nLa combinaison était bien\n")
				[(print(text_to_emo(c), end=' ')) for c in combi_to_find]
				print(f"\n\n🏅 {Effect.BLINK}{BrightColor.WHITE}GAGNE ! \o/{BrightColor.OFF}{Effect.BLINK_OFF} 😎\n")
				input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
				if input_play_again == 'o':
					return(master_mind())
				else:
					return "AU REVOIR..."
			else:
				print(game())
				return ''

	print(game())


master_mind()