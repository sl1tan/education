def check(arr, k):
    n = len(arr)
    places_nearby = 0
    for i in range(n):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                if places_nearby == 0:
                    places_nearby += 1
                else:
                    if arr[i][j - 1] == 0:
                        places_nearby += 1
                    else:
                        places_nearby = 0
            else:
                places_nearby = 0

            if places_nearby == k:
                return i + 1

            if j == len(arr[i]) - 1:
                places_nearby = 0
    return 0


n, m = [int(i) for i in input().split()]
cinema = [[int(j) for j in input().split()] for i in range(n)]
places = int(input())

print(check(cinema, places))
