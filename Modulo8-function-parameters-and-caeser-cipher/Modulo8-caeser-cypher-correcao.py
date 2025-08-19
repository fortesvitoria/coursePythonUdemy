# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code? Usando modulo
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
'''
def encrypt(original_text, shift_amount):
   cipher_text = ''
   for letter in original_text:
     shifted_position = alphabet.index(letter) + shift_amount
     shifted_position %= len(alphabet) #usa modulo para percorrer letras com mais de 25 caracteres
     cipher_text += alphabet[shifted_position]

   print(f'Here is the encoded result: {cipher_text}')

encrypt(text, shift)
'''

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
'''
#unica diferença é a direção do shift
def decrypt(original_text, shift_amount):
   output_text = ''
   for letter in original_text:
     shifted_position = alphabet.index(letter) - shift_amount #trocando a direção
     shifted_position %= len(alphabet) #usa modulo para percorrer letras com mais de 25 caracteres
     output_text += alphabet[shifted_position]
   print(f'Here is the decoded result: {output_text}')

decrypt(text, shift)
'''

# TODO-1: Import and print the logo from art.py when the program starts.
# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

#cria lista do alfabeto
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from logo_caeser import logo
print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ''
    if encode_or_decode == "decode":
        shift_amount *= -1  # troca a direção, se posivitvo, vira negativo e vice-versa

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter #add a letra
        else:
            shifted_position = alphabet.index(letter) + shift_amount  # trocando a direção
            shifted_position %= len(alphabet)  # usa modulo para percorrer letras com mais de 25 caracteres
            output_text += alphabet[shifted_position]

    print(f'Here is the {encode_or_decode} result: {output_text}')

should_continue = True

while should_continue:

    directon = input('Type "encode" to encrypt, type "decode" do decrypt: \n')
    text = input('Type your message: \n')
    shift = int(input('Type the shift number: \n'))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=directon)

    restart = input('Type "yes" if you want to go again. Otherwise, type "no". ').lower()
    if restart == 'no':
        should_continue = False
        print('Bye!')
