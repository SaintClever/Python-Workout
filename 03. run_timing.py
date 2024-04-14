def run_timing():
    total = []

    while True:
        user_input = input("Enter 10 km run time: ")

        if user_input.isdigit():
            total.append(float(user_input))
        elif not user_input.isdigit() and user_input != "enter":
            print("Type enter")
        else:
            return f"\nAverage of {sum(total) / len(total)}, over {len(total)} runs"


print(run_timing())
