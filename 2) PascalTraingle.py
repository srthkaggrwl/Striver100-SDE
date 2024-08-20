# p=[1,1]
# p.insert(1, p[0]+p[1])
# print(p)

class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            print([[1]])
        
        elif numRows == 2:
            print([[1],[1,1]])
        else:
            arr = [[1],[1,1]]
            
            for i in range(numRows-2):
                prev_arr = arr[-1]
                new_arr = [1,1]
                for j in range (1,len(prev_arr)):
                    new_arr.insert(j, prev_arr[j-1]+prev_arr[j])
                arr.append(new_arr)
            print(arr)

        
solution = Solution()
solution.generate(5)    