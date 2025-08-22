#criando um dicionario
# {'Key':'Value'}
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program to run as expected.',
    'Function': 'A piece of code that you can easily call over and over again',
}
#print(programming_dictionary)

#selecionando o item no dicionario
#print(programming_dictionary['Bug'])

#adcionando data
programming_dictionary['Loop'] = 'The action of doing something over and over again'

#print(programming_dictionary)

#empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#edit and item
programming_dictionary['Bug'] = 'New info about bug'
#print(programming_dictionary['Bug'])

#Loop through a dictionary
for key in programming_dictionary:
    print(key) #nesse caso só informa a chave
    print(programming_dictionary[key]) #informa o valor