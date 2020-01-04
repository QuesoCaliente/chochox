import requests
from bs4 import BeautifulSoup
import os

def menu():
    os.system('cls')
    print(''.center(100, "="))
    print('Scrap chochox.com'.center(100,' '))
    print(''.center(100,"="))
    print ("Selecciona una opción")
    print ("\t1 - Scrapear Post")
    print ("\t2 - salir")



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
            try:
                os.mkdir('imagenes')
            except OSError:
                pass
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
            print('---------')
            input('Descarga Finalizada, presiona enter para continuar: # ')
            print('---------')
    elif opcion == 2:
        break
    else:
        print("")
        input("No haz elegido una opcion disponible, presiona enter para continuar: # ")
    
