'''
Functions Assignment

- Create a function that takes in 3 parameters(firstname, lastname, age) and returns a dictionary based on those values
'''

def create_dict(first: str, last: str, age: int):
    person = {"first_name: ": first, "last_name: ": last, "age: ": age}
    return person

if __name__ == "__main__":
    print(create_dict("Raheel", "Kumar", 27))