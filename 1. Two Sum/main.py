def twoSum(nums: list[int], target: int) -> list[list[int]]:
    nums_map = {}

    for i in range(0, len(nums)):
        diff = target - nums[i]

        if nums_map and diff in nums_map:
            return [nums_map[diff], i]
        else:
            nums_map[nums[i]] = i


def main():
    nums = [7, 11, 15, 2]
    target = 9
    response = twoSum(nums, target)

    print(response)


if __name__ == '__main__':
    main()
