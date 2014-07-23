#-- coding: utf-8 --
from sys import exit
from random import randrange

"""
1. Implementera så att man kan slumpa fram frågorna och inte i en följd
2. Få alla fel svar (kanske köra om quizen bara på de)
"""

#Lists of answers
alfanumKod=["M",
			"N",
			"T, H, Z", 
			"B",
			"W, V, K",
			"F, R",
			"J, P, X",
			"S, D",
			"G, Q, L",
			"C"
]

figurKod=[
	"Mask","Näsa","Hår","Bulle","Val","Räv","yXa","Dörr","Lök","Cykel",
	"aNeMon", "aNaNas", "NöT","NuBbe","aNKare","NaRrmössa","NyPon","NyStan","NaGel","NyCkel",
	"HuMla","HaNd","HaTt","TaBlett","TV","HaRe","TuPp","HyDda","HaLmbal","TaCo",
	"BoM","BeN(skelett)","BåT","BeBis","BoK","BåR","BoJ","BaDkar","BiL","BoCk(jul-)",
	"KiMono","KaNtarell","VaTtenmelon","KaBelhög","KiWi","KRita","KeX","VaS","VåG","KoCkmössa",
	"RoM","RuNsten","FoT","RaBarber","RaKet","FåR","RiPa","RaDio","FiLm-rulle","RaCket",
	"PuMa","JeaNs","PiZza","JoBbarhjälm","JuKebox","JoRdglob","PaPaya","PiStol","PaLm","JuiCepaket",
	"DoMinospel","DiNosaurie","SHorts","DuBb-däck","DyKare","DRake","SPindel","DoSa","SåG","SäCk",
	"GeM","LöNnlöv","LaTte","eLBas","oLiV","GaRdin","LeoPardmjukisdjur","GåS","GaLage","LoCktång",
	"CyMbal","CoNtainer","CiTronsskriva","CaBriolet","CyKlopöga","CeRat","CaPotasto","CD-skiva","CyLinder","CoCktail"
]

print "\nVälkommen till programmet som ska hjälpa dig förbättra ditt minne!"

#Prints all alfanumeric code to train
def val_1alfaKod:
	for num in range(0,10):
		print "%s - %s" % (num, alfanumKod[num])
	print "\nTryck på ENTER för att komma tillbaka till menyn:"
	raw_input("")
	menu()

#Prints all coded numbers to train
def val_kodSiffror():
	for num in range(0,100):
		print "%d - %s" % (num, figurKod[num])
	print "\nTryck på ENTER för att komma tillbaka till menyn:"
	raw_input("")
	menu()

#Quiz for alfanumeric codes, user choose different settings
def val_alfaKodTrain():
	print "\nTräna alfanumerisk kod i:\n1. Följd\n2. Slump"
	points=0
	option=raw_input("> ")

	if option=="1":
		for num in range(0,10):
			print "%s - ?" % num
			answer=raw_input("> ")
			if answer==alfanumKod[num]:
				points=points+1
			elif answer=="rätta":
				break
			else:
				print "Fel, rätt svar: %s" % alfanumKod[num]
		print "\n%d/10 rätt\n" % points
	menu()

#Quiz for coded numbers, user choose different settings
def val_alfaKodTrain():
	print "\nTräna kodade siffror i:\n1. Följd\n2. Slump"
	points=0
	option=raw_input("> ")

	if option=="1":
		for num in range(0,100):
			print "%d - ?" % num
			answer=raw_input("> ")
			if answer==figurKod[num]:
				print "Rätt!\n"
				points=points+1
			elif answer=="rätta":
				break
			else:
				print "Fel, rätt svar: %s" % figurKod[num]
	elif option=="2":
		for num in random(0,100)
			print ""
	print "===========\n|%d/100 rätt|\n===========\n" % points
	print "Tryck på ENTER för att ta dig tillbaka till huvudmenyn"

def avsluta():
	exit(0)

def menu():

	print "====== Meny ======"
	print "1. Alfanumerisk kod\n2. Kodade siffror\n3. Träna alfanumerisk kod\n4. Träna kodade siffror\n5. Avsluta"
	print "=================="
	while True:
		option=raw_input("> ")
		
		if option=="1":
			val_alfaKod()
		elif option=="2":
			val_kodSiffror()
		elif option=="3":
			val_alfaKodTrain()
		elif option=="4":
			val_kodSiffrorTrain()
		elif option=="5":
			avsluta()
		else:
			#print "\nVar god välj igen\n"
			menu()

			
menu()