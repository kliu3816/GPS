from math import cos, sin, pi, acos #import math functions

#calcuates the distance from one coord to another
def distance(lat1, long1, lat2, long2): 
    lat1 = lat1 / (180/pi)
    long1 = long1 / (180/pi)
    lat2 = lat2 / (180/pi)
    long2 = long2 / (180/pi)
    d = 3963.0 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 - long1))
    return d

#adds the distances to a hashtable and determine the closest coords
def disarr(arr1, arr2): 
    disdict = {}
    for x in arr1:
        distances = []
        for y in arr2:
            dis = distance(x[0], x[1], y[0], y[1])
            distances.append(dis)
        minindex = distances.index(min(distances))
        disdict[tuple(x)] = arr2[minindex]
    return disdict
            

def main():
    # arr1 = [(37.7749, -122.4194), (34.0522, -118.2437)]  # Example: San Francisco, Los Angeles
    # arr2 = [(36.7783, -119.4179), (40.7128, -74.0060)]   # Example: California, New York
    print("This program matches locations in the first array to their closest locations in the second array.\n")
    print("Enter the first array (format: latitude,longitude): ")
    print("Type 'done' when you are finished.")
    arr1 = []
    while True:
        user_input = input("Enter point: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            lat, long = map(float, user_input.split(","))
            arr1.append((lat, long))
        except ValueError:
            print("Invalid input! Please enter in the correct format")

    print("\nEnter the second array (latitude, longitude): ")
    print("Type 'done' when you are finished.")
    arr2 = []
    while True:
        user_input = input("Enter point: ").strip()
        if user_input.lower() == 'done':
            break
        try:
            lat, long = map(float, user_input.split(","))
            arr2.append((lat, long))
        except ValueError:
            print("Invalid input! Please enter in the correct format")

    # Check if inputs are valid
    if not arr1 or not arr2:
        print("Both arrays must contain at least one point!")
        return

    # Compute the closest matches

    result = disarr(arr1, arr2)
    for key, value in result.items():
        print(f"{key} in Array 1 is closest to {value} in Array 2.")

if __name__ == "__main__":
    main()