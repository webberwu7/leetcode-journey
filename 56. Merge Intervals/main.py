def merge(intervals: list[list[int]]) -> list[list[int]]:
    # 先使用陣列的第一個起始值做排序
    intervals = sorted(intervals, key=lambda s: s[0])

    result = []
    current = intervals[0]
    for i in range(1, len(intervals)):
        # 看該組的尾端 是否大於等於 下一組的頭
        if current[1] >= intervals[i][0]:
            # 下一組的尾也有大於等於目前的尾
            if intervals[i][1] >= current[1]:
                current[1] = intervals[i][1]

        else:
            result.append(current)
            current = intervals[i]

    result.append(current)

    return result


def main():
    # intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
    intervals = [[1, 4], [2, 3]]
    response = merge(intervals)

    print(response)


if __name__ == '__main__':
    main()
