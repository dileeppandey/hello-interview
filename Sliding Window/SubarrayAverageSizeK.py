class SubarrayAverageSizeK(object):

    def calculate(self, arr, K):
        windowStart = 0
        windowSum = 0
        length = len(arr)
        result = [0] * (length - K + 1)
        for windowEnd in range(length):
            windowSum += arr[windowEnd]
            if windowEnd >= K - 1:
                result[windowStart] = windowSum / K
                windowSum -= arr[windowStart]
                windowStart += 1
        return result


sb = SubarrayAverageSizeK()
print(sb.calculate([1, 2, 3, 4, 5, 6, 7], 3))
