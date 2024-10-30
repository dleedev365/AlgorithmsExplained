'''
How Quickselect Works
    1. Choose a Pivot: Like in Quicksort, we start by selecting a pivot element from the list.
    2. Partition the Array: Rearrange elements around the pivot so that elements less than the pivot are on the left and elements greater are on the right.
    3. Recursive Selection:
        If the pivot’s position is exactly 𝑘, then we’ve found the kth smallest element.
        If k is smaller than the pivot index, recursively search the left subarray.
        If k is larger, recursively search the right subarray.
'''
class Solution:
    def quickSelect(self, arr, k, left=0, right=None):
        if not right:
            right = len(arr) - 1
        
        if left == right:
            return arr[left]
        
        pivot_index = self.partition(arr, left, right)

        if pivot_index == k:
            return arr[pivot_index] 
        elif k < pivot_index: # recursivley search left subarr
            return self.quickSelect(arr, k, left, pivot_index - 1)
        else: 
            return self.quickSelect(arr, k, pivot_index + 1, right)


    def partition(self, arr, left, right):
        # Note: choose a pivot index wisely, (it can lead to the worst case: O(N^2))
        pivot_index = len(arr) - 1 # choose the last index to reduce the chance of the worse case
        pivot = arr[pivot_index]

        # move the pivot to the end
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

        i = left # i is the index of sorted sub array such that all elements are smaller than pivot

        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i] 
                i += 1

        # once done, move the pivot_index into it's right place
        arr[pivot_index], arr[i] = arr[i], arr[pivot_index]

        return i       
        

# Test
arr = [3,2,1,5,4]
k = 2
result = Solution().quickSelect(arr, k-1) # k is 1-indexed
print(f'expected: 2, result: {result}')