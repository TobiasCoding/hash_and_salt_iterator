import hashlib, random

def getsha256str(stexto):
    hashsha = hashlib.sha256()
    hashsha.update(stexto.encode())
    return hashsha.hexdigest()

def getsha256file(filepath):
    hashsha = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hashsha.update(chunk)
    return hashsha.hexdigest()

def create_iterated_hash():
    file = input("\nSet the file: ")
    current_hash = getsha256file(file)

    salts = ""
    for i in range(2):
        randomness = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for _ in range(10))
        current_hash = getsha256str(current_hash + randomness)
        salts += randomness + "\n"
    
    filename = f"salts-{current_hash}.txt"

    with open(filename, "a") as file:
        file.write(f"{current_hash}\n{salts[:-1]}")

    print(f'''> Hash: {current_hash}\n> Salts route file: {filename}''')

def check_hash():
    file = input("\nSet the original file to check: ")
    salt_route_file = input("\nSet the salt route file: ")

    current_hash = getsha256file(file)

    with open(salt_route_file, "r") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i == 0:
                target_hash = line.strip()
            else:
                current_hash = getsha256str(current_hash + line.strip())

    if current_hash == target_hash:
        print(f"\n😊 Hash SI coicide!\nEl archivo es original")
    else:
        print(f"\n🥺 El hash NO coincide.\nEl archivo no es original o la ruta de sal es incorrecta o ha sido manipulada")


while True:
    print("\nOpciones:")
    print("1. Crear un hash iterado con sal")
    print("2. Chequear hash")
    print("3. Salir")
    
    choice = input("\nElija una opción (1, 2, 3): ")
    
    if choice == "1":
        create_iterated_hash()
    elif choice == "2":
        check_hash()
    elif choice == "3":
        break
    else:
        print("\nOpción inválida, por favor intente de nuevo.")
