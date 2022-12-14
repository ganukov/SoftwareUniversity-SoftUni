class Person:
    min_age = 0
    max_age = 150

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def __validate_age(cls, value):
        raise ValueError(f'{value} must be between {cls.min_age}'
                         f'and {cls.max_age}')

    # @property
    # def age(self):
    # return self.__age

    # @age.setter
    # def age(self, value):
    # self.__validate_age(value)
    # self.__age = value
