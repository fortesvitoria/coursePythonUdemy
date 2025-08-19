# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code? Usando modulo
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#função criptografia
def encrypt(original_text,shift_amount):
    lista_encrypted = []
    for letra in original_text: #para cada letra no texto original
        if letra in alphabet: #se a letra esta no alfabeto
            index_letra = alphabet.index(letra) #pega o index de cada letra dentro do alfabeto
            index_encrypted =  (index_letra + shift_amount) % len(alphabet) #soma o index com o numero so shift e o modulo evita overflow.
            lista_encrypted.append(alphabet[index_encrypted]) #add nova palavra na lista
        else:
            lista_encrypted.append(letra)  # mantem espaços e símbolos
    crypted_text = ''.join(lista_encrypted) #transforma lista em string
    print(f"Texto criptografado: {crypted_text}")
    return crypted_text

#funcao decrypt
def decrypt(crypted_text,shift_amount):
    lista_crypted = []
    for letra in crypted_text:  # para cada letra no texto criptografado
        if letra in alphabet:  # se a letra esta no alfabeto
            index_letra = alphabet.index(letra)  # pega o index de cada letra dentro do alfabeto
            index_encrypted = (index_letra - shift_amount) % len(
                alphabet)  # diminui o index com o numero so shift e o modulo evita overflow.
            lista_crypted.append(alphabet[index_encrypted])  # add nova palavra na lista
        else:
            lista_crypted.append(letra)  # mantem espaços e símbolos
    decrypted_text = ''.join(lista_crypted)  # transforma lista em string
    print(f"Texto descriptografado: {decrypted_text}")
    return decrypted_text

should_continue = True

while should_continue:
    direction = input('Type "encode" to encrypt and "stop" to end the game: \n')

    if direction == 'stop':
        should_continue = False
        print('Goodbye!')
    else:
        # executa de acordo com a escolha
        if direction == 'encode':
            text = input('Type your message: \n').lower()
            shift = int(input('Type the shift number: \n'))
            text_encrypted = encrypt(text, shift)
            direction = input('type "decode" do decrypt and "stop" to end the game: ' )
            if direction == 'decode':
                decrypt(text_encrypted, shift)


# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.



