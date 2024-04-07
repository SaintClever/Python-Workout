"""
Specifically, write a function, get_rainfall, that tracks rainfall in a number of cities. Users of your program will enter the name of a city; 

- if the city name is blank, then  the function prints a report (which I’ll describe) before exiting.

- If the city name isn’t blank, then the program should also ask the user how much  rain has fallen in that city (typically measured in millimeters).

- After the user enters the quantity of rain, the program again asks them for a city name, rainfall amount, and so on—until the user presses Enter instead of typing the name of a city.

- When the user enters a blank city name, the program exits—but first, it reports  how much total rainfall there was in each city.
"""


def get_rainfall():
    data = {}

    while True:        
        city = input("\nCity: ").strip()

        data_formated = "".join(
            f"\n{city:>8}: {rainfall:>8}"
            for city, rainfall in data.items())
        
        if city in data:
            rainfall = float(input("Rainfall: "))
            data[city] = float(data[city]) + rainfall
        
        elif city == "":
            print("\n==== Rainfall ====", data_formated)
            break

        elif city != "":
            rainfall = f"{float(input("Rainfall: ")):.2f}"
            data[city] = rainfall

get_rainfall()
