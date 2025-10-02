'''
LISTS
name = ['Vitoria', 'Marta', 'Aline']
'''

states_of_brazil=['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins']
print(f'State at the position{states_of_brazil.index(states_of_brazil[15]), states_of_brazil[15]} in a total of {len(states_of_brazil)} states.')

#Start count from end to start
print(f'State at the position, starting from negative index {states_of_brazil.index(states_of_brazil[-27]), states_of_brazil[-27]} in a total of {len(states_of_brazil)} states.')


print('Replace item to the list:')
print('*** Before: ***')
print(f'State at the position{states_of_brazil.index(states_of_brazil[1]), states_of_brazil[1]} in a total of {len(states_of_brazil)} states.')
print(f'State at the position{states_of_brazil.index(states_of_brazil[2]), states_of_brazil[2]} in a total of {len(states_of_brazil)} states.')
print(f'State at the position{states_of_brazil.index(states_of_brazil[3]), states_of_brazil[3]} in a total of {len(states_of_brazil)} states.')

print('*** After: ***')
states_of_brazil[2] = "BAZINGA!"
print(f'State at the position{states_of_brazil.index(states_of_brazil[1]), states_of_brazil[1]} in a total of {len(states_of_brazil)} states.')
print(f'State at the position{states_of_brazil.index(states_of_brazil[2]), states_of_brazil[2]} in a total of {len(states_of_brazil)} states.')
print(f'State at the position{states_of_brazil.index(states_of_brazil[3]), states_of_brazil[3]} in a total of {len(states_of_brazil)} states.')

print('Add item to the end of the list:')
states_of_brazil.append('THCUM!')
print(states_of_brazil[27])

print('Add an list to the list:')
states_of_brazil.extend(['BLA','BLE'])
print(states_of_brazil)