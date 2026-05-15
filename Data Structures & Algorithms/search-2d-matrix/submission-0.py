class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # log (m * n) = log m + log n. 

        # "flattening" the matrix to be 1 dimensional then doing a binary search
        # could give us an o(log(n))

        # brute force is run 2 nested for loops
        """
        for r in rows:
            for c in cols:
                if matrix[r][c] == target
                    return true
        return false
        """

        # binary search 
        # flattening
        # log m + log n = binary search on m rows + binary search on n cols
        # think of a LARGE 1d matrix

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows*cols-1 # the very last value
        while left <= right: #std binary search implementation
            
            mid = (left+right)//2
            equivalentValue = mid%cols
            matrixNumber = mid//cols
            matrixValue = matrix[matrixNumber][equivalentValue]
            
            


            if matrixValue == target:
                return True
            if matrixValue > target:
                right = mid -1
            else:
                left = mid + 1


        return False



