###IMPORTATION###
import time, os, sys


from platform import python_version
print(python_version)
if int(python_version()[0])<3:
	sys.exit("Il faut minimum Python 3 pour tricher.")



"""
try:
	os.system('python get-pip.py')
except:
	os.system('py get-pip.py')

to_install=[]
try:
	from selenium import webdriver
except:
	to_install.append("selenium")

try:
	from webdriver_manager.chrome import ChromeDriverManager
except:
	to_install.append('webdriver_manager')
try:
	from datetime import datetime
except:
	to_install.append('datetime')

for instal in to_install:

		os.system('python3 -m pip install '+instal)

"""





from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
###IMPORTATION.fin###




identifiant=""  ### Mettre identifiant ici pour pas le remettre a chaque fois
mdp=""			### Mettre mot de passe ici pour pas le remettre a chaque fois




def path_to_url(bb_collab_url):
	try:
		driver=webdriver.Chrome()
	except:
		print("Derniere tentative")
		try:
			driver = webdriver.Chrome(ChromeDriverManager().install())
		except:
			print('Installe Chrome')
			return
	driver.get("https://ent.iledefrance.fr/auth/login?callback=https%3A%2F%2Fent.iledefrance.fr%2F")
	time.sleep(2)
	while True:
		try:
			usrname=driver.find_element_by_xpath('//*[@id="email"]')
			usrname.send_keys(identifiant)
			pw=driver.find_element_by_xpath('//*[@id="password"]')
			pw.send_keys(mdp)
			driver.find_element_by_xpath('/html/body/default-styles/div/div/div/section/div/div/form/div/button/i18n/span').click()
			break
		except:
			time.sleep(2)
	time.sleep(2)
	driver.get(bb_collab_url)
	time.sleep(2)
	try:
		while driver.find_element_by_xpath('/html/body/portal/div/section/div[2]/div/h4/i18n/span').text=="Oups ! La salle que vous tentez de rejoindre n'est pas encore ouverte.":
			driver.get(bb_collab_url)
			print('Salle ferme... Auto-Actualisation')
			time.sleep(7)
	except:
		print('Connecte !')


####INITALISATION####
os.system('clear')
if identifiant=="":
	print('Suis les instructions')
	identifiant=input("Identifiant ENT : ")
if mdp=="":
	mdp=input('Mot de passe ENT : ')

bb_collab_url = input('URL de la visio : ')
os.system('clear')
sheduled=input("Heure et minute de connexion --H-- exemple '10H10' : ")
####INITALISATION.FIN####



print("NE FERME PAS LA PAGE ET LAISSE COMME SA")
print("Je me connecte tout seul a "+sheduled+". "+identifiant.split('.')[0]+" est laid")


while True:
	if datetime.now().strftime('%HH%M')==sheduled:
		os.system('clear')
		print('Il est temps...')
		path_to_url(bb_collab_url)
		break
	time.sleep(10)





