from subprocess import check_output
check_output("pip install pyperclip", shell=True)

import hashlib

def getsha256file(archivo):
    try:
        hashsha = hashlib.sha256()
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                hashsha.update(bloque)
        return hashsha.hexdigest()
    except Exception as e:
        print("Error: %s" % (e))
        return ""
    except:
        print("Error desconocido")
        return ""

def getsha256str(stexto):
    hashsha = hashlib.sha256()
    hashsha.update(stexto.encode())
    return hashsha.hexdigest()

true = ''
while true == '':
    start = int(input('Introduce a number of start of the aleatory number: '))
    end = int(input('Introduce a number of finish of the aleatory number: '))
    if start >= end:
        true = ''
        print('The start number must be lower than the finish number!')
    else:
        true = 'Approbed'

import random
value = random.randrange(start, end)

input = input('Enter the direction of file: ')

input = getsha256file(input)
print(input)

x = 0
while x<value:
    input = getsha256str(input)
    print(input)
    x += 1

import pyperclip as clipboard
clipboard.copy(input)

print('\nItered {} times.'.format(x))
print('\nLast value: {}.'.format(input))
print('The hash value is in your paperboard! You can paste using Ctrl + V.')
print('Prueba')
