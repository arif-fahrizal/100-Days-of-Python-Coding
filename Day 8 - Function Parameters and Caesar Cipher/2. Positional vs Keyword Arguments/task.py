# Functions with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_name("Jack Bauer")
greet_with("Cozz", "Javanese")
greet_with(location="Sundanese", name="Blaze")
