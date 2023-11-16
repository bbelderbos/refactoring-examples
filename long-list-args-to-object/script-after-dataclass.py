from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    address: str
    phone: str
    email: str

def process_data(person: Person):
    print(f"Processing data for {person.name}, {person.age}, living at {person.address}. Contact info: {person.phone}, {person.email}")

person = Person("Alice", 30, "123 Main St", "555-1234", "alice@example.com")
process_data(person)
