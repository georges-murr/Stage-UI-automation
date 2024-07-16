import requests
from bs4 import BeautifulSoup

url = 'https://usj.edu.lb/'
response = requests.get(url)
web_content = response.content

soup = BeautifulSoup(web_content, 'html.parser')

def extract_element_info(element):
    info = {}
    info['tag'] = element.name
    
    if 'id' in element.attrs:
        info['id'] = element.attrs.get('id')
    if 'name' in element.attrs:
        info['name'] = element.attrs.get('name')
    if 'class' in element.attrs:
        info['class'] = element.attrs.get('class')
    if 'id' in element.attrs:
        info['style'] = element.attrs.get('style')
    if 'alt' in element.attrs:
        info['alt'] = element.attrs.get('alt')

    for attr, value in element.attrs.items():
        if attr not in info:
            info[attr] = value
    
    info['text'] = element.get_text(strip=True)
    info['html'] = str(element)

    return info

elements_info = []
for element in soup.find_all():
    element_info = extract_element_info(element)
    elements_info.append(element_info)

for info in elements_info:
    print(info)
    print('---')
