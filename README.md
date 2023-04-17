# python-information-gathring
voici une description du code a quoi sert avec chaque partie 

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = input("Entrez l'URL du site Web : ")
response = requests.get(url)
html_content = response.content
print(html_content)

Ici, le script utilise la bibliothèque "requests" pour envoyer une requête GET à l'URL du site Web saisi par l'utilisateur. Le contenu HTML de la page d'accueil est ensuite stocké dans la variable "html_content" et affiché à l'écran.

robots_url = f"{url}/robots.txt"
robots_txt = requests.get(robots_url).text
print("Contenu du fichier robots.txt :")
print(robots_txt)

Dans cette partie, le script utilise l'URL du site Web pour récupérer le contenu du fichier "robots.txt" et l'afficher à l'écran.

sitemap_url = f"{url}/sitemap.xml"
sitemap_xml = requests.get(sitemap_url).text
print("Contenu du fichier sitemap.xml :")
print(sitemap_xml)

Ici, le script utilise l'URL du site Web pour récupérer le contenu du fichier "sitemap.xml" et l'afficher à l'écran.

homepage = requests.get(url).text
soup = BeautifulSoup(homepage, 'html.parser')
links = [link.get('href') for link in soup.find_all('a')]
print("Liens sur la page d'accueil :")
for link in links:
print(link)

Dans cette partie, le script utilise la bibliothèque "BeautifulSoup" pour extraire tous les liens de la page d'accueil du site Web et les afficher à l'écran.

driver = webdriver.Chrome()
driver.get(url)

start_time = time.time()
driver.refresh()
end_time = time.time()

response_time = end_time - start_time
print("Temps de réponse: ", response_time)

start_time = time.time()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
end_time = time.time()

loading_time = end_time - start_time
print("Temps de chargement: ", loading_time)

driver.quit()

Dans cette partie, le script utilise la bibliothèque "selenium" pour mesurer le temps de réponse et le temps de chargement du site Web en utilisant un navigateur automatisé (Chrome dans ce cas). Le navigateur est ouvert, le temps de réponse est mesuré en actualisant la page et le temps de chargement est mesuré en faisant défiler la page jusqu'à la fin. Enfin, le navigateur est fermé.
