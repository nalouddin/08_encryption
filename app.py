
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

disection = input("Shifrlash uchun 'encode' deb yozing, shifrni ochish uchun 'decode' deb yozing\n").lower()
text = input("Xabaringizni yozing:\n").lower()
shift = int(input("Rraqamini kiriting:\n"))

def encrypt(text, shift):
    cipher_text = ""

    for letter in text:
        shefted_position = alphabet.index(letter) + shift
        cipher_text += alphabet[shefted_position % 26]
