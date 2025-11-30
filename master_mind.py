from colorist import Color, Effect, BrightColor, BgBrightColor, blue, red, green, yellow, white, black, magenta
import random
import time
from ascii import title, bye, perdu
from datetime import date
import os

pions_combi = ['b', 'r', 'v', 'j', 'm']

print(title)
print('\n')
print(f'''\nVous devez trouver une combinaison de 4 couleurs dans le bon ordre.\n\nLes couleurs possibles sont {BrightColor.BLUE}Bleu{BrightColor.OFF}('b'), {BrightColor.RED}Rouge{BrightColor.OFF}('r'), {BrightColor.GREEN}Vert{BrightColor.OFF}('v'), {Color.YELLOW}Jaune{Color.OFF}('j') et {Color.MAGENTA}Mauve{Color.OFF}('m').\n\nUne fois votre combinaison entrée, le jeu vous indique par un point blanc que vous avez la bonne couleur mais pas à la bonne place,\npar un point noir que vous avez la bonne couleur à la bonne place et par une croix rouge que vous n'avez pas la bonne couleur.''')
print('\n')


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
	
def generate_combi():
	random.shuffle(pions_combi)
	combi_to_find = pions_combi[:4]
	table = []
	return [combi_to_find, table]

combi_to_find = generate_combi()[0]
table = generate_combi()[1]
score_V = []

    
def game(combi_to_find, table):

	input_play_again = 'n'
	printed_combi = []

	for c in combi_to_find:
		printed_combi.append(text_to_emo(c))
		# print(text_to_emo(c), end=' ')


	def combi_proposal():
		combi = []
		while True:
			input_combi = input("Entrez une couleur non déja choisie parmi 'b', 'r', 'v', 'j' ou 'm':  ")
			if input_combi in pions_combi and input_combi not in combi:
				print('\n')
				combi.append(input_combi)
				[(print(text_to_emo(c), end=' ')) for c in combi]
				print('\n')
				if len(combi) == 4:
					print('\n'*27)
					break
			else:
				red("\nSaisissez une lettre comme indiqué")

		return combi



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
	
	print('\n')

	def game_longest_win_serie(score_V):
		stg_score_V = ('').join(score_V)
		stg_score_V = 'S' + stg_score_V
		indexes_S = []
		V_series = []
		len_series = []
		
		# print("score_v :", score_V)
		for x in range(len(stg_score_V)):
			if stg_score_V[x] == 'S':
				indexes_S.append(x)
		indexes_S.append(None)

		for x in range(len(indexes_S)-1):
			V_series.append(stg_score_V[indexes_S[x]:indexes_S[x+1]])
		for serie in V_series:
			if 'V' in serie:
				len_series.append(len(serie))
		if len_series:
			result = max(len_series)-1
		else:
			result = None
		return result

	def save_game_max_win_series(score):
		jour = date.today().strftime("%d/%m/%y")
		with open('MM-max-win-series.txt', 'a') as f:
			f.write(str([jour, score])+'\n')
			f.close()

	def display_5_best_series():
		clean_scores = {}
		scores = open("MM-max-win-series.txt", "r")
		scores_raw = scores.readlines()
		scores_r = []
		if scores_raw:
			for x in range(len(scores_raw)):
				scores_r.append(scores_raw[x][0:-1])
				scores_r[x] = scores_r[x].strip("['']").split("', ")

			for x in range(len(scores_r)):
				if not clean_scores.get(scores_r[x][0]):
					clean_scores[scores_r[x][0]] = []
			for x in range(len(scores_r)):
				if scores_r[x][1] != 'None':
					clean_scores[scores_r[x][0]].append(scores_r[x][1])

			clean_scores = dict(sorted(clean_scores.items()))

			ordered_scores = []
			for k, v in clean_scores.items():
				for n in v:
					ordered_scores.append([int(n), k])
			ordered_scores = sorted(ordered_scores, reverse=True)
			
			best_5_series = []
			for x in range(len(ordered_scores)):
				if x == 5:
					break
				best_5_series.append(ordered_scores[x][1] + '  ' + str(ordered_scores[x][0]))
			return best_5_series
		else:
			return None

	while True:
		if len(table) >= 6 and checking_res != ['N', 'N', 'N', 'N']:
			score_V.append('S')
			max_win_serie = game_longest_win_serie(score_V=score_V)
			
			print(perdu)
			print("\n\nLa combinaison était:\n")
			[(time.sleep(1), print(text_to_emo(c))) for c in combi_to_find]
			print('\n')
			print("Série de victoires la plus longue dans cette partie:", max_win_serie)
			print('\n')
			input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
			if input_play_again == 'o':
				print('\n')
				return game(combi_to_find= generate_combi()[0], table=generate_combi()[1])
			else:
				print('\n')
				save_game_max_win_series(max_win_serie)
				input_display_best_scores = input("Afficher les meilleurs scores réalisés ? 'o' oui, 'n' non :  ")
				if input_display_best_scores == 'o':
					print('\n')
					best_5_series = display_5_best_series()
					for s in best_5_series:
						print(s)
				else:
					return bye				
				return bye
				
		elif len(table) <= 6 and checking_res == ['N', 'N', 'N', 'N']:
			score_V.append('V')
			max_win_serie = game_longest_win_serie(score_V=score_V)
			
			print("\n\nLa combinaison était bien" + '  ' + (' ').join(printed_combi))
			print('\n')
			print(rf"🏅 {Effect.BLINK}{BrightColor.WHITE}GAGNE ! \o/{BrightColor.OFF}{Effect.BLINK_OFF} 😎")
			print('\n')
			print("Série de victoires la plus longue dans cette partie:", max_win_serie)
			print('\n')
			input_play_again = input("Une autre partie ? Entrez 'o' oui, 'n' non :  ")
			if input_play_again == 'o':
				print('\n')
				return game(combi_to_find= generate_combi()[0], table=generate_combi()[1])		
			else:
				print('\n')
				save_game_max_win_series(max_win_serie)
				input_display_best_scores = input("Afficher les meilleurs scores réalisés ? 'o' oui, 'n' non :  ")
				if input_display_best_scores == 'o':
					print('\n')
					best_5_series = display_5_best_series()
					for s in best_5_series:
						print(s)
				else:
					return bye
				return bye

		elif len(table) < 6 and checking_res != ['N', 'N', 'N', 'N']:
			return(game(combi_to_find, table))


print(game(generate_combi()[0], generate_combi()[1]))
