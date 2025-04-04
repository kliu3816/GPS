# tests/test.py

from gps import distance, dms_to_decimal, disarr

def test_distance_sf_to_la():
    # San Francisco to Los Angeles ≈ 559 km
    d = distance(37.7749, -122.4194, 34.0522, -118.2437)
    assert 550 <= d <= 570

def test_dms_to_decimal_conversions():
    # North and East should be positive
    assert round(dms_to_decimal(40, 26, 46, 'N'), 4) == 40.4461
    assert round(dms_to_decimal(79, 58, 56, 'E'), 4) == 79.9822

    # South and West should be negative
    assert round(dms_to_decimal(40, 26, 46, 'S'), 4) == -40.4461
    assert round(dms_to_decimal(79, 58, 56, 'W'), 4) == -79.9822

def test_disarr_closest_match():
    arr1 = [(37.7749, -122.4194), (34.0522, -118.2437)]  # SF, LA
    arr2 = [(36.7783, -119.4179), (40.7128, -74.0060)]   # Fresno, NYC

    result = disarr(arr1, arr2)

    assert result[(37.7749, -122.4194)] == (36.7783, -119.4179)  # SF -> Fresno
    assert result[(34.0522, -118.2437)] == (36.7783, -119.4179)  # LA -> Fresno
