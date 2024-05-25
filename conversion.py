def char_to_byte(character):
    return format(ord(character), '08b')

def word_to_bytes(word):
    return ' '.join(format(ord(c), '08b') for c in word)

def byte_to_ascii(byte_str):
    return chr(int(byte_str, 2))

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Convertir carácter a byte")
        print("2. Convertir palabra a bytes")
        print("3. Convertir byte a ASCII")
        print("4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            char = input("Ingresa un carácter: ")
            print(f"Byte: {char_to_byte(char)}")
        elif choice == '2':
            word = input("Ingresa una palabra: ")
            print(f"Bytes: {word_to_bytes(word)}")
        elif choice == '3':
            byte_str = input("Ingresa un byte (ej. '01100001'): ")
            print(f"ASCII: {byte_to_ascii(byte_str)}")
        elif choice == '4':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
