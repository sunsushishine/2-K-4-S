def rot1(text, alphabet, encrypt=True):
    shift = 1 if encrypt else -1
    shifted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            idx = (alphabet.index(char.upper()) + shift) % len(alphabet)
            shifted_char = alphabet[idx]
            shifted_text += shifted_char if is_upper else shifted_char.lower()
        else:
            shifted_text += char
    return shifted_text

# Алфавит #FIXME
english_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
russian_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

text = input("Введите текст для шифрования: ")
encrypted_text = rot1(text, english_alphabet + russian_alphabet)
print("Зашифрованный текст:", encrypted_text)
decrypted_text = rot1(encrypted_text, english_alphabet + russian_alphabet, encrypt=False)
print("Расшифрованный текст:", decrypted_text)
