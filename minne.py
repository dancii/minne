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
def val_alfaKod():
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
			if answer.lower()==alfanumKod[num].lower():
				points=points+1
				print "Rätt!"
			elif answer.lower()=="check":
				break
			else:
				print "Fel, rätt svar: %s" % alfanumKod[num]
	#Ask the questions in a random order
	elif option=="2":
		count=0
		lstKnownNumbs=[False]*10
		while (count < 10):
			num = knownNumb(10, lstKnownNumbs)
			lstKnownNumbs[num] = True
			print "%s - ?" % num
			answer=raw_input("> ")
			if answer.lower()==alfanumKod[num].lower():
				points=points+1
				print "Rätt!"
			elif answer.lower()=="check":
				break
			else:
				print "Fel, rätt svar: %s" % alfanumKod[num]
			count=count+1
		lstKnownNumbs[:]=[]
	print "===========\n|%d/10 rätt|\n===========\n" % points
	menu()

#Quiz for coded numbers, user choose different settings
def val_kodSiffrorTrain():
	print "\nTräna kodade siffror i:\n1. Följd\n2. Slump"
	points=0
	option=raw_input("> ")

	if option=="1":
		for num in range(0,100):
			print "%d - ?" % num
			answer=raw_input("> ")
			if answer.lower()==figurKod[num].lower():
				print "Rätt!\n"
				points=points+1
			elif answer.lower()=="check":
				break
			else:
				print "Fel, rätt svar: %s" % figurKod[num]
	elif option=="2":
		count=0
		lstKnownNumbs=[False]*100
		while (count < 101):
			num = knownNumb(101, lstKnownNumbs)
			lstKnownNumbs[num] = True
			print "%s - ?" % num
			answer=raw_input("> ")
			if answer.lower()==figurKod[num].lower():
				points=points+1
				print "Rätt!"
			elif answer.lower() == "check":
				break
			else:
				print "Fel, rätt svar: %s" % figurKod[num]
			count=count+1
		lstKnownNumbs[:]=[]
	print "============\n|%d/100 rätt|\n============\n" % points
	menu()

def val_instruktioner():
	print "\nFörst väljer du vilken övning du vill göra för att sedan välja på vilket sätt du vill utföra övningen"
	print "Du kan avbryta och rätta när som helst under dina övningar genom att skriva 'check' istället för att svara"
	print "Du får fram dina antal rätt och menyn kommer tillbaka\n"
	menu()

def knownNumb(range, lstKnownNumbs):
	found = False
	while (found == False):
		num=randrange(range)
		if lstKnownNumbs[num]==True:
			found = False
		else:
			found = True
	return num


def menu():

	print "====== Meny ======"
	print "1. Alfanumerisk kod\n2. Kodade siffror\n3. Träna alfanumerisk kod\n4. Träna kodade siffror\n5. Instruktioner\n6. Avsluta"
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
			val_instruktioner()
		elif option=="6":
			exit(0)
		else:
			#print "\nVar god välj igen\n"
			menu()

			
menu()