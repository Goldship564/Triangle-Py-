# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def is_valid_triangle(a, b, c):
    """Check if three sides can form a valid triangle"""
    return (a + b > c) and (b + c > a) and (a + c > b) and (a > 0) and (b > 0) and (c > 0)

def plot_triangle(a, b, c):
    """Plot triangle using given side lengths"""
    # Place first point at origin (0,0)
    x = [0, a, 0]
    y = [0, 0, 0]

    # Calculate third point using law of cosines
    # Angle between a and b
    cos_C = (a*a + b*b - c*c) / (2*a*b)
    x[2] = b * cos_C
    y[2] = b * (1 - cos_C**2)**0.5

    # Create the plot
    plt.figure(figsize=(8, 6))
    plt.plot(x + [x[0]], y + [y[0]], 'm-', linewidth=2)  # Connect points and close triangle
    plt.fill(x, y, 'magenta', alpha=0.3)  # Fill triangle with transparent color

    # Add labels
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, f'P{i+1}', ha='right')

    plt.title(f'Triangle with sides {a}, {b}, {c}')
    plt.grid(True)
    plt.axis('equal')  # Equal aspect ratio
    plt.show()

def main():
    print("Welcome to Triangle Checker!")
    print("Enter three positive numbers to see if they form a triangle")

    while True:
        try:
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            c = float(input("Enter side c: "))

            if is_valid_triangle(a, b, c):
                print(f"\nYes, {a}, {b}, {c} can form a triangle!")
                plot_triangle(a, b, c)
            else:
                print(f"\nNo, {a}, {b}, {c} cannot form a triangle")

            if input("\nTry again? (y/n): ").lower() != 'y':
                break

        except ValueError:
            print("Please enter valid numbers")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
