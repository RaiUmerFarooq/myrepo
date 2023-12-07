def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    print("Welcome to the Rectangle Calculator!")

    # Get user input for length and width
    length = 12
    width = 13

    # Calculate area and perimeter
    area, perimeter = calculate_rectangle_properties(length, width)

    # Display results
    print(f"\nArea of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

if __name__ == "__main__":
    main()
