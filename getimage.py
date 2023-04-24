#requests
import os
import requests

def Save(url):
    f_ext = os.path.splitext(url)[-1]
    print(f_ext)
    f_name = 'img{}'.format(f_ext)
    page = requests.get(url)
    with open(f_name, 'wb') as f:
        f.write(page.content)

url='https://tse3.mm.bing.net/th?id=OIP.U46kDcwtmtNDF6EZIenZtAHaE8&pid=15.1.jpg'
Save(url)