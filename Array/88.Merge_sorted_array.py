# Общий способ решения
class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        common = m + n - 1

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[common] = nums1[first]
                first -= 1
            else:
                nums1[common] = nums2[second]
                second -= 1
            common -= 1


# Второй питоновский вариант
class SolutionTwo:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2[:]

        nums1.sort()
