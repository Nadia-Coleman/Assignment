#!/usr/bin/env python3

def squareArea(side):
    # modify this function to return the area of a square
    area = side * side
    return area


def circleAreaByDiameter(diameter):
    # modify this function to return the area of a circle given the Diameter
    area = 3.14 * diameter  # incorrect formula
    return area


def equilateralTriangleArea(side):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = .43 * side * side  # incorrect formula
    return area


def rectangleArea(sidea, sideb):
    # modify this function to return the area of an Equilateral Triangle given one side
    area = sidea * sideb
    return area


def generalTriangleArea(sidea, sideb):
    area = 1/2 * sidea * sideb  # incorrect formula
    return area


def squareParameter(side):
    area = 4 * side  # incorrect formula
    return area


def circleCircumferance(radius):
    area = 2 * 3.14 * radius  # incorrect formula
    return area


def cylinderVolume(radius, height):
    area = 3.14 * radius * radius * height # incorrect formula
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
    print("The area of a rectangle with one side = to 4 and another = to 8: ",
          rectangleArea(8, 4))
    print("The answer below should be 16.")
    print("The area of a general triangle with sidea = to 4 and sideb = to 7 is: ", generalTriangleArea(4,8))
    print("The answer below should be 36.")
    print("The area of a square parameter with side = to 9 is: ", squareParameter(9))
    print("The answer bellow should be 31.4.")
    print("The circumference of a circle with radius = to 5 is: ", circleCircumferance(5))
    print("The answer bellow should be 1005 when rounded.")
    print("The volume of a cylinder with radius = to 8 and height = to 5 is: ", cylinderVolume(8,5))



if __name__ == "__main__":
    main()
