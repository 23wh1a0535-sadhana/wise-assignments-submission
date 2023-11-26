def calculate_cube_volume(side_length):
    # Calculate the volume of the cube
    volume = side_length ** 3
    return volume

def main():
    # Get user input for the side length
    side_length = float(input("Enter the side length of the cube: "))

    # Ensure the side length is positive
    if side_length <= 0:
        print("Side length must be a positive number.")
    else:
        # Calculate and display the volume
        volume = calculate_cube_volume(side_length)
        print(f"The volume of the cube with side length {side_length} is: {volume}")

