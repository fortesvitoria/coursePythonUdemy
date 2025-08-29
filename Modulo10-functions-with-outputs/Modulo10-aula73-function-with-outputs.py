# fucntions with outputs

def func_output():
    result = 3 * 2
    return result

output = func_output()
print(output)

print('*' * 15)

def format_name(f_name, l_name):
    formated_f_name = f_name.title() #salva output da funcao title dentro de uma variavel
    formated_l_name = l_name.title()  # title funcao para camelcase

    #print(f'{formated_f_name} {formated_l_name}')
    return f'{formated_f_name} {formated_l_name}'
    #o return susbtitui a parte do codigo onde a funcao é chamada.
#ao inves da opcao abaixo, com o return add o output dentro da variavel e chamamos a variavel
#format_name('vitoria', 'FORTES')

formated_str = format_name('vitoria', 'FORTES')
print(formated_str)
print(format_name(input('Your name: '), input('Your surname: '))) #com inputs

print(f'{'*' * 15} Multiple returns{'*' * 15}')

def format_name_2(f_name_2, l_name_2):
    if f_name_2 == '' or l_name_2 == '':
        return 'Invalid inputs'
    formated_f_name_2 = f_name_2.title() #salva output da funcao title dentro de uma variavel
    formated_l_name_2 = l_name_2.title()  # title funcao para camelcase
    return f'{formated_f_name_2} {formated_l_name_2}'


formated_str_2 = format_name_2('eduardo', 'FORTES')
print(formated_str_2)
print(format_name_2(input('Your name: '), input('Your surname: '))) #com inputs

