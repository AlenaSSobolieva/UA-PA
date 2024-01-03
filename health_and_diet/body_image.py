# function to evaluate Body Mass Index

def lb_to_kg(lb):
    return lb * 0.45359237


def ft_and_inch_meters(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def bmi(height: str, weight: str) -> float:
    height = float(height)
    weight = float(weight)

    # convert pounds/inches > kilograms/meters
    # add gender
    # add age

    if (weight < 5) and (weight > 200) or (height < 0.5) and (height > 2.5):
        print('pass')
    return height / weight ** 2
