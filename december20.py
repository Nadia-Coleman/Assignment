#!/usr/bin/env python3

def squareArea(side):
    # modify this function to return the area of a square
    area = side * side * side * side
    return area


def circleAreaByDiameter(diameter):
    # modify this function to return the area of a circle given the Diameter
    area = diameter * 3.14 * diameter / 2 * 2
    return area


def equilateralTriangleArea(side):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = side * side * side
    return area


def rectangleArea(sidea, sideb):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = sidea * sideb
    return area


def generalTriangleArea(side):
    area = 1/2 * side * side
    return area


def squareParameter(side):
    area = side * side
    return area


def circleCircumferance(radius):
    area = 3.14 * radius * radius
    return area


def cylinderVolume(radius):
    area = 2 * 3.14 * radius * radius + 2 * 3.14 * radius * radius
    return area


# Also add generalTriangleArea, squareParameter, circleCircumferance, and cylinder volume.


def main():
    print("The area of a square with side = to 4 is: ", squareArea(4))
    print("The area of a circle with diameter = to 4 is: ", circleAreaByDiameter(4))
    print("The area of an Equilateral Triangle with one side = to 4 is: ",
          equilateralTriangleArea(4))
    print("The area of an rectangle with one side = to 4 and another = to 8: ",
          rectangleArea(8, 4))


if __name__ == "__main__":
    main()
