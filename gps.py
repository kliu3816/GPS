import csv
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

def readfile(filename, latcol=None, longcol=None):
    arr = [] 
    try:
        with open(filename, mode = 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            lat_index= header.index(latcol)
            long_index = header.index(longcol)
            for row in reader:
                latitude = float(row[lat_index])
                longitude = float(row[long_index])
                arr.append((latitude, longitude))
        return arr
    except Exception:
        print(f"Error reading file: {Exception}")
        return []
    
def ask_coords():
    choice = input("Do you want to submit a csv file? (y/n)").strip().lower()
    if choice == "y":
        # file = input("Enter csv filename: ").strip()
        # lat = input("Enter the columon name of the Latitude:").strip()
        # long = input("Enter the columon name of the Longitude:").strip()
        return readfile("test1arr2.csv", latcol="latitude", longcol="longitude")
    
    elif choice == "n":
        print("Enter the array (format: latitude,longitude): ")
        print("Type 'done' when you are fyinished.")
        arr = []
        while True:
            user_input = input("Enter point: ").strip()
            if user_input.lower() == 'done':
             break
            try:
                lat, long = map(float, user_input.split(","))
                arr.append((lat, long))
            except ValueError:
                print("Invalid input! Please enter in the correct format")
        return arr
    else:
        print("Invalid choice!")
        return []

def main():
    # arr1 = [(37.7749, -122.4194), (34.0522, -118.2437)]  # Example: San Francisco, Los Angeles
    # arr2 = [(36.7783, -119.4179), (40.7128, -74.0060)]   # Example: California, New York
    print("This program matches locations in the first array to their closest location in the second array.\n")
    print("For the first array, ")
    arr1 = ask_coords()
    print("For the second array, ")
    arr2 = ask_coords()

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
