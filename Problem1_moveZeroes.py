def move_zeroes(nums):
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left] = nums[right]
            left += 1

    for i in range(left, len(nums)):
        nums[i] = 0

    return nums


nums = list(map(int, input().split(",")))
print(move_zeroes(nums))