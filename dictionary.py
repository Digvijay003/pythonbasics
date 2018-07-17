states = { # choose the bracket carefully for each data strucyures 
    'madhya pradesh': 'mr',
    'goa': 'goaa',
    }

cities = {
    'mr': 'bhopal',
    'ur': 'lknw',
    'goa': 'panaji',
    }

print cities['mr']

print states['goa']

for state in states.items():
    print ("{0}".format(state))# if u get formatting errors use placeholder {} 

for city in cities.items():
    print ("{0}".format(city))
    
