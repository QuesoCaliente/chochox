import requests
from bs4 import BeautifulSoup
import os, sys
from PIL import Image
from time import sleep
import glob
path = os.getcwd()

def scrapMulti(start_page, end_page, url_base):
    lista = []
    iterador = 1
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
                    resultado = resultado.replace('hhtps', 'https')
                    iter = len(resultado.split('/'))-1
                    filename = resultado.split('/')[iter]
                    print(f'Descargando... {filename}')
                    request = requests.get(resultado)
                    if request.status_code != 200:
                        print('Error Imagen No disponible')
                        sleep(1)
                        continue
                    path = os.getcwd()
                    open(f'imagenes/{titulo}/{filename}', 'wb').write(request.content)
                    oldsize = os.stat(f'imagenes/{titulo}/{filename}').st_size
                    picture = Image.open(f'imagenes/{titulo}/{filename}')
                    if ".gif" in filename:
                        try:
                            picture.save(f"{path}/imagenes/{titulo}/{filename}",optimize=True,quality=85, save_all=True, append_images=[im.seek(im.tell() + 1)])
                        except:
                            pass
                    else:
                        picture.save(f"{path}/imagenes/{titulo}/{filename}",optimize=True,quality=85)
                    newsize = os.stat(f'imagenes/{titulo}/{filename}').st_size
                    print(f'{filename} \u001b[32m Optimizado\u001b[0m  {oldsize} - {newsize}')
                    
            print('# Descarga de Imagenes Completa')
            print('# Optimizacion de Imagenes Completa')
            sleep(1)
            os.system('cls')




def menu():
    texto ='''
     __                               ___   ____  
    / _\ ___ _ __ __ _ _ __   /\   /\/ _ \ |___ \ 
    \ \ / __| '__/ _` | '_ \  \ \ / / | | |  __) |
    _\ \ (__| | | (_| | |_) |  \ V /| |_| | / __/ 
    \__/\___|_|  \__,_| .__/    \_/  \___(_)_____|
                      |_|                         
    '''
    os.system('cls')
    print(''.center(100, "="))
    print(texto.center(100,' '))
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
                print("\u001b[31;1m Error: \u001b[33;1m Ya existe el directorio")
                input("Presione\u001b[34;1m Enter \u001b[37m Para continuar")
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
                    resultado = resultado.replace('hhtps', 'https')
                    iter = len(resultado.split('/'))-1
                    filename = resultado.split('/')[iter]
                    print(f'Descargando... {filename}')
                    request = requests.get(resultado)
                    if request.status_code != 200:
                        print('Error Imagen No disponible')
                        sleep(1)
                        continue
                    path = os.getcwd()
                    open(f'{path}/imagenes/{titulo}/{filename}', 'wb').write(request.content)
                    oldsize = os.stat(f'imagenes/{titulo}/{filename}').st_size
                    picture = Image.open(f'imagenes/{titulo}/{filename}')

                    if ".gif" in filename:
                        try:
                            picture.save(f"{path}/imagenes/{titulo}/{filename}",optimize=True,quality=85, save_all=True, append_images=[im.seek(im.tell() + 1)])
                        except:
                            pass
                    else:
                        picture.save(f"{path}/imagenes/{titulo}/{filename}",optimize=True,quality=85)
                    newsize = os.stat(f'imagenes/{titulo}/{filename}').st_size
                    print(f'{filename} \u001b[32m Optimizado\u001b[0m {oldsize} - {newsize}')
                    
            path2 = f'imagenes/{titulo}'
            print('# Optimizacion de Imagenes Completa')
            print('---------')
            input('Descarga Finalizada, presiona enter para continuar: # ')
            os.system('cls')
            print('---------')
    elif opcion == 4:
        break
    elif opcion == 2:
        path = os.getcwd()
        carpetas = os.listdir(f'{path}/imagenes')

        for nombre in carpetas:
            archivos = glob.glob(f"{path}/imagenes/{nombre}/*")
            for file in archivos:
                oldsize = os.stat(f'{file}').st_size
                picture = Image.open(f'{file}')
                picture.save(f"{file}","JPEG",optimize=True,quality=85)
                newsize = os.stat(f'{file}').st_size
                filename = os.path.splitext(file)[0]
                print(f'{filename} \u001b[32m Optimizado\u001b[0m  {oldsize}kb - {newsize}kb')
                sleep(0.2)
                
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
    
