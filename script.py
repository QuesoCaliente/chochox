import requests
from bs4 import BeautifulSoup
import os
from art import *

def scrapMulti(start_page, end_page, url_base):
    lista = []

    for i in range(int(start_page), int(end_page)+1):   #Recorrer todas las pagina elegidas
        if i > 1:
            url = "%spage/%d" % (url_base, i)
        else:
            url = url_base
        req = requests.get(url)
        print(f'Extrayendo {url}')
        if req.status_code == 200:
            html = BeautifulSoup(req.text, "html.parser")
            posts = html.find_all('a', {'class':'popimg'})
            for post in posts:
                lista.append(post['href'])
    
    for urlpost in lista:
        req2 = requests.get(urlpost)

        if req2.status_code == 200:
            html2 = BeautifulSoup(req2.text, "html.parser")
            imagenesdiv = html2.find_all('div', {'class':'wp-content'})
            titulo = html2.h1.text
            titulo = titulo.replace(' ', '_')
            titulo = titulo.replace('?', '')
            titulo = titulo.replace('-', '_')
            titulo = titulo.replace('/', '_')
            try:
                os.mkdir('imagenes')
            except OSError:
                pass
            if os.path.isdir(f"imagenes/{titulo}"):
                print(f'{titulo} \u001b[31m omitido\u001b[0m [Ya existe]')
                continue
            try:
                os.mkdir(f'imagenes/{titulo}')
            except OSError:
                pass
            print(titulo)
            for post in imagenesdiv:
                for imagen in post.find_all('img'):
                    resultado = imagen['src']
                    iter = len(resultado.split('/'))-1
                    filename = resultado.split('/')[iter]
                    print(f'Descargando... {filename}')
                    request = requests.get(resultado)
                    open(f'imagenes/{titulo}/{filename}', 'wb').write(request.content)
            path2 = f'imagenes/{titulo}'
            os.system(f'cd {path2}')
            os.system(f'optimize-images -nr {path2}') 
            print('# Optimizacion de Imagenes Completa')
            os.system('cls')




def menu():
    texto = "Scrap v0.2"
    Art=text2art(texto)
    os.system('cls')
    print(''.center(100, "="))
    print(Art.center(100,' '))
    print(''.center(100,"="))
    print ("Selecciona una opción")
    print (u"\t1 - \u001b[36m Scrapear Post\u001b[0m")
    print (u"\t2 - \u001b[32m Optimizar Imagenes\u001b[0m")
    print (u"\t3 - \u001b[35m Scrapear Paginas\u001b[0m")
    print (u"\t4 - \u001b[31m Salir\u001b[0m")



while True:
    menu()
    opcion = int(input("Ingresar una opcion: # "))
    if opcion == 1:
        print('Ingresa la url'.center(50,"="))
        url = input('# ')
        if not "chochox.com" in url:
            input("No es una url valida, presiona enter para continuar")
            break
            


        req = requests.get(url)
        status_code = req.status_code
        iterador = 0
        if status_code == 200:
            html = BeautifulSoup(req.text, "html.parser")
            imagenesdiv = html.find_all('div', {'class':'wp-content'})
            titulo = html.h1.text
            titulo = titulo.replace(' ', '_')
            titulo = titulo.replace('?', '')
            titulo = titulo.replace('-', '_')
            titulo = titulo.replace('/', '_')
            try:
                os.mkdir('imagenes')
            except OSError:
                pass
            if os.path.isdir(f"imagenes/{titulo}"):
                continue
            try:
                os.mkdir(f'imagenes/{titulo}')
            except OSError:
                pass
            print(titulo)
            for post in imagenesdiv:
                for imagen in post.find_all('img'):
                    iterador = iterador + 1
                    resultado = imagen['src']
                    iter = len(resultado.split('/'))-1
                    filename = resultado.split('/')[iter]
                    print(f'Descargando... {filename}')
                    request = requests.get(resultado)
                    open(f'imagenes/{titulo}/{filename}', 'wb').write(request.content)
            path2 = f'imagenes/{titulo}'
            os.system(f'cd {path2}')
            os.system(f'optimize-images -nr {path2}') 
            print('# Optimizacion de Imagenes Completa')
            print('---------')
            input('Descarga Finalizada, presiona enter para continuar: # ')
            os.system('cls')
            print('---------')
    elif opcion == 4:
        break
    elif opcion == 2:
        path = 'imagenes/'
        os.system(f'optimize-images {path}') 
    elif opcion == 3:
        print('Ingresa la url'.center(50,"="))
        url = input('# ')
        print('Ingrese Pagina inicio'.center(50,"="))
        start_page = input('# ')
        print('Ingrese Pagina final'.center(50,"="))
        end_page = input('# ')
        scrapMulti(start_page, end_page, url)
    else:
        print("")
        input("No haz elegido una opcion disponible, presiona enter para continuar: # ")
    
