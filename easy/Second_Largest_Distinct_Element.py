def second_largest_distinct(arr):
    largest = second = None
    for num in arr:
        if num == largest or num == second:
            continue
        if largest is None or num > largest:
            second = largest
            largest = num
        elif second is None or num > second:
            second = num
    return second if second is not None else -1
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(second_largest_distinct(arr))