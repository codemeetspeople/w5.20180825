from string import ascii_lowercase
import random

def deliver(animal):
    animal = animal.capitalize()
    sound = ''.join([random.choice(ascii_lowercase) for _ in range(4)])
    final_sound = f'{sound}-{sound}'

    pattern = (
        '@animal_in_zoo\n'
        'class {name}(Animal):\n'
        '    @classmethod\n'
        '    def speak(cls):\n'
        '        return \'{sound}\'\n'
    ).format(name=animal, sound=final_sound)

    with open('zoo/animals.py', 'r') as f:
        data = f.read()

    with open('zoo/animals.py', 'w') as f:
        f.write(f'\n{data}\n{pattern}\n')