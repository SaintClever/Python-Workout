def get_final_line():
    with open("how_many_different_numbers.py", "r") as f:
        final_line = f.read()
        return final_line.split()[-1]


print(get_final_line())
