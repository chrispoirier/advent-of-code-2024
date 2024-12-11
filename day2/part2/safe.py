def check_safe(d):
    not_all_increasing = False
    not_all_decreasing = False
    diff_gt_3 = False
    diff_lt_1 = False
    if d[0] < d[1]:
        for i in range(1, len(d)):
            if d[i] <= d[i-1]:
                not_all_increasing = True
            if abs(d[i] - d[i-1]) > 3:
                diff_gt_3 = True
            if abs(d[i] - d[i-1]) < 1:
                diff_lt_1 = True
    elif d[0] > d[1]:
        for i in range(1, len(d)):
            if d[i] >= d[i-1]:
                not_all_decreasing = True
            if abs(d[i] - d[i-1]) > 3:
                diff_gt_3 = True
            if abs(d[i] - d[i-1]) < 1:
                diff_lt_1 = True
    else:
        not_all_increasing = True
        not_all_decreasing = True
    if not not_all_increasing and not not_all_decreasing and not diff_gt_3 and not diff_lt_1:
        return True
            
    return False