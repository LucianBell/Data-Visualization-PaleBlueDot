from bs4 import BeautifulSoup
import os

# Obtendo o caminho absoluto do diretório do script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construindo o caminho absoluto para o arquivo data.html
file_path = os.path.join(script_dir, 'data.html')

# Abrindo o arquivo usando o caminho absoluto
with open(file_path, 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Encontrar a div que contém a lista de cidades
cities_div = soup.findAll('div', class_="item")

# Criando lista de cidades 
cities_list = []

#Iterando em cada div de cidade
for city_div in cities_div:
    arr_of_name_and_code = city_div.span.text.split(' ')
    code = arr_of_name_and_code[-1].strip('()')
    name = ' '.join(arr_of_name_and_code[0:-1])
    state = city_div['estado']
    city_obj = {
        'code': code,
        'name': name, 
        'state': state
    }
    cities_list.append(city_obj)
