from zoo import animals
from zoo.delivery import deliver
from importlib import reload

while True:
    reload(animals)
    print('Available animals: {}'.format(
        ', '.join(animals.ANIMALS.keys())
    ))
    print('Choose one (or \'exit\'):')

    action = input().strip()

    if action == 'exit':
        print('Bye-bye!')
        exit()

    if action not in animals.ANIMALS:
        print(f'{action} in progress. Try again!')
        print()
        deliver(action)
        continue

    print(f'{action}: {animals.ANIMALS[action].speak()}')
    print()
