"""Pobiera istniejące źródła i fonty. Nie generuje obrazów.
Użycie: python3 prepare_inputs.py <work> <fonts>.
"""
from pathlib import Path
import sys,urllib.request
from PIL import Image
work,fonts=map(Path,sys.argv[1:3]);work.mkdir(parents=True,exist_ok=True);fonts.mkdir(parents=True,exist_ok=True)
urls={
's4.png':'https://d8j0ntlcm91z4.cloudfront.net/user_3HWylqcqa2lagu2K8wHWNUz6ROZ/hf_20261014_134921_36c754cd-7267-4f6f-b71b-bc946d2d9ea8.png',
'op916.png':'https://d8j0ntlcm91z4.cloudfront.net/user_3HWylqcqa2lagu2K8wHWNUz6ROZ/hf_20261015_083223_04f94f57-2a17-4886-b777-f8156ec3659b.png',
'op11.png':'https://d8j0ntlcm91z4.cloudfront.net/user_3HWylqcqa2lagu2K8wHWNUz6ROZ/hf_20261015_083407_5a25dc6a-97fb-4227-bcca-0116363f9f75.png',
'approved-v1.png':'https://d2ol7oe51mr4n9.cloudfront.net/user_3HWylqcqa2lagu2K8wHWNUz6ROZ/bf41d724-5ba9-4402-a751-3977c3b04bb5.png'}
for name,url in urls.items():urllib.request.urlretrieve(url,work/name)
# Oryginalny znak z zatwierdzonego PNG, bez rekonstrukcji AI.
Image.open(work/'approved-v1.png').crop((898,1214,1039,1293)).save(work/'logo-siloe.png')
for weight,name in [(400,'Regular'),(500,'Medium'),(600,'SemiBold'),(700,'Bold')]:
 urllib.request.urlretrieve('https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/Poppins-'+name+'.ttf',fonts/('Poppins-'+str(weight)+'.ttf'))
urllib.request.urlretrieve('https://raw.githubusercontent.com/google/fonts/main/ofl/poppins/OFL.txt',fonts/'OFL.txt')
print('Downloaded existing sources and Poppins; no generation.')
