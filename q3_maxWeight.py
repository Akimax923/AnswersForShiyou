def mean(subset):
    return sum(subset) / len(subset)

def median(sorted_subset):
    length = len(sorted_subset)
    mid = length // 2
    if length % 2 == 0:
        return (sorted_subset[mid-1] + sorted_subset[mid]) / 2
    else:
        return sorted_subset[mid]

def mean_median_diff(sorted_subset):
    mean_val = mean(sorted_subset)
    median_val = median(sorted_subset)
    return mean_val - median_val

def max_mean_median_difference(n, a):
    if n == 0:
        return float('-inf')  # 空数组处理

    max_difference = float('-inf')
    
    for length in range(1, n + 1):  # 子序列长度
        for i in range(n - length + 1):  # 起始位置
            subset = a[i:i + length]  # 获取子序列
            diff = mean_median_diff(subset)
            if diff > max_difference:
                max_difference = diff
    
    return max_difference

