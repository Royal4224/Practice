def meeting_planner(slotsA, slotsB, dur):
    i, j = 0, 0
    while i < len(slotsA) and j < len(slotsB):
        a_beg, a_end, b_beg, b_end = slotsA[i][0], slotsA[i][1], slotsB[j][0], slotsB[j][1]
        max_beg = max(a_beg, b_beg)
        min_end = min(a_end, b_end)

        if max_beg < min_end:
            if verify_difference(max_beg, min_end, dur):
                return [max_beg, max_beg + dur]

        if min_end == a_end:
            i += 1
        else:
            j += 1

    return []


def verify_difference(beg, end, dur):
    if end - beg >= dur:
        return True
    return False


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(slotsA, slotsB, dur))

dur = 12
print(meeting_planner(slotsA, slotsB, dur))

dur = 5
print(meeting_planner(slotsA, slotsB, dur))