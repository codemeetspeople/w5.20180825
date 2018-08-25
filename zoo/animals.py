


ANIMALS = {}


def animal_in_zoo(cls):
    if cls.get_name() not in ANIMALS:
        ANIMALS[cls.get_name()] = cls
    return cls


class Animal:
    @classmethod
    def get_name(cls):
        return cls.__name__.lower()

    @classmethod
    def speak(cls):
        return NotImplementedError()


@animal_in_zoo
class Donkey(Animal):
    @classmethod
    def speak(cls):
        return 'heee-haaa'


@animal_in_zoo
class Wolf(Animal):
    @classmethod
    def speak(cls):
        return 'wooo-wooo'

@animal_in_zoo
class Elephant(Animal):
    @classmethod
    def speak(cls):
        return 'jhej-jhej'


@animal_in_zoo
class Tiger(Animal):
    @classmethod
    def speak(cls):
        return 'xwzo-xwzo'


@animal_in_zoo
class Fox(Animal):
    @classmethod
    def speak(cls):
        return 'olgo-olgo'

