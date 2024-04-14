# import operator


def format_sort_records(people):
    return "".join(
        f"{person[1]:<10} {person[0]:<10} {person[2]:5.2f}\n" for person in people
    )

    # or

    # return "".join(
    #     "{1:10}{0:10}{2:5.2f}\n".format(*person)
    #     for person in sorted(people, key=operator.itemgetter(1))
    # )


PEOPLE = [
    ("Donald", "Trump", 7.85),
    ("Vladimir", "Putin", 3.626),
    ("Jinping", "Xi", 10.603),
]

print(format_sort_records(PEOPLE))
