import random

def generate_alphabet():
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    random.shuffle(alphabet)
    return ''.join(alphabet)

def encrypt(text, alphabet):
    encrypted_text = ''
    for char in text.lower():
        if char in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            index = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.index(char)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, alphabet):
    decrypted_text = ''
    for char in text.lower():
        if char in alphabet:
            index = alphabet.index(char)
            decrypted_text += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'[index]
        else:
            decrypted_text += char
    return decrypted_text

def main():
    user_input = input("Введите текст для шифрования: ")
    custom_alphabet = generate_alphabet()
    print("Сгенерированный алфавит:", custom_alphabet)
    
    encrypted_text = encrypt(user_input, custom_alphabet)
    print("Зашифрованный текст:", encrypted_text)
    
    decrypted_text = decrypt(encrypted_text, custom_alphabet)
    print("Расшифрованный текст:", decrypted_text)

if __name__ == "__main__":
    main()
