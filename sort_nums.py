# solution([1,2,3,10,5]) # should return [1,2,3,5,10]
# solution(None) # should return []


def solution(nums):
    if nums is None:
        return []

    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


print(solution([1, 2, 3, 10, 5]))
