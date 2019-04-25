"""
Minimum Platforms
https://practice.geeksforgeeks.org/problems/minimum-platforms/0/?ref=self
"""


def minimum_platform(arrival_time, departure_time, size):
    """
    Given arrival and departure times of all trains that reach a railway 
    station, find the minimum number of platforms required for the railway 
    station so that no train waits.
    """
    print(arrival_time, departure_time, size)
    platform_count = 1
    if size < 1:
        return 0
    i = 1
    j = 0
    while i < size and j < size:
        if arrival_time[i] >= departure_time[j]:
            i += 1
            j += 1
        else:
            i += 1
            platform_count += 1
    return platform_count


def main():
    """
    driver function
    """
    test_cases = int(input())
    while test_cases > 0:
        size = int(input())
        arrival_time = list(map(int, input().strip().split(" ")))
        departure_time = list(map(int, input().strip().split(" ")))
        departure_time_sorted = sorted(departure_time)
        platform_count = minimum_platform(arrival_time, departure_time_sorted,
                                          size)
        print(platform_count)
        test_cases -= 1


def main_h():
    """
    driver function
    """
    size = int(input())
    arrival_time = []
    departure_time = []
    j = size
    while j > 0:
        i = list(map(int, input().strip().split(" ")))
        arrival_time.append(i[0])
        departure_time.append(i[1])
        j -= 1

    departure_time_sorted = sorted(departure_time)
    platform_count = minimum_platform(arrival_time, departure_time_sorted, size)
    print(platform_count)


main_h()