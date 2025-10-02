#function with two parameters

def greet_with(name,location):
    print(f'Welcome {name}! Whats is like in {location}?')

#positional arguments - aqui importa a posição
greet_with('Vitoria', 'Porto Alegre')

#keyword arguments - aqui tanto faz a posição
greet_with(name='Eduardo', location='Rio')
greet_with(location='Viamão',name='Lucas')
