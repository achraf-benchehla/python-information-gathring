import requests
from bs4 import BeautifulSoup

from selenium import webdriver
import time

url = input("Entrez l'URL du site Web : ")
# ici on va recuperer le contenu du la page html (pentest web on peut l'analyser et trouver les faiblesse du code )
response = requests.get(url)
html_content = response.content

print(html_content)

# Récupérer le fichier robots.txt
robots_url = f"{url}/robots.txt"
robots_txt = requests.get(robots_url).text
print("Contenu du fichier robots.txt :")
print(robots_txt)

# Récupérer le sitemap.xml
sitemap_url = f"{url}/sitemap.xml"
sitemap_xml = requests.get(sitemap_url).text
print("Contenu du fichier sitemap.xml :")
print(sitemap_xml)

# Récupérer les liens de la page d'accueil
homepage = requests.get(url).text
soup = BeautifulSoup(homepage, 'html.parser')
links = [link.get('href') for link in soup.find_all('a')]
print("Liens sur la page d'accueil :")
for link in links:  # afficher les liens qui utilise la page dans chaque ligne 
    print(link)       # ....


# pour que cette partie fonctionne il faut webdriver  
# Charger le site web dans ce cas il faut telecharger les biblio et installer webdriver
driver = webdriver.Chrome()
driver.get(url)

# Mesurer le temps de réponse
start_time = time.time()
driver.refresh()
end_time = time.time()

response_time = end_time - start_time
print("Temps de réponse: ", response_time)

# Mesurer la vitesse de chargement
start_time = time.time()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
end_time = time.time()

loading_time = end_time - start_time
print("Temps de chargement: ", loading_time)

# Fermer le navigateur
driver.quit()

