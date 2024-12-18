import argparse
from SmurfNameGenerator import SmurfNameGenerator

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Generate a Smurf name based on your full name.")
    parser.add_argument('first_name', type=str, help='Your first name')
    parser.add_argument('last_name', type=str, help='Your last name')
    args = parser.parse_args()

    # Create the SmurfNameGenerator object
    smurf_generator = SmurfNameGenerator()

    # Generate the Smurf name
    smurf_name = smurf_generator.smurf_the_name(args.first_name, args.last_name)

    # Print the result
    print(f"Your Smurf name is: {smurf_name}")

if __name__ == "__main__":
    main()
