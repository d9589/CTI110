# David Redmond
# 22 June 2025
# P2 LAB2
# Purpose is to create a dictionary and retrieve the values.


def main():
    # Car Dictionary
    cars_mpg = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

    # Car Keys
    cars = cars_mpg.keys()
    print(f"Your selection of vehicles are {cars}\n")

    # Car Input. MPG Output
    selected_car = input("Enter a vehicle to see it's MPGs: ")
    print(f"The {selected_car} gets {cars_mpg[selected_car]} MPG \n")

    # Miles Input. Gals Needed Output.
    selected_miles = float(
        input(f"How many miles will you drive the {selected_car}?: ")
    )
    print("\n")
    gallons_req = selected_miles / cars_mpg[selected_car]
    print(
        f"{gallons_req:.2f} gallon(s) of gas are needed to drive the {selected_car} {selected_miles} miles."
    )


if __name__ == "__main__":
    main()
