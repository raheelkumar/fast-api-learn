class Animal:

    weight: int
    color: str
    age: int
    animal_type: str

    def eat(self):
        print('Animal eating')

    def sleep(self):
        print('Animal sleeping')


class Dog(Animal):

    can_shed: bool
    domestic_name: str


    def talk(self):  
        print("Bark!!")

    # This is method overriding means it will override the eat method in parent class Animal
    def eat(self):
        print('Chews on bone!')


class Bird(Animal):

    birdType: str

    def talk(slef):
        print('Chirp!')

    def fly(self):
        print('Bird begins to soar!')