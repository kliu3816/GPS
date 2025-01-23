# GPS
Assignment 1 for EC530
Made with Python

# Features:
- Calculate the distance between two coordinates using the Haversine formula.
  Distance = 3963.0 * arccos[(sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2-long1)]
- Match each point in one list of coordinates to the closest point in another list.
- Interactive user input to create custom coordinate lists.

# Example Input/Output:
# input:
Enter the first array (format: latitude,longitude):  
Enter point: 37.7749,-122.4194  
Enter point: 34.0522,-118.2437  
Enter point: done  

Enter the second array (format: latitude,longitude):  
Enter point: 36.7783,-119.4179  
Enter point: 40.7128,-74.0060  
Enter point: done  

# output:
(37.7749, -122.4194) in Array 1 is closest to (36.7783, -119.4179) in Array 2.  
(34.0522, -118.2437) in Array 1 is closest to (36.7783, -119.4179) in Array 2.  
