class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        # Extend nums1 with zeros to make space for nums2
        nums1[m:] = [0] * n  # Append zeros based on the length of nums2
        
        i, j = 0, 0  # Start with the first elements of nums2 and the portion of nums1 to be merged
        while i < n and j < m + n:
            # If nums2[i] should be placed before nums1[j], or we've reached the appended zeros
            if j == m + i or nums2[i] < nums1[j]:
                # Move elements in nums1 to the right to make space for nums2[i]
                nums1[j+1:m+i+1] = nums1[j:m+i]
                # Place nums2[i] into its correct position
                nums1[j] = nums2[i]
                i += 1  # Move to the next element in nums2
            j += 1  # Move to the next position in nums1