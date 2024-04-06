def alphabetize_names(people):
    output = []

    for person in people:
        output.append(
            {
                "last": person.get("last"),
                "first": person.get("first"),
                "email": person.get("email"),
            }
        )

    return output


PEOPLE = [
    {"first": "Reuven", "last": "Lerner", "email": "reuven@lerner.co.il"},
    {"first": "Donald", "last": "Trump", "email": "president@whitehouse.gov"},
    {"first": "Vladimir", "last": "Putin", "email": "president@kremvax.ru"},
]

print(alphabetize_names(PEOPLE))
