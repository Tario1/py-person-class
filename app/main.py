class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    persons_list = [Person(person_dict.get("name"),
                    person_dict.get("age")) for person_dict
                    in people if person_dict.get("name") is not None
                    and person_dict.get("age") is not None]

    for person_dict in people:
        current_person = Person.people.get(person_dict.get("name"))
        if not current_person:
            continue
        partner_name = person_dict.get("wife")
        if partner_name and partner_name in Person.people:
            current_person.wife = Person.people[partner_name]
        partner_name = person_dict.get("husband")
        if partner_name and partner_name in Person.people:
            current_person.husband = Person.people[partner_name]
    return persons_list
