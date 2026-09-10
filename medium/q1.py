def subarray_sum_equals_k(nums, k):
    count = {0: 1}
    prefix_sum = 0
    result = 0
    for num in nums:
        prefix_sum += num
        result += count.get(prefix_sum - k, 0)
        count[prefix_sum] = count.get(prefix_sum, 0) + 1
    return result


def main():
    # Read n and K
    n, k = map(int, input("Enter n and K (space-separated): ").split())

    # Read the array
    arr = list(map(int, input(f"Enter {n} space-separated integers: ").split()))

    if len(arr) != n:
        print(f"Warning: expected {n} numbers but got {len(arr)}.")

    answer = subarray_sum_equals_k(arr, k)
    print("Number of subarrays with sum equal to K:", answer)


if __name__ == "__main__":
    main()