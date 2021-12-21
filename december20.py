#!/usr/bin/env python3

def squareArea(side):
    # modify this function to return the area of a square
    area = side * side
    return area


def circleAreaByDiameter(diameter):
    # modify this function to return the area of a circle given the Diameter
    area = diameter * 3.14 * diameter / 2 * 2 #incorrect formula
    return area


def equilateralTriangleArea(side):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = side * side * side #incorrect formula
    return area


def rectangleArea(sidea, sideb):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = sidea * sideb
    return area


def generalTriangleArea(side):
    area = 1/2 * side * side #incorrect formula
    return area


def squareParameter(side):
    area = side * side #incorrect formula
    return area


def circleCircumferance(radius):
    area = 3.14 * radius * radius #incorrect formula
    return area


def cylinderVolume(radius):
    area = 2 * 3.14 * radius * radius + 2 * 3.14 * radius * radius #incorrect formula
    return area


# Also add generalTriangleArea, squareParameter, circleCircumferance, and cylinder volume.


def main():
    print("The bellow answer should be 16")
    print("The area of a square with side = to 4 is: ", squareArea(4))
    print("The bellow answer should be 12.56")
    print("The area of a circle with diameter = to 4 is: ", circleAreaByDiameter(4))
    print("The bellow answer should be 6.928")
    print("The area of an Equilateral Triangle with one side = to 4 is: ",
          equilateralTriangleArea(4))
    print("The bellow answer should be 32")
    print("The area of an rectangle with one side = to 4 and another = to 8: ",
          rectangleArea(8, 4))


if __name__ == "__main__":
    main()
