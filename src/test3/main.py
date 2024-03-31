A = [[1, 5], [10, 14], [16, 18], [19, 23]]
B = [[2, 6], [8, 10], [11, 20], [25, 80], [90, 97], [99, 109]]


class Solution:
    def mergeTwoSortedList(self, A, B):
        if A[0] > B[0]:
            A, B = B, A

        res = [A[0]]
        i, j = 1, 0

        while i < len(A) and j < len(B):
            # Make sure res[-1] is not overlap with neither A[i] nor B[j]
            minVal, maxVal = res[-1]
            al, ar = A[i]
            if ar <= maxVal:
                i += 1
                continue
            if al <= maxVal:
                res[-1] = [minVal, ar]
                i += 1
                continue
            bl, br = B[j]
            if br <= maxVal:
                j += 1
                continue
            if bl <= maxVal:
                res[-1] = [minVal, br]
                j += 1
                continue
                # there are only 3 cases:
                # 1) B[j] is in the gap of res[-1] and A[i], or  insert B[j] and move j forward
                # 2) A[i] is in the gap of res[-1] and B[j], or  insert A[i] and move j forward
                # 3) A[i], B[j] overlaps, then append the union to res[-1], move i, j forward
            if br < al:
                res.append(B[j])
                j += 1
            elif ar < bl:
                res.append(A[i])
                i += 1
            else:
                res.append([min(al, bl), max(ar, br)])
                i += 1
                j += 1

        res.extend(A[i:])
        res.extend(B[j:])
        print(res)
        return res


s = Solution()
s.mergeTwoSortedList(A, B)

