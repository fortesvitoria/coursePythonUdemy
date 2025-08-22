'''
Exemplo de nesting com dicionario:
{
    'Key': [List],  #list nested in the dictionary
    'Key2': {Dict},  #dictionary nested in the dictionary

}
'''

#criando dicionario
capitals = {
    'Brazil': 'Brasilia',
    'Germany': 'Berlin',
}

#nested list in dictionary
travel_log = {
    'Brazil': ['Porto Alegre', 'Brasilia', 'São paulo'],
    'Japan': ['Osaka', 'Tokyo', 'Kyoto']
}

print(f'Travel log: {travel_log}')

#acessando item da lista do dicitonario
print(travel_log['Brazil'][1]) #print Brasilia
print(travel_log['Japan'][2]) #print Kyoto

#list inside a list
nested_list = ['A', 'B', ['C', 'D']] #2d list

#print letter 'd' from the nested list
print(nested_list[2][1])

#nesting a dictionary inside a dictionary
travel_loger = {
    'Brazil': {
        'Brasilia':'Capital do pais',
        'Porto Alegre': 'Minha cidade natal',
        'Rio de janeiro': 'Cidade natal do Eduardo',
    },
    'Japan': {
        'num_times_visited': 8,
        'cities_visited': ['Osaka', 'Tokyo', 'Kyoto'],
    }
}

print(travel_loger)

#print Kyoto
print(travel_loger['Japan']['cities_visited'][2])