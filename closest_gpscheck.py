import csv
from math import cos, sin, pi, acos #import math functions

#calcuates the distance from one coord to another
def distance(lat1, long1, lat2, long2): 
    lat1 = lat1 / (180/pi)
    long1 = long1 / (180/pi)
    lat2 = lat2 / (180/pi)
    long2 = long2 / (180/pi)
    d = 3963.0 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 - long1))
    return d * 1.609344 #convert to km

#adds the distances to a hashtable and determine the closest coords
def disarr(arr1, arr2): 
    disdict = {}
    arr2 = sorted(arr2, key=lambda point: point[0])

    for x in arr1:
        distances = []
        min_dist = float('inf')
        closest = None

        for y in arr2:
            if abs(y[0] - x[0]) > min_dist/111:
                break

            dis = distance(x[0], x[1], y[0], y[1])
            if dis < min_dist:
                min_dist = dis
                closest = y
        disdict[tuple(x)] = tuple(closest)
    return disdict

def readfile(filename, latcol, longcol):
    arr = [] 
    try:
        with open(filename, mode = 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader)
            lat_index= header.index(latcol)
            long_index = header.index(longcol)
            for row in reader:
                try:
                    lat = float(row[lat_index])
                    long = float(row[long_index])
                    arr.append((lat, long))
                except ValueError as e:
                    continue
    except Exception:
        print(f"Error reading file: {Exception}")
        return []
    return arr
    
def ask_coords():
    choice = input("Do you want to submit a csv file? (y/n)").strip().lower()
    if choice == "y":
        file = input("Enter csv filename: ").strip()
        lat = input("Enter the columon name of the Latitude:").strip()
        long = input("Enter the columon name of the Longitude:").strip()
        arr = readfile(file, lat, long)
        return arr
    
    elif choice == "n":
        print("Enter the array (format: latitude,longitude): ")
        print("Type 'done' when you are finished.")
        arr = []
        while True:
            user_input = input("Enter point: ").strip()
            if user_input.lower() == 'done':
             break
            try:
                lat, long = map(float, user_input.split(","))
                arr.append((lat,long))
            except ValueError:
                print("Invalid input! Please enter in the correct format")
        return arr
    else:
        print("Invalid choice!")
        return []

# Converts DMS (Degrees, Minutes, Seconds) to Decimal Degrees
def dms_to_decimal(degrees, minutes, seconds, direction):
    decimal = float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    if direction.upper() in ['S', 'W']:  # South or West, make it negative
        decimal *= -1
    return decimal

def main():
    # arr1 = [(37.7749, -122.4194), (34.0522, -118.2437)]  # Example: San Francisco, Los Angeles
    # arr2 = [(36.7783, -119.4179), (40.7128, -74.0060)]   # Example: California, New York
    print("This program matches locations in the first array to their closest location in the second array.\n")
    print("For the first array, ")
    arr1 = ask_coords()
    if not arr1:
        print("Array 1 must contain at least one point!")
        return
    print("For the second array, ")
    arr2 = ask_coords()
    if not arr2:
        print("Array 2 must contain at least one point!")
        return


    #Compute the closest matches
    result = disarr(arr1, arr2)
    for key, value in result.items():
        print(f"{key} in Array 1 is closest to {value} in Array 2.")

if __name__ == "__main__":
    main()
